#Q3
#Rotate the image 45 and 90

import cv2
import numpy as np

#Loading the image using open cv
image = cv2.imread('dog.jpg')

#Rotate 90  degree  
rotated_image_90 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)


# Saving the processed images
cv2.imwrite('Q3/rotated_image_90_byOpenCv.jpg', rotated_image_90)

# Get the dimensions of the image
height, width = image.shape[:2]

# Define the rotation angle (in degrees)
angle = 45

# Calculate the rotation matrix
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

# Apply the affine transformation
rotated_image_45 = cv2.warpAffine(image, rotation_matrix, (width, height))

# Saving the processed images
cv2.imwrite('Q3/rotated_image_45_byOpenCv.jpg', rotated_image_45)

cv2.waitKey(0)
cv2.destroyAllWindows()