
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
test1()
