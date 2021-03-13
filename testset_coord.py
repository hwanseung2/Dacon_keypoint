#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch
import cv2
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[2]:


path = os.path.join("C:\\Users\\hwanseung\\Desktop\\open", "1. open", 'test_imgs')
os.listdir(path)


# In[3]:


df = pd.read_csv(os.path.join("C:\\Users\\hwanseung\\Desktop\\", "open", "1. open","efficient_crop.csv"))
df.head()

imgs = df.iloc[:, 0].to_numpy()
motions = df.iloc[:, 1:]
columns = motions.columns.to_list()[::2]
class_labels = [label.replace('_x', '').replace('_y', '') for label in columns]
keypoints = []
for motion in motions.to_numpy():
    a_keypoints = []
    for i in range(0, motion.shape[0], 2):
        a_keypoints.append((float(motion[i]), float(motion[i+1])))
    keypoints.append(a_keypoints)
keypoints = np.array(keypoints)


# In[8]:


print(len(class_labels))


# In[ ]:


red_color = (0,0,255)
patient_length = 0
for patient in sorted(os.listdir(path)):
    #img_path = os.path.join("C:\\Users\\hwanseung\\Desktop\\open\\1. open\\test_imgs\\",patient)
    #print(img_path)
    img = cv2.imread(f"C:\\Users\\hwanseung\\Desktop\\open\\1. open\\test_imgs\\{patient}")
    #print(img)
    for coord in range(24):
        temp_keypoints = keypoints[patient_length, coord, :]
        temp_keypoints = (int(temp_keypoints[0]), int(temp_keypoints[1]))
        img = cv2.line(img, temp_keypoints, temp_keypoints, red_color, 20)
        cv2.putText(img, class_labels[coord], temp_keypoints, cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0,0))
        
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    patient_length += 1
    plt.figure(dpi = 200)
    plt.imshow(img)
    plt.show()
#     cv2.imshow(mat = img)

#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# In[59]:





# In[60]:


print(img)


# In[ ]:




