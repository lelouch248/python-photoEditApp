from PIL import Image,ImageEnhance,ImageFilter
import os


path = './images'
pathoutput = '/editedimages'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN)
    factor = 1.5
    enchancer = ImageEnhance.Contrast(edit)
    edit = enchancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]
    edit.save(f'.{pathoutput}/{clean_name}_edited.jpg')