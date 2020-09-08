current = 10


def change():
    global current
    current = 12

def test():
    print(current)



change()
test()