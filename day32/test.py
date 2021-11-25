
#testing strin methods

def test1():
    string="""
quote1
quote2
quote3
quote4
quote5
quote6
quote7
quote8
    """
    string = string.strip()
    quotes = string.split("\n")
     
    for i in range(len(quotes)):
        print(f"index={i+1} | quote={quotes[i]}")
#test1()

#testign dicts
def test2():
    my_dict = {
            "key1":"value1",
            "key2":"value2",
            "key3":"value3",
            "key4":"value4",
    }

    for key in my_dict:
        print(key)
        print(my_dict[key])

#test2()
