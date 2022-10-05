#!/usr/bin/env python
# coding: utf-8

# Definition
# -- 
# Balanced number is the number that * The sum of all digits to the left of the middle digit(s) and the sum of all digits to the right of the middle digit(s) are equal*.
# 
# 
# Notes
# -- 
# - If the number has an odd number of digits (impar) then there is only one middle digit, e.g. 92645 has middle digit 6; --> WE HAVE TO "REMOVE" ONLY ONE DIGIT
# 
# - otherwise, there are two middle digits , e.g. 1301 has middle digits 3 and 0 --> WE HAVE TO "REMOVE" TWO DIGITS
# 
# The middle digit(s) should not be considered when determining whether a number is balanced or not, e.g 413023 is a balanced number because the left sum and right sum are both 5.
# 
# Number passed is always Positive .
# 
# Return the result as String

# In[108]:


#we have to use and DEFINE the next function
def balanced_num(number):

    #we convert the integer to string to can obtain its length
    number_string = str(number).replace("-","") #to avoid negative number we convert the string into a positive number
    number_lenght = len(number_string)

    #we convert the str into a list
    number_list = list (number_string)

    #we are going to create counters to make both sums
    number_sum_left = 0
    number_sum_right = 0
    if number_string.isdigit(): #if the variable number is not a digit we print a warning
        #we have to know if the length is even or odd
        if number_lenght%2 == 0: #even (so we can not consider the two middle digits)
            print("log: ","even")
            even_division_left = number_lenght//2 - 1 # 0,1,2,3 (len=4) --> we want 0 index, so we need 1 and behind in the range
            even_division_right = number_lenght//2 + 1 # 0,1,2,3 (len=4) --> we want 3 index, so we need 3 and forward
            for i in range(0,even_division_left):
                number_sum_left += int(number_list[i])
            for e in range(even_division_right,number_lenght):
                number_sum_right += int(number_list[e])
            if number_sum_left == number_sum_right:
                return "Balanced"
            else:
                return "Not Balanced"
        else:#odd (so we can not consider the single middle digit)
            print("log: ","odd")
            even_division_left = (number_lenght-1)//2 # 0,1,2 (len=3) --> we want 0 index, so we need 1 and behind in the range
            even_division_right = (number_lenght+1)//2 # 0,1,2 (len=3) --> we want 2 index, so we need 2 and forward
            for i in range(0,even_division_left):
                number_sum_left += int(number_list[i])
            for e in range(even_division_right,number_lenght):
                number_sum_right += int(number_list[e])
            if number_sum_left == number_sum_right:
                return "Balanced"
            else:
                return "Not Balanced"
    else:
        print("log: no number in the function")


# In[122]:


balanced_num(9998)


# In[ ]:





# In[ ]:




