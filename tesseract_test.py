from PIL import Image
import pytesseract as pt
from pytesseract import Output

print(pt.image_to_string(Image.open('images/wiki.png')))
print(pt.image_to_boxes(Image.open('images/wiki.png'), output_type=Output.DICT))
