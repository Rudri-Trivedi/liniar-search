list = [10,30,80,76,3,45,2,40,70,48,90,87]
print(list)

user_input = int(input('Enter a number. '))


for i in list:
    if i == user_input:
        print(f'index number of {i} is ..: {list.index(i)}')
