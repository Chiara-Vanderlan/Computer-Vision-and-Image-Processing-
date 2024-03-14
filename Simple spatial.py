#Q2
#Load an image and then perform a simple spatial 3x3 average of image pixels. 
#Repeat the process for a 10x10 neighborhood and again for a 20x20 neighborhood. 


import cv2
import numpy as np

#Loading the image using open cv
image = cv2.imread('dog.jpg')
#Function to perform spatial 3*3 avarage 
def filter(image,neighborhood_size):

    size = neighborhood_size
    padded_image = cv2.copyMakeBorder(image,size, size,size,size,cv2.BORDER_REFLECT)
    kernel = np.ones((neighborhood_size,neighborhood_size),dtype=np.float32) / (neighborhood_size ** 2)
    processed_image = cv2.filter2D(padded_image,-1,kernel)
    
    return processed_image


#applying the filter process
processed_image1 = filter(image,3)
processed_image2 = filter(image,10)
processed_image3 = filter(image,20)


# Saving the processed images
cv2.imwrite('Q2/Processed image_3x3.jpg', processed_image1)
cv2.imwrite('Q2/Processed image_10x10.jpg', processed_image2)
cv2.imwrite('Q2/Processed image_20x20.jpg', processed_image3)

cv2.waitKey(0)
cv2.destroyAllWindows()