# captcha_generator
creates a captcha generator using YOLOv3 and openCV

#sample result:
![ScreenShot](https://github.com/Tab-sp/captcha_generator/blob/main/sample_result.jpg)


##explanation
1) get image
2) crop so dimention is biggest possible square
  - get smallest side length between width and height
  - reshape using openCV so dimention is side X side
3) run through yolov3 model to get detection of general objects stored in coco.name
4) get most frequently occuring object, discard detection of all rest
5) fill green, (0,255,0), boxes on found objects
6) chop up the image into 9 even pieces, 3X3
7) count number of green pixels in each piece
  - True if number of green pixel is greater than 20% of greatest green pixel count in a piece
  - False if not
  - store values in an array (lets call it A)
8) chop up original image with same process
9) use pygame GUI to display it
10) click each images in pygame GUI to alter value of a temporary array
11) if the values of temporary array equals to A, return correct
