# freinds = ["Kevin", "John", "Jim","Oscar"]
# freinds[1] = "Mike"

# print(freinds[1])
# print(freinds[-2])
# print(freinds[1:]) #all after 1 including 1st element
# print(freinds[1:3]) #print 1 and 2 but not 3rd


#--------------- LIST FUNCTIONS ----------------

# lucky_numbers = [4, 8, 15, 16, 24, 5]
# freinds = ["Kevin", "John", "Jim","Oscar", "Shanks"]

# freinds.extend(lucky_numbers) # append a list to an exisiting list
# print(freinds)

# freinds.append("Zoro") # append only a new data to the exisiting list at the end
# print(freinds)

# freinds.insert(1, "Luffy") # insert new element at index 1 and all other element are pushed by 1
# freinds.remove("Jim")
# print(freinds)
# freinds.clear()
# print(freinds)

# freinds.pop() # removes or pop the last element out of the list
# print(freinds)

# print(freinds.index("Luffy")) #return the index if the element is present in the list
# print(freinds.count("Jim")) #count the no of time the value is present in the list

# freinds.sort() # sort in ascending order
# lucky_numbers.sort()
# print(freinds)

# lucky_numbers.reverse()
# print(lucky_numbers)

# freinds2 = freinds.copy() # copy all the elements
# print(freinds2)


#--------------- TUPLES ----------------

coordinates = (4, 5) #we cannot change or modify tuples
coordinates1 =[(1,2), (2,6), (0,0)]
print(coordinates[0])
