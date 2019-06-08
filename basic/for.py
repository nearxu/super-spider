

name = 'bill'

if name is 'lee':
    print('hello lee')
elif name is 'bill':
    print('hello bill')

# range(start,stop,step)
def sums():
    sum = 0
    for x in range(2,101,2):
        sum +=x
    print(sum)

# sums()

def print_start():
    row = int(input('please row start'))

    # v1
    # for i in range(row):
    #     for _ in range(i+1):
    #         print('*',end='')
    #     print()
    
    # for i in range(row):
    #     for j in range(row):
    #         if j < row-i-1:
    #             print(' ',end='')
    #         else:
    #             print('*',end='')
    #     print()

    for i in range(row):
        for _ in range(row -i -1):
            print(' ',end='')
        for _ in range(2*i+1):
            print('*',end='')
        print()
    


print_start()




