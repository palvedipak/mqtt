from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

@app.get("/fetch_sensor_readings")
def fetch_sensor_readings(start: str, end: str):
    # Connect to MongoDB and fetch data within the specified range
    client = MongoClient("mongodb://mongodb_username:mongodb_password@mongodb_host:27017/")
    db = client["sensor_data_db"]
    collection = db["sensor_readings"]
    data = collection.find({"timestamp": {"$gte": start, "$lte": end}})
    return list(data)

@app.get("/last_ten_sensor_readings")
def last_ten_sensor_readings(sensor_id: str):
    # Connect to Redis and fetch the last ten sensor readings
    # Note: You need to implement Redis interaction here
    # Use the sensor_id to retrieve the relevant data
    return []

