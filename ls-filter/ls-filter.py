li=[]

my_file = open("raw4", "r")
content_list = my_file.readlines()

#print(content_list)

for i, line in enumerate(content_list):
    li.append(line[57:-6])

print(li)
print(len(li))
