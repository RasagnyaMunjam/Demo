
'''5. Write a Python program to count the frequency of words in a file'''

a=open("C:\Users\rm21150\Desktop\Munjm/file1.txt","r",encoding='utf-8')
print(a.read())

















'''def longestSubarray(s):
     
    # Initializing i and j as left and
    # right boundaries of sliding window
    i = 0
    j = 0
    k = 1
 
    for j in range(len(s)):
         
        # If current character is '0'
        if (s[j] == '0'):
 
            # Decrement k by one
            k -= 1
 
        # If k is less than zero and character
        # at ith index is '0'
        if (k < 0 ):
            if s[i] == '0':
                k += 1
                 
            i += 1
             
    j += 1
 
    # Return result
    return j - i - 1
 
# Driver Code
if __name__ == "__main__" :
 
    S = "011101101"
print(longestSubarray(S))
'''

 
