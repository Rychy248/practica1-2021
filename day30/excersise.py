#Excersice 2
facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        total_likes += 0

print("Total likes = ",total_likes)


#Excersice 1
fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        print("\n",fruit + " pie")
    except IndexError:
        print("Fruit Pie")

def asking():
    try:
        index_option = int(input("Type an index(integer) betwen 0 and 2: "))
    except ValueError:
        print("Type a number! ;)")
        asking()
    else:
        make_pie(index_option)

asking()    
#make_pie(4)


