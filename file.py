# file = open('data.txt')
# ele=file.read()
# print(ele)
# file.close()

# with open('data.txt') as file:
#     ele = file.read()
#     print(ele)

# with open('data.txt','w') as file:
#     file.write('\nWhat is your name')


with open('data.txt','a') as file:
    file.write('\nMy Name Is Rifat')