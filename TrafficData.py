import urllib.request
import os
import ssl
import json
import datetime


import createMetrics

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):

    ssl._create_default_https_context = ssl._create_unverified_context


def trafficData():

    lastReadDate = createMetrics.getLatestFileDate()
    print(lastReadDate)

    x = urllib.request.urlopen(
        'https://data.cityofchicago.org/resource/m6dm-c72p.json').read()
    y = json.loads(x)

    chicagoRecords = []

    now = datetime.datetime.now()

    for record in y:
        
        chicagoRecord = {}

        if 'trip_start_timestamp' in record: #add trip start timestamp
            startTime = record['trip_start_timestamp']
            startTimeObj = datetime.datetime.strptime(startTime, '%Y-%m-%dT%H:%M:%S.000')
            chicagoRecord['trip_start_timestamp'] = startTime
            
            if not lastReadDate or lastReadDate <= startTimeObj:
                
                if 'pickup_centroid_latitude' in record: #add pickup latitude
                    chicagoRecord['pickup_centroid_latitude'] = record['pickup_centroid_latitude']
                else:
                    chicagoRecord['pickup_centroid_latitude'] = 0.0

                if 'pickup_centroid_longitude' in record: #add pickup longitude
                    chicagoRecord['pickup_centroid_longitude'] = record['pickup_centroid_longitude']
                else:
                    chicagoRecord['pickup_centroid_longitude']=0.0

                if 'dropoff_centroid_latitude' in record: #add dropoff latitude
                        chicagoRecord['dropoff_centroid_latitude'] = record['dropoff_centroid_latitude']
                else:
                            chicagoRecord['dropoff_centroid_latitude']=0.0

                if 'dropoff_centroid_longitude' in record: #add dropoff longitude
                    chicagoRecord['dropoff_centroid_longitude'] = record['dropoff_centroid_longitude']    
                else:
                        chicagoRecord['dropoff_centroid_longitude'] = 0.0
                
                if 'trip_miles' in record: #add trip length in miles
                    chicagoRecord['trip_miles'] = record ['trip_miles']
                else:
                        chicagoRecord['trip_miles'] = 0.0

                if 'trip_seconds' in record: #add trip in seconds
                    chicagoRecord['trip_seconds'] = record ['trip_seconds']
                else:
                    chicagoRecord['trip_seconds'] = 0.0
                
                if 'trip_total' in record: #add trip cost
                    chicagoRecord['trip_total'] = record ['trip_total']
                else:
                    chicagoRecord['trip_total'] = 0.0

                if 'shared_trip_authorized' in record: # add whether a shared trip was authorized
                    chicagoRecord['shared_trip_authorized'] = record['shared_trip_authorized']
                else:
                    chicagoRecord['shared_trip_authorized'] = None

                chicagoRecord['created_on'] = str(now) #add created on date

                chicagoRecords.append(chicagoRecord)

    fileName = "chicago_records_" + str(now) + (".json")
    filePath= "data//" + fileName
    with open (filePath, 'w') as outfile:
        json.dump(chicagoRecords, outfile)


trafficData()
