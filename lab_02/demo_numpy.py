
# coding: utf-8

# In[1]:

import numpy as np
a = np.arange(15).reshape(3,5)


# In[2]:

text_file = open("demo_numpy.txt", "w")
print(a)
print(a.shape)
print(a.size)
print(a.itemsize)
print(a.ndim) 
print(a.dtype)
text_file.write(str(a)+ "\n" )
text_file.write(str(a.shape)+ "\n" )
text_file.write(str(a.size)+ "\n" )
text_file.write(str(a.itemsize)+ "\n" )
text_file.write(str(a.ndim)+ "\n" ) 
text_file.write(str(a.dtype)+ "\n" )
text_file.close()


# In[ ]:



