def add(a:float, b:float)  -> float | None:
    try:

        a / b
        # name name= int('great')
        lst = [1, 2, 3]
        # print(lst[6])
        # file = open('file.txt', mode='r', encoding='utf-8')
        # print(file.read())
        # print("About to close")
        # file.close()
        print (a / b)
    except ZeroDivisionError as e:
        print("Can't divide with zero -> ", e)
        # raise e
        # raise ValueError("I know all is not well")
        # return None
    except (TypeError, NameError):
        print("Type Error")
    else:
        print("Owo epo")
    # except IndexError:
    #     print("Error")
    # finally:
    #     print("About to close")

print(add(1, 2))