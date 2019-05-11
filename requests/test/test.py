

def fun():
    for i in range(100):
        def fun2(i):
            print(i)
    fun2(3)


def fun():
    for i in range(100):
        for j in range(100):
            def fun2(i):
                print(i)
      fun2(3)


fun()
