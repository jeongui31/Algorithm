string=input()
result=''

for s in string:
    if s.isalpha():
        if s.isupper():
            result+=chr(65+(ord(s)+13-65)%26)
        elif s.islower():       
            result+=chr(97+(ord(s)+13-97)%26)
    else:
        result+=s
    
print(result)