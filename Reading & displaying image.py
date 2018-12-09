
# coding: utf-8

# In[1]:

# import library
import cv2


# In[2]:

# main function
def main():
    """
    Function to read image path & display accordingly
    """
    image_path = "E:\standard_test_images\standard_test_images\lena_color_512.tif"
    img = cv2.imread(image_path)
    
    # create separate window for image
    cv2.namedWindow("Lena", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Lena", img)
    cv2.waitKey(0)
    cv2.destroyWindow("Lena1")


# In[3]:

if __name__ == "__main__":
    main()


# In[ ]:



