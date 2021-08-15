#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#   Calculator v.:1.1 by BR   # 
#/////////////////////////////#
print('"Calculator (v.:1.1) by BR"')
print('- Hello!')
print('- What is your name?')
name = input('')
if name==('BlackRaser'): print('- Hello, Father')
else: 
    print('- Nice to meet you, '+name+'!')
    print('- In this version, I can read simple arithmetic expressions with two variables')
    print('- Now, enter the first number:')
    a = float(input())
    print('- Welp. And now, enter the second number:')
    b = float(input())
    sum = (0,a+b,a-b,a*b,a/b)
    d = len(sum)
    #a1 = a
    #b1 = b
    #a = str(print('- Please, wait...'))
    #b = str(print('...'))
    print('Available actions:',d-1)
    print('- '+name+', here are your numbers:',a,', ',b,'. What are you want?')
    print('1. Summation (a+b)       3. Multple (a*b)')
    print('2. Subtract (a-b)        4. Divide (a/b)')
    c = int(input())
    print('- Total:',sum[c])
