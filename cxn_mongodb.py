from encode_decode import ImageCoding
import datetime

class mDB:
    def __init__(self, license_plate, cam_id):
        self.license_plate = license_plate

    def w_LP_Encode(self):
        img_encode = ImageCoding("plaka.jpg").encodeImage()


if __name__ == "__main__":
    mDB("06YUH32", "34_01").w_LP_Encode()