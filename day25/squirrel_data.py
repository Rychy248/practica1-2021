import pandas

data = pandas.read_csv("2018_Squirrel_Data.csv") 
dict_num_colors = dict(data["Primary Fur Color"].value_counts())
for key,value in dict_num_colors.items():
    dict_num_colors[key] = [value]
colors_pd = pandas.DataFrame(dict_num_colors)
colors_pd.to_csv("Squirrel_colors_nums.csv")
data = pandas.read_csv("Squirrel_colors_nums.csv") 
print(data)
#other practice
data = pandas.read_csv("2018_Squirrel_Data.csv") 
colors = data["Primary Fur Color"].unique()
counts = []
for color in colors:
    counts.append(len(data[data["Primary Fur Color"] == color]))
dict_num_colors = {
    "Primary Fur Color":colors,
    "Counts":counts
}
colors_pd = pandas.DataFrame(dict_num_colors)
colors_pd.to_csv("second_squirrel_data.csv")
data = pandas.read_csv("second_squirrel_data.csv") 
print("\n\n",data)
