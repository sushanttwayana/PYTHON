#-------------------CLASS AND OBJECTS-----------------

class Students:
    def __init__(self , name, major, gpa, is_male): #maps out what attributes a students should have , initialize stdudent datatype

        self.name = name # actual name changes to passed value
        self.major = major 
        self.gpa = gpa #the student gpa will be the gpa we passed in
        self.is_male = is_male 

    #functions inside a class ---------------
    def scholarship(self) :
        if self.gpa >= 3.5 :
            return True
        
        else :
            return False
#now we can create a actual student and give the required information as an attributes which is known as object

class Question :
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer