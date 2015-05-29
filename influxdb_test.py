import time
from influxdb import InfluxDBClient
json_body = [
        {
            "name": "cpu_load_short",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": "2009-11-10T23:00:00Z",
            "fields": {
                "value": 0.64
            }
        }
    ]
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'mydb2')
#client.create_database('mydb2')

start_time = time.time()
for i in range(100):
    client.write_points(json_body, None, "mydb2", "default", None, 1000)
print 'Time for batch of Size 1000: ',(time.time() - start_time)

start_time = time.time()
for i in range(1000):
    client.write_points(json_body, None, "mydb2", "default", None, 100)
print 'Time for batch of Size 100: ',(time.time() - start_time)

start_time = time.time()
for i in range(10000):
    client.write_points(json_body, None, "mydb2", "default", None, 10)
print 'Time for batch of Size 10: ',(time.time() - start_time)

start_time = time.time()
for i in range(100000):
    client.write_points(json_body, None, "mydb2", "default", None, 1)
print 'Time for batch of Size 1: ',(time.time() - start_time)