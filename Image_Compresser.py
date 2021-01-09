from PIL import Image
import PIL

def compressor(image_path, image_path_to_save, image_quality=5):
    # Piilow grants us quality and optimize to compress an image
    picture = Image.open(image_path)
    picture.save(image_path_to_save,optimize=True,quality=image_quality)
    picture.close()