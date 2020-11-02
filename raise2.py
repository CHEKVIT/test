b = 1
c = None
try:
    if b == 0:
        raise ZeroDivisionError ('cannot divide 0')
    c = 3/b

    print('gsgsdgdsgs')
except ZeroDivisionError as e:
    print(e)
finally:
    print('hello swiata')

print('hello World')
print(c)