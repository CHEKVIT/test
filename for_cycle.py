arrMatch = [1, 3, 5, 6, 7, 8, 9]
arr = [1, 2, 3, 4, 5, 'abc']
def one(arrMatch, arr):
    tmp = list(arrMatch)
    index = 0
    for i in arrMatch:
        if i in arr:
            tmp.remove(i)
            print('{name} found '.format(name = i))
        index += 1
    return tmp
tmp = one(arrMatch, arr)
itemCount = len(tmp)
print(tmp)
print(itemCount)