
# coding: utf-8

# In[1]:

import cv2


# In[24]:

def main():
    # image reading path
    img_path = "\standard_test_images\standard_test_images\lena_color_512.tif"
    
    #image writing path
    output_path = "\standard_test_images\output\lena_color_512.jpg"
    
    # second argument is one, which means original format
    img1 = cv2.imread(img_path, 1)
    # second argument is zero, which means gray-scale format
    img2 = cv2.imread(img_path, 0)
    
    cv2.imshow("Lena", img2)
    
    # to save image
    cv2.imwrite(output_path, img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# In[25]:

if __name__ == "__main__":
    main()


# In[ ]:



