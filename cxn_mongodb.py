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

        filter = {"license_plate": license_plate}
        # Burada plaka sorgula eğer veritabanında önceden kayıtlıysa oradaki previous_parks kısmına yeni parkın resmini kaydedecek.
        if self.collection.find_one(filter):
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
        else:   # Eğer plaka veritabanında kayıtlı değilse aşağıdaki işlemler uygulanacak:
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
