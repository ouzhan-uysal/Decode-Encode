import base64

class ImageCoding:
    def __init__(self, path):   # read file in path
        with open(path,"rb") as img:
            self.read_img = img.read()

    def encodeImage(self):      # encrypt image
        img_64_encode = base64.encodebytes(self.read_img)
        # with open("encode_plate.txt", "wb") as enimg:
        #     enimg.write(img_64_encode)
        return img_64_encode

    def decodeImage(self):      # decrypt image
        img_64_decode = base64.decodebytes(self.read_img)
        with open("decode_plate.jpg", "wb") as deimg:
            deimg.write(img_64_decode)


# if __name__ == "__main__":
    # ImageCoding(path="plaka.jpg").encodeImage()
    # # ImageCoding(path="encode_plate.txt").decodeImage()