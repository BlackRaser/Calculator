#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#   Calculator v.:1.3 by BR   # 
#/////////////////////////////#
print('"Calculator (v.:1.3) by BR"')
print('- Hello!')
name = input('- What is your name?\n')
if name==('BlackRaser'): print('- Hello, Father')
else: 
    print('- Nice to meet you, '+name+'!')
    print('- In this version, I can read simple arithmetic expressions with two variables')
    a = float(input('- Now, enter the first number:\n'))
    b = float(input('- Welp. And now, enter the second number:\n'))
    sum = (0,a+b,a-b,a*b,a/b)
    d = len(sum)
    print('Available actions:',d-1)
    print('- '+name+', here are your numbers: '+str(a)+', '+str(b)+'. What are you want?')
    print('1. Summation (a+b)       3. Multple (a*b)\n2. Subtract (a-b)        4. Divide (a/b)')
    c = int(input())
    print('- Total: '+str(sum[c]))