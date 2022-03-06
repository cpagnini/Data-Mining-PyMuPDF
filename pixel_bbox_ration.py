#CHECKING PIXEL BBOX RATION

from PIL import Image
import fitz
from operator import itemgetter
from itertools import groupby
from pdf2image import convert_from_path



path = "PDFile\\PMC3170839_00005.pdf"
                                          

images = convert_from_path(path)
print("Pixel size")
print(images[0].size)


doc =fitz.open(path)
page = doc[0]
dict_ = page.get_text('dict')
print("Rect Size")
print(f'w: {dict_["width"]}, h: {dict_["height"]}')

ratiow = dict_["width"] / images[0].size[0]
print('\nRatio witdh: ' +str(ratiow))
ratioh = dict_["height"] / images[0].size[1]
print('\nRatio eight: ' +str(ratioh))


print("\nCropping an image as example\n")
im = images[0]
img1 = im.crop((140, 248, 1524, 619))


