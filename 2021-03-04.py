#!/usr/bin/env python
# coding: utf-8

# 1342. Number of Steps to Reduce a Number to Zero

# In[10]:


def numberOfSteps(num):
    count = 0
    while num >0:
        if num%2==0:
            num = num/2
            count+=1
            if num%2==0:
                num= num/2
                count+=1
            if num%2!=0:
                num = num-1
                count+=1
        if num%2!=0:
            num = num-1
            count+=1
            if num%2==0:
                num= num/2
                count+=1
            if num%2!=0:
                num = num-1
                count+=1
    return count

numberOfSteps(14)


# In[16]:


def numberOfSteps (num):
        cnt = 0
        while num > 0:
            if num % 2 == 0: 
                num //= 2
            else:
                num -= 1
            cnt += 1 
        return cnt 
numberOfSteps(14)


# 1528. Shuffle String

# In[19]:


s = "codeleet"
indices = [4,5,6,7,0,2,1,3]


# In[30]:


import collections

def restoreString (s, indices):
    # Create a dictionary by combining two lists 
    a = dict(zip(indices, s))
    # get Ordered Dictionary 
    od = collections.OrderedDict(sorted(a.items()))
    # turn dictionary values into string
    return  "".join(od.values())
    
print(restoreString(s,indices))    


# In[36]:


def restoreString(s, indices):
    res = [''] * len(s)
    for index, char in enumerate(s):
        res[indices[index]] = char
    return "".join(res)
print(restoreString(s,indices))    


# 1365. How Many Numbers Are Smaller Than the Current Number

# In[37]:


nums = [8,1,2,2,3]


# In[72]:


def smallerNumbersThanCurrent(nums):
    list1 = []
    
    for num in nums:
        temp = [n for n in nums if n < num]
        list1.append(len(temp))
    return list1 

smallerNumbersThanCurrent(nums)


# In[75]:


def smallerNumbersThanCurrent(nums):
    return [*map(sorted(nums).index, nums)]

smallerNumbersThanCurrent(nums)


# In[77]:


def smallerNumbersThanCurrent(nums):
    return [len(list(filter(lambda x: x < n, nums))) for n in nums]
smallerNumbersThanCurrent(nums)


# 1108. Defanging an IP Address
# 
# 

# In[79]:


address = "255.100.50.0"


# In[93]:


def defangIPaddr(address):
    return "[.]".join(address.split("."))

defangIPaddr(address)


# In[ ]:


def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))
    def defangIPaddr(self, address: str) -> str:
        return re.sub('\.', '[.]', address)
    def defangIPaddr(self, address: str) -> str:
        return ''.join('[.]' if c == '.' else c for c in address)


# 1281. Subtract the Product and Sum of Digits of an Integer

# In[114]:


n = 234
import numpy 
def subtractProductAndSum(n):
    digits = [int(x) for x in str(n)]
    a = numpy.prod(digits) - sum(digits)
    return a

subtractProductAndSum(n)


# https://www.geeksforgeeks.org/python-multiply-numbers-list-3-different-ways/

# In[127]:


n = 234
from functools import reduce

def subtractProductAndSum(n):
    a = [int(x) for x in str(n)]
    return reduce((lambda x, y: x * y), a) - reduce((lambda x, y: x + y), a)

subtractProductAndSum(n)


# In[130]:


n = 234

import numpy as np

def subtractProductAndSum(n):
    a = [int(x) for x in str(n)]
    return np.prod(a) - np.sum(a)

subtractProductAndSum(n)


# 1313. Decompress Run-Length Encoded List

# In[132]:


nums = [1,2,3,4]


# In[140]:


def decompressRLElist(nums):
    for i in range(0, len(nums)):
        [freq, val] = [nums[i], nums[i+1]]
    return [freq,val]

decompressRLElist(nums)


# 1389. Create Target Array in the Given Order
# 

# In[141]:


import collections

def restoreString (s, indices):
    # Create a dictionary by combining two lists 
    a = dict(zip(indices, s))
    # get Ordered Dictionary 
    od = collections.OrderedDict(sorted(a.items()))
    # turn dictionary values into string
    return  "".join(od.values())
    
print(restoreString(s,indices))    


# In[148]:


nums = [0,1,2,3,4]
index = [0,1,2,2,1]


# In[166]:


from collections import OrderedDict

def createTargetArray(nums, index):
    d = dict(zip(nums, index))
    sorted_dict = OrderedDict(sorted(d.items(), key=lambda a: a[1]))
    return sorted_dict

createTargetArray(nums, index)


# In[167]:


from collections import OrderedDict

def createTargetArray(nums, index):
    d = dict(zip(nums, index))
    return d

createTargetArray(nums, index)

