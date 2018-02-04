import re
fichier = open('test.txt', 'r')

text = fichier.read()

result = re.sub(r'"(.*)\\\\(.*)"', r'"\1\\\\\\\\\2"', text)

print(text)
print("--------")
print(result)