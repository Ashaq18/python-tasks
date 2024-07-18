def check(string):
    string = string.lower()
    vowels = set("aeiou")
    s = set()
    for char in string:
        if char in vowels:
            s.add(char)
    if len(s) == len(vowels):
        return "String contains all vowels"
    else:
        return "String does not contain all vowels"

string = input("Enter the string: ")
result = check(string)
print(result)
