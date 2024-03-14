#Q3
#Rotate an image by 45 and 90 degrees. 

from PIL import Image

#Import the image
image = Image.open('cat.jpg')

#Rotate the image by 45 degree
rotate_45 = image.rotate(45)

#Rotate the image by 90 degree
rotate_90 = image.rotate(90)


rotate_45.save("Q3/image_rotateby45.jpg")
rotate_90.save("Q3/image_rotateby90.jpg")