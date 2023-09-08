import cv2 as cv
import pytesseract as pt
from PIL import Image
from pytesseract import Output

path = "images/wiki.png"
image = cv.imread(path)
text = pt.image_to_string(Image.open(path))
boxes = pt.image_to_boxes(Image.open(path), output_type=Output.DICT)

print("detected text:", text)
for l, r, b, t in zip(boxes["left"], boxes["right"], boxes["bottom"], boxes["top"]):
    image = cv.rectangle(image, (l, t), (r, b), 2)

cv.imshow('image with box', image)

k = cv.waitKey(0)
