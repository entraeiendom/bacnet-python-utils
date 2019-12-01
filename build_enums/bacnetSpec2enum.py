import re
str = open('spec_content.txt','r').read()
replaced = re.sub(r"\n \(", "(", str)
print(replaced)
f = open("content_replaced.txt", "a")
f.write(replaced)
f.close()

camelCase = open('content_camelcase.txt','a')
with open('content_replaced.txt', 'r') as reader:
    # reader = open('spec_content.txt')
    try:
        line = reader.readline()
        while line != '':  # The EOF char is an empty string
            line = line.title()
            line = line.replace('-','');
            # line = line.replace('(', '(\'')
            # line = line.replace(')', '\')')

            print(line, end='')
            camelCase.write(line)
            line = reader.readline()
    finally:
        reader.close()
camelCase.close()