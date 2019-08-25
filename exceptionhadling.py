# try:
#     print(x)
# except Exception as error:
#     print('There is some issue : {} '.format(error))

# print('Hello')

try:
    f = open('ne1ws.txt',mode = 'r',encoding='utf-8')
except FileExistsError as error:
    print('in catch {}'.format(error))
finally:
    f.close()

# check if the file is open