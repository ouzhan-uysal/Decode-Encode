from encode_decode import ImageCoding
import datetime
from pymongo import MongoClient

class mDB:
    def __init__(self, license_plate, cam_id):
        self.license_plate = license_plate
        
        client = MongoClient("mongodb+srv://ouz:c4A1P24cw01EZpc7@lp-encode-cluster.oydxs.mongodb.net/Previous-Parking-Spots?retryWrites=true&w=majority")
        db = client["Previous-Parking-Spots"]
        collection = db["license_plates"]


    def w_LP_Encode(self):
        img_encode = ImageCoding("plaka.jpg").encodeImage()



if __name__ == "__main__":
    mDB("06YUH32", "34_01")