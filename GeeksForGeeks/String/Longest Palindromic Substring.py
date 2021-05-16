
def  ispalendrome(s):
    if ( s== s[::-1]):
        return True
    else:
        return False


def longpalendrome(s):
    n=len(s)
    best_len=0
    best_str=''
    for i in range(0,n):
        for j in range(i,n+1):
            leng=j-i+1
            string_sub= s[i:j]
            if(ispalendrome(string_sub) and leng>best_len):
                best_len=leng
                best_str=string_sub
    return best_str

a=input()
print(longpalendrome(a))

#this approach gets 0N3

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         m = ''  # Memory to remember a palindrome
#         for i in range(len(s)):  # i = start, O = n
#             for j in range(len(s), i, -1):  # j = end, O = n^2
#                 if len(m) >= j-i:  # To reduce time
#                     break
#                 elif s[i:j] == s[i:j][::-1]:
#                     m = s[i:j]
#                     break
#         return m
 
