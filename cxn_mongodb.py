from den_code import ImageCoding
import time
from pymongo import MongoClient
import json

from gridfs import GridFS

mDBConnectionKey = "WRITE_KEY_HERE"

class mDB:
    def __init__(self):
        client = MongoClient(mDBConnectionKey)
        db = client["LP-Encodes"]
        self.collection = db["license_plates"]

    def w_LP_encode(self, license_plate, device_id):
        lp_img = ImageCoding(path="plaka2.jpg").encodeImage()
        
        # process for an existing plate
        if self.collection.find_one({"license_plate": license_plate}):
            self.collection.update_one({
                "license_plate": license_plate
                },
                {"$push": {
                    "previous_parks": {
                    "datetime":time.strftime('%Y.%m.%d-%H.%M.%S'),
                    "device_id":device_id,
                    "device_location": "None",
                    "lp_img": lp_img
                    }
                }})
                
        else:   # New plate detect
            data = {
                "license_plate":license_plate,
                "previous_parks": [{
                    "datetime":time.strftime('%Y.%m.%d-%H.%M.%S'),
                    "device_id":device_id,
                    "device_location": "None",
                    "lp_img": lp_img
                    }]}
            self.collection.insert_one(data)


    def r_LP_encode(self, license_plate):
        filter = {"license_plate": license_plate}
        if self.collection.find_one(filter):
            # en_code = self.collection.find_one(filter, {"previous_parks":{"$slice":-1}})      # Son girdiyi getirir.
            en_code = (self.collection.find_one(filter, {"_id":0, "datetime":1, "previous_parks":1}))
            # en_code = json.dumps(en_code, default=str)  # mongoDB'den date, bytes türleri çekilecekse gelen hata bu şekilde çözülüyor.
            with open("encode_plate.json", "w") as dnm:
                json.dump(en_code, dnm)
            # ImageCoding(license_plate).decodeImage(en_code=en_code)

        else:
            print("plaka sistemde kayıtlı değil")


if __name__ == "__main__":
    mDB().w_LP_encode(license_plate="80YIH32", device_id="34_16")
    # mDB().r_LP_encode(license_plate="80YIH32")
