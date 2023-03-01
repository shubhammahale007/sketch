#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


img=cv2.imread("F:\shubzz\gettyimages-171165631-594x594.jpg")
gr=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
invert=cv2.bitwise_not(gr)
blur=cv2.GaussianBlur(invert,(21,21),0)
invertedblur=cv2.bitwise_not(blur)
sketch=cv2.divide(gr,invertedblur,scale=256.0)
cv2.imshow('original img ',img)
cv2.imshow('gray img',gr)
cv2.imshow('invert img ',invert)
cv2.imshow('blur img ',blur)
cv2.imshow('invertedblur img ',invertedblur)
cv2.imshow('sketch img ',sketch)


# In[ ]:


cv2.waitKey(0)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




