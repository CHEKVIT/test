b = 1
c = None
try:
    if b == 0:
        raise ZeroDivisionError("cannot divide 0")
    c = 3 / b
​
    print('hello python')
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
​
​
print("hello world")
