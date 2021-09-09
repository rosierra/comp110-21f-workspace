i: int = 0 

user_string: str = input("Give me the length of the string: ")
total: int = 0 

while i < len(user_string):
    if (user_string[i]) == "a": 
        total = total + 1
    i = i + 1
print(total)