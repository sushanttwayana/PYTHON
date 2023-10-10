# catching errors and exceptions

try :
    value = 10/0
    number = int(input("Enter a number :"))
    print(number)

# except ZeroDivisionError:
#     print("Divided By Zero")

except ZeroDivisionError as err:
    print(err)

except ValueError:
    print("Invalid Input")