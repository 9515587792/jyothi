y=raw_input('')
n=['a','e','i','o','u','A','E','I','O','U']
if(y>='a' and y<='z' or y>='A' and y<='Z'):
    if(y in n):
            print('Vowel')
    else:
         print('Consonant')
else:
     print('invalid')
