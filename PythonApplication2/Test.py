test =['ruan','thea','ThEa','Shorta arse']

for index in range(0,len(test)):
    print(f'{index+1}:{test[index]}')

try:
    user_input = input("Enter choice:")
    item =  test[int(user_input)-1]
    print(item)
except :
    print('pick is mofo')



