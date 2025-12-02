# f = open("fileHandling/practice.txt","r")

# data = f.read(10)
# data2 = f.readline()
# print(data2)
# print(data)
# print(type(data))
# f.close()

# f = open("fileHandling/practice.txt",'w')

# f.write("this is the new line in file after opening in the write mode") #overwrites the entire file


# f = open("fileHandling/practice.txt",'a')
# f.write("    this is the new file line for append .")
# data = f.read()

# print(data)
# f.close()


#----------------with -open Method

with open("fileHandling/practice.txt") as f:
    
    print(f.read())


with open("fileHandling/practice.txt",'a') as f:
    f.write(" \n this is new line in the file ")
  