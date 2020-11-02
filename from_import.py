gvar = 10
def get():
    print(gvar)

def set():
    global gvar
    gvar = 5

get()
set()
get()