import re

pattern='for'
text='This is a long line of text and tell me now!'

list = re.split(r'[aeiou]', 'abcdefghij')

print (list)

if re.search(pattern, text):
    print('Yes')
else:
    print("Text not found!")