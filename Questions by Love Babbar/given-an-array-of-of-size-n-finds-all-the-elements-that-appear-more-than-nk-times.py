# given-an-array-of-of-size-n-finds-all-the-elements-that-appear-more-than-nk-times/

from collections import Counter 
def majorityElement(self, a: List[int]) -> List[int]:
    # a=[1,2,3,5,2]
    # b=list(set(a))
    # print(b)
    k=(len(a)/3)
    x=Counter(a)
    # print(x)
    y=[]
    for i in range(len(a)):
        if x[a[i]]>k:
            y.append(a[i])
    c=list(set(y))
    return c
