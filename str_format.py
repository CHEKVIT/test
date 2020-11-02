testTumple = ("apple", "banana", "cherry")
print(testTumple)

tmp = list(testTumple)
tmp[1] = "kiwi"
testTumple= tuple(tmp)
print(testTumple)

thistumple = ("apple",)
print(type(thistumple))

thistumple = ("apple" )
print(type(thistumple))