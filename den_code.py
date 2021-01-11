import base64
import json

class ImageCoding:
    def __init__(self, path):   # read file in path
        with open(path,"rb") as img:
            self.read_img = img.read()

    def encodeImage(self):      # encrypt image
        img_64_encode = base64.b64encode(self.read_img).decode("utf-8")
        # with open("encode_plate2.txt", "wb") as enimg:
        #     enimg.write(img_64_encode)
        return img_64_encode

    def decodeImage(self, en_code):      # decrypt image
        if en_code:
            img_64_decode = base64.decodebytes(en_code)
            with open("decode_plate.jpg", "wb") as deimg:
                deimg.write(img_64_decode)
        else:
            img_64_decode = json.loads(self.read_img.decode('utf-8'))
            img_64_decode = img_64_decode["previous_parks"][0]
            img_64_decode = base64.b64decode(img_64_decode["lp_img"])
            with open("decode_plate.jpg", "wb") as deimg:
                deimg.write(img_64_decode)


if __name__ == "__main__":
    # ImageCoding(path="plaka.jpg").encodeImage()
    ImageCoding(path="encode_plate.json").decodeImage(None)