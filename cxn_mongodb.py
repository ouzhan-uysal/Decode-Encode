from den_code import ImageCoding
import datetime
from pymongo import MongoClient

mDBConnectionKey = "mongodb+srv://ouz:vtld6giXyU3xuwjE@ops-cluster.oydxs.mongodb.net/LP-Encodes?retryWrites=true&w=majority"

class mDB:
    def __init__(self):
        self.client = MongoClient(mDBConnectionKey)
        # self.db = self.client[""]
        # self.connection = self.db[""]
        print(self.client.list_database_names())

    def wLPencode(self):
        ImageCoding(path="plaka.jpg").encodeImage() # img_encode
        
if __name__ == "__main__":
    mDB()