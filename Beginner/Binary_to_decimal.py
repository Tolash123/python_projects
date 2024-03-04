print('Welcome')
print('-'*25)
ques = input('Do you want to convert to binary: ')
if ques == 'yes':
    decimal = int(input('Enter a decimal number(19): '))
    print(f'The binary of {decimal} is: ',bin(decimal))
else:
    binary = int(input('Enter a binary number(1011): '))
    
    