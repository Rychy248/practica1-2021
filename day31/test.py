#--- testing 4  Dictionaries
def testing4():
    empty_dict = {}
    dict1 = {
            'key1':'value1',
            'key2':'value2',
            'key3':'value3',
        }
    dict2 = {
            'key4':'value4',
            'key5':'value5',
            'key6':'value6',
        }
    print(dict1)
    dict1.update(dict2)
    print(dict1)
    dict1.update(empty_dict)
    print(dict1)

#testing4()

#--- testing 3  Pandas
def empty():
    import pandas 
    my_empty_dict = {

            }
    df = pandas.DataFrame(my_empty_dict)
    print(df)
#empty()

def testing3():
    import pandas
    import random
    list1 = [i*2 for i in range(3)]
    list2 = [random.randint(2,4) for _ in range(3)]
    dict1 = {
            'My list 1':list1,
            'My list 2':list2,
    }

    data_frame = pandas.DataFrame(dict1)
    print(dict1,"\n",data_frame)

    list3 = [i*3 for i in range(5)]
    list4 = [random.randint(5,6) for _ in range(5)]
    
    df2 = pandas.DataFrame({'My list 1':list3,'My list 2':list4})
    data_frame = data_frame.append(df2,ignore_index=True,sort=False)

    print("\n",data_frame)

    data_frame = data_frame.drop(index=[0,1])
    print("\n",data_frame)

#testing3()

#--- testing 2 Exceptions 
class MyException(Exception):
    pass
def testing2():
    try:
        raise MyException("This is my own error")
    except MyException:
        print("Hi i'm Rychy")

    raise MyException("This is my own error")

#testing2()

#--- testing 1 classes 
def function1():
    print("Hello i am function 1!")

    def subfunction11():
        print("Hello i am subfunction 1!")

    def subfunction12():
        print("Hello i am subfunction 2!")

class FT():
    def function1(self):
        print("Hello i am function 1!")

        def subfunction11():
            print("Hello i am subfunction 1!")

        def subfunction12():
            print("Hello i am subfunction 2!")

        self.subfunction12 = subfunction12

        print("I can call my inner function, from my main function: -> ",end=" ")
        subfunction11()

def testing1():
    ft = FT()
    ft.function1()
    
    try:
        ft.function1.subfunction12()
    except Exception as ex:
        print("Printing error: ",ex)

    try:
        print("A can call an inner function like if in the class a defined it like a atribute")
        ft.subfunction12()
    except Exception as ex:
        print("Printing error: ",ex)

#testing1()
