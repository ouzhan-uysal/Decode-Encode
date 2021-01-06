import base64
import json

class ImageCoding:
    def __init__(self):
        pass

    def encodeImage(self, img_path):      # encrypt image
        img_path = open(img_path, "rb")
        img_read = img_path.read()
        img_64_encode = base64.encodebytes(img_read)
        with open("encode_plate.txt", "wb") as enimg:
            enimg.write(img_64_encode)
        return img_64_encode

    def decodeImage(self, code_path):      # decrypt image
        with open(code_path, "rb") as deimg:
            decode = deimg.read()
        img_64_decode = base64.decodebytes(decode)
        with open("decode_plate.jpg", "wb") as deimg:
            deimg.write(img_64_decode)


if __name__ == "__main__":
    # r = ImageCoding().encodeImage(img_path="plaka.jpg")

    ImageCoding().decodeImage(code_path="encode.txt")