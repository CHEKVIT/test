import string
i=list(string.ascii_lowercase)
print(i)
print(len(i))
#Task5
# There is number no letter.
number_letter = int(input("what is you the best number from 0- 26?"))
import string
string.ascii_lowercase[number_letter]
print("previously letter", string.ascii_lowercase[number_letter-1])
print("next letter",string.ascii_lowercase[number_letter+1])