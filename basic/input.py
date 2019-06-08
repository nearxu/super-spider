

import math

def area():
    radius = float(input('please r'))
    perimeter = 2*math.pi*radius
    areas = math.pi*radius*radius
    print('per:%.2f' % perimeter)

    print('areas:%.2f'%areas)

area()

def handle_string():
    str1 = 'hello world'
    print('len:%.2f' %len(str1))

    print('title first:',str1.title())

handle_string()