#!/usr/bin/env python
# coding: utf-8

# # shuffle the array

# ### zip

# In[46]:


nums = [2,5,1,3,4,7]
n = 3


# In[77]:


def shuffleArray(nums, n):
    list1 = []
    list2 = []
    list3 = []
    for i in range(0,n):
        list1.append(nums[i])
    for j in range(n,len(nums)):
        list2.append(nums[j])
    for a, b in zip(list1, list2):
        #mixing two lists is a job of zip
        list3 +=[a,b]
    return list3
print(shuffleArray(nums,3))
        


# In[ ]:


def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i, j in zip(nums[:n],nums[n:]):
            res += [i,j]
        return res


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


# # Number of Good Pairs
# 

# In[80]:


nums = [1,2,3,1,1,3]


# In[90]:


import itertools as it

def good(nums):
    list=[]
    for i in it.combinations(nums,2):
        if i[0] == i[1]:
            list.append(i[0])
            list.append(i[1])
            return list
good(nums)        


# In[136]:


def good(nums):
    count = 0
    N = len(nums)
    for i in range(N):
        for j in range(i +1, N):
            if nums[i] == nums[j]:
                count+=1
        return count
good(nums) 

