from den_code import ImageCoding
import datetime
from pymongo import MongoClient

mDBConnectionKey = "mongodb+srv://ouz:123qwe!'QW@ops-cluster.oydxs.mongodb.net/LP-Encodes?retryWrites=true&w=majority"

class mDB:
    def __init__(self):
        self.client = MongoClient(mDBConnectionKey)
        self.db = self.client["LP-Encodes"]
        self.collection = self.db["license_plates"]

    def w_LP_encode(self, license_plate, device_id):
        img_encode = ImageCoding(path="plaka.jpg").encodeImage()

        # process for an existing plate
        if self.collection.find_one({"license_plate": license_plate}):
            self.collection.update_one({
                "license_plate": license_plate
                },
                {"$push": {
                    "previous_parks": {
                    "datetime":datetime.datetime.now(),
                    "device_id":device_id,
                    "device_location": "None",
                    "lp_encode": img_encode
                    }
                }})
                
        else:   # New plate detect
            data = {
                "license_plate":license_plate,
                "previous_parks": [{
                    "datetime":datetime.datetime.now(),
                    "device_id":device_id,
                    "device_location": "None",
                    "lp_encode": img_encode
                    }]}
            self.collection.insert_one(data)


if __name__ == "__main__":
    mDB().w_LP_encode(license_plate="11XYZ22", device_id="34_16")
