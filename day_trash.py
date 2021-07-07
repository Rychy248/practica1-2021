var1 = "I'm var 1"

def fun1():
  print("Hello df1")


def fun2():
  print("Im fun 2")
  varfun2 = "I'm varfun2 in the fun2"
  fun1()
  print("Succes\n")

  def fun22():
    print("I'm fun22 in the fun2")
    print(varfun2)
    print(var1)
    fun1()
    print("Succes\n")

  def fun23():
    print("I'm 23 fun 3")
    print(varfun2)
    fun22()
    fun1()
    print("Succes\n")

  fun23()

def fun3():
  print("I'm the fun3")
  fun2()

fun3()
input("")
