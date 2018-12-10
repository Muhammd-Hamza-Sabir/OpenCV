
# coding: utf-8

# In[3]:

# import library
import cv2


# In[22]:

# main function
def main():
    image_path = "E:\standard_test_images\standard_test_images\lena_color_256.tif"
    # image reading in BGR format
    # img = cv2.imread(image_path, 1)
    
    # image reading in gray-scale format
    img = cv2.imread(image_path, 0)
    
    # type of read image
    print(type(img))
    
    # dtype of each pixel in image
    print(img.dtype)
    
    # shape of image (height, width, no. of channels)
    print(img.shape)
    
    # size of image (height*width*no. of channel) in bytes
    print(img.size)

    cv2.namedWindow("Lena", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Lena", img)
    cv2.waitKey(0)
    cv2.destroyWindow("Lena")


# In[23]:

if __name__ == "__main__":
    main()


# In[ ]:



