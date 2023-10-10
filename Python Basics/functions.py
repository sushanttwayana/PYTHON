#initialize the function
# def function1(name, age) : 
#     print("Hello " + name + " you are " + str(age) + " years old") #indented bhako jati matrai function bhitra parxa

# function1("Batman", 40)    
# function1("man", 30)    

#----------------- return --------------------

# def cube(num) :
#     return(num*num*num) #breaks out of the function tyo bhanda tala ko code execute hudaina

# result = cube(4)
# print(cube(3))

#----------------- if statements --------------------

# is_male = False
# is_tall = True

# if is_male and is_tall : #and or
#     print('Hello Mr. you are tall')
# elif is_male and not(is_tall):
#     print("You are short male")
# elif not(is_male) and is_tall :
#     print ("you are long female ")
# else:
#     print ('hello Mrs you are not tall')

# def max_num(a, b ,c) :
#     if a >= b and a >= c :
#         return a
#     elif b >= a and b >= c :
#         return b
#     else :
#         return c

# max_num = max_num(5,10,15)
# print (max_num )


#----------------- dictonaries --------------------

# monthConversion = {
#     #keys can also be numbers as well as long as they are uniques
#     "Jan" : "Januray",
#     "Feb" : "Feburary",
#     "Mar" : "March", #key :values && all keys must be unique
#     "Apr" : "April",
#     "May" : "May",
#     "Jun" : "June",
#     "Jul" : "July",
#     "Aug" : "August",
#     "Sep" : "September",
#     "Oct" : "October",
#     "Nov" : "November",
#     "Dec" : "December",
# }

# # print ( monthConversion["Jan"]  +' '+ str(len(monthConversion)))
# # print(monthConversion["Nov"])
# print(monthConversion.get("Luv", "Not a valid key")) #we can specify something for a not valid key



#----------------- while loop--------------------

# i = 1
# while i <= 10 :
#     print('The number is ',str(i))
#     i += 1

# print("Done with the loop")


#----------------- for loop--------------------

# for letter in "Khwopa Acedamy" :
#     print(letter)

friends = ["Jim", "Ram" , "Johny"]
# len(friends)

# for name in friends :
#     print(name)

# for index in range(10) :
#     print(index) #print except 10

# for index in range(3, 10) :
#     print(index)

# for index in range(len(friends)) :
#     print(friends[index])

# for index in range(5):
#     if index == 0 :
#         print("first Iteraton")
#     else :
#         print("not first iteration")


#----------------- exponent function --------------------


# def raise_to_power(base_no, power_no):

#     result = 1
#     for index in range(power_no) : # range from 0 upto powernumber - 1
#         result = result * base_no
#     return result

# result = raise_to_power(5,3)
# print(result)


#----------------- 2D Lists and Nested Loops --------------------


number_grid = [
    [1, 2, 3], #row0
    [4, 5, 6],
    [7, 8, 9], 
    [0] 
]


# print(number_grid[0][0])  #[row][column]

for row in number_grid:
    # print(row)
    for column in row:
        print(column)