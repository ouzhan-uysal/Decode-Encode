from den_code import ImageCoding
import datetime
from pymongo import MongoClient
import json

mDBConnectionKey = "mongodb+srv://ouz:123qwe!'QW@ops-cluster.oydxs.mongodb.net/LP-Encodes?retryWrites=true&w=majority"

class mDB:
    def __init__(self):
        client = MongoClient(mDBConnectionKey)
        db = client["LP-Encodes"]
        self.collection = db["license_plates"]

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


    def r_LP_encode(self, license_plate):
        filter = {"license_plate": license_plate}
        if self.collection.find_one(filter):
            # en_code = self.collection.find_one(filter, {"previous_parks":{"$slice":-1}})      # Son girdiyi getirir.
            en_code = self.collection.find_one(filter, {"_id":0, "previous_parks":1})
            # en_code = json.dumps(en_code, default=str)  # mongoDB'den date, bytes türleri çekilecekse gelen hata bu şekilde çözülüyor.
            with open("deneme.json", "w") as dnm:
                json.dump(en_code, dnm)
            # ImageCoding(license_plate).decodeImage(en_code=en_code)

        else:
            print("plaka sistemde kayıtlı değil")


if __name__ == "__main__":
    # mDB().w_LP_encode(license_plate="11XYZ22", device_id="34_11")
    mDB().r_LP_encode(license_plate="06YIH32")