#open the file
# employee_file = open("employees.txt", "r")

# open("employees.txt", "w")
# open("employees.txt", "r+")
# open("employees.txt", "a") # add new information


#--------------------- reading of the files -----------------
# print(employee_file.readable()) # return true or false 
# # print(employee_file.read()) # dispalys all the output
# print(employee_file.readline()) #read only the first line of the file
# print(employee_file.readline()) #read only the first "two" line of the file

# print(employee_file.readlines()) # put into the array 
# print(employee_file.readlines()[1]) # put into the array 


# for employee in employee_file.readlines() : # using loop read all of the contents of the file
#     print(employee)



#--------------------- writing of the files -----------------

employee_file = open("employees.txt", "a")

employee_file.write("\nCoby - Mariane") # add or write to the file
# employee_file.write("\nBaka - Admiral")


employee_file = open("employees.txt", "w") #overwrite all the existing file
employee_file.write("\nBaka - Admiral")

employee_file = open("index.html", "w") # naya file banaidinxa maybe web file as well
employee_file.write("<h2>Hello World</h2>")

employee_file.close()
