#CREATED BY RYCHY, contact me -> jorgeajrhh@gmail.com

# import turtle 
from turtle import Turtle, Screen
from turtle import color, begin_fill, forward
from turtle import left, pos, end_fill, done

from prettytable import PrettyTable
# I solved my problem whit this page
# https://tkdocs.com/tutorial/install.html#install-x11-python

# EJercice three
table = PrettyTable()
table.add_column("Pockemon Name",['Pikachu','Raichu','Bidoof','Bibarel','Burmy'])
table.add_column("Type",['Electric','Electric','Normal','Normal-Water','Bug'])
table.align = 'c'
table.vertical_char = 'I'
table.header_style = 'upper'
print(table)
  
# EJercice two
""" 
timmy = Turtle()
timmy.shape('turtle')
timmy.color('OrangeRed4')
timmy.forward(100)

my_screen = Screen()
my_screen.exitonclick()
""" 
# DOcumetation
# https://docs.python.org/3/library/turtle.html documetation
# https://cs111.wellesley.edu/labs/lab01/colors colors


"""
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break

end_fill()
done()
"""
