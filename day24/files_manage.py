

#We can open files, like the next form, but on this way we need close manually 
#the files who we'll opened.

""" 
file = open("files_manage.txt")
contents = file.read()

print(contents)

file.close()
"""

#with the next way, we don't need remember to close the file, it'll be closed automaticly
#be careful with the mode, r=read_only - w=write_only - a=append_only
#read(), write() write()
with open("files_manage.txt",mode="a") as file:
    file.write("\nNew text")
