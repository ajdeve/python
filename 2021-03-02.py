#!/usr/bin/env python
# coding: utf-8

# ##  Count Items Matching a Rule

# ### My Solution

# In[97]:


items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"

class Solution:
    def countMatches(self, items,  ruleKey, ruleValue) -> int:
        i = 0 
        for type, color, name in items:
            if ruleKey == 'type' and type == ruleValue:
                i +=1
            elif ruleKey == 'color' and color == ruleValue:
                i +=1
            elif ruleKey == 'name' and name == ruleValue:
                i +=1
        return i


# ## Other Solutions

# In[96]:


class Solution: 
    def countMatches(self, items, ruleKey, ruleValue) -> int:
        rule = {'type' : 0, 'color' : 1, 'name' : 2}
        cnt = 0
        for item in items:
            if item[rule[ruleKey]] == ruleValue:
                cnt += 1
        return cnt


# In[ ]:


def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
       return sum((ruleKey, ruleValue) in (("type", t), ("color", c), ("name", n)) for t, c, n in items)

