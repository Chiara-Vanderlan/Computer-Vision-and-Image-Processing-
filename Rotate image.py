from PIL import Image

#Import the image
image = Image.open('dog.jpg')

#Rotate the image by 90 degree
rotate_90 = image.rotate(90)

#Rotate the image by 180 degree
rotate_180 = image.rotate(180)

rotate_90.save("Processed_images/image_rotateby90.jpg")
rotate_180.save("Processed_images/image_rotateby180.jpg")