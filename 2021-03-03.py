#!/usr/bin/env python
# coding: utf-8

# # Running Sum of 1d Array

# ## Generator 방법

# In[19]:


nums = [1,2,3,4]


# In[30]:


def run_sum_gen(nums):
    cumsum = 0
    for elt in nums:
        cumsum += elt
        yield cumsum

new_nums = list(run_sum_gen(nums))

# This takes basically no additional memory (only one float/int):
for x in run_sum_gen(nums):
    print(x)


# ## Classic While

# In[31]:


def runningSum(self, nums):
        i = 1
        while i<len(nums):
            nums[i]+=nums[i-1]
            i+=1
        return nums


# ## Accumulate

# In[ ]:


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return accumulate(nums)   


# ## Numpy

# In[29]:


import numpy as np

new_nums = np.cumsum(nums)
new_nums


# In[ ]:




