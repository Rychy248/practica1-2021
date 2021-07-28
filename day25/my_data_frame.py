import pandas


#creating a data frame 
data_dict={
    "students":["Rychy","Mary","Rouse","Mellow","Jhon"],
    "score":[9,8,7,9,7]
}
data = pandas.DataFrame(data_dict)

print(data.students)
