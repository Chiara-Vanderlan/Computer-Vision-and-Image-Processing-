import cv2
import numpy as np

#Loading the image using open cv
image = cv2.imread('dog.jpg')

#Displaying the image
#cv2.imshow('Image', image   )
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Function to perform spatial 3*3 avarage 
def filter(image,neighborhood_size):

    size = neighborhood_size
    padded_image = cv2.copyMakeBorder(image,size, size,size,size,cv2.BORDER_REFLECT)
    kernel = np.ones((neighborhood_size,neighborhood_size),dtype=np.float32) / (neighborhood_size ** 2)
    processed_image = cv2.filter2D(padded_image,-1,kernel)
    #height,width,channels = image.shape
    #new image output
    #processed_image = np.zeros((height,width,channels),dtype=np.float32)

    #Iterate over each pixel(except borders)
    #for x in range(1,height - 1):
     #   for y in range(1, width - 1):
            #3*3 neighborhood 
      #      neighbors = image[x-1:x+2,y-1:y+2]
       #     avg_b = np.mean(neighbors[:,:,0])
        #    avg_g = np.mean(neighbors[:,:,1])
         #   avg_r = np.mean(neighbors[:,:,2])

#            processed_image[x,y]=[avg_b, avg_g ,avg_r]
    return processed_image
    #return processed_image.astype(np.uint8)

#applying the filter process
processed_image1 = filter(image,3)
processed_image2 = filter(image,10)
processed_image3 = filter(image,20)

cv2.imshow('Original Image', image )
cv2.imshow('Processed Image 3x3', processed_image1 )
cv2.imshow('Processed Image 10x10', processed_image2 )
cv2.imshow('Processed Image 20x20', processed_image3 )


cv2.waitKey(0)
cv2.destroyAllWindows()