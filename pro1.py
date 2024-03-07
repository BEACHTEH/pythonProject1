def outer():
    num = 10

    def inner():
        global num  # nonlocal关键字声明
        num = 100
        print(num)

    inner()
    print(num)


outer()
