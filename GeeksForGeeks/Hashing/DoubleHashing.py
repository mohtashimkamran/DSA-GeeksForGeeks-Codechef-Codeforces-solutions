# def doubleHashing(a,k,ht,dhv):
#     for i in range(len(k)):
#         hashkey=k[i] % ht
#         if a[hashkey] == 0:
#             a[hashkey]=k[i]
#         else:
#             new_hashkey=hashkey
#             while a[new_hashkey] != 0:
#                 s = dhv-(k[i] % dhv)
#                 new_hashkey= (s+new_hashkey)%ht
#             a[new_hashkey]=k[i]
#     return a
# arr=[49,63,56,52,54,48,63]
# a=[0]*len(arr)
# hashtable_size=7
# double_hash_value=6
# print(doubleHashing(a,arr,hashtable_size,double_hash_value))

def InsertiondoubleHashing(a,k,ht,dhv):
    # for i in range(len(k)):
    hashkey = k  % ht
    if a[hashkey] == 0:
        a[hashkey]=k 
    else:
        new_hashkey=hashkey
        while a[new_hashkey] != 0:
            s = dhv-(k  % dhv)
            new_hashkey= (s+new_hashkey)%ht
        a[new_hashkey]=k 
    return a
def dele(a,k,ht,dhv):
    hashkey=k % ht
    if a[hashkey] == k:
        a[hashkey]=0
        print("Deleting!!!!!")
        print("Deleted")
    else:
        i=0
        flag=0
        new_hashkey=hashkey
        while(a[new_hashkey]!=k and i<=ht):
            s=dhv-(k%dhv)
            new_hashkey = (s+new_hashkey)%ht
            if(a[new_hashkey]==k):
                a[new_hashkey]=0
                print("Deleting!!!!!")
                print("Deleted")
                flag=1
                break
            i+=1
        if flag==0:
            print("Tried Deleting but...")
            print("Element not found!")
    return a 

hashtable_size=7
a=[0]*hashtable_size
double_hash_value=6
arr=[49,63,56,52,54,48,63]
for i in range(len(arr)):
    print(InsertiondoubleHashing(a,arr[i],hashtable_size,double_hash_value))
print("The Hashtable has been Set now you can Search,Delete or anything you want!!")
arr=[49,63,56,52,54,57,63]
for i in range(len(arr)):
    print(dele(a,arr[i],hashtable_size,double_hash_value))
# print(doubleHashing(a,arr,hashtable_size,double_hash_value))


