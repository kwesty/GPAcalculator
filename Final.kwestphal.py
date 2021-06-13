import math  #This program will determine a students grade based on two user input test scores and print students GPA and letter grade and save to .txt file
def gradeSum(midTerm, final, studentName): #function to add two user grades together and write user grades to a .txt file named after the student
    if midTerm and final in range(0,51): #only except test scores between 0-50
     results = open(studentName + ".txt","w")
     sum = midTerm + final
     results.write("This is the students sum of the Midterm and Final exam: " +str(sum)+ '\n') #write student sum of tests to file
     results.close() #close .txt file
    else:
     print ("You need to enter a score between 1-50! Try again!")
     main()
     

def gradeAverage(midTerm, final, studentName): #a function to determine a grade average using the sum of the two test scores given midterm and final
    if midTerm and final in range(0,51): #only except test scores between 0-50
     results2 = open(studentName + ".txt","a")
     average = (midTerm + final) / 2
     results2.write("This is the students average grade: " +str(average)+ '\n') #write the students average to .txt file 
     results2.close() #close file 
    else:
     print ("You need to enter a score between 1-50! Try again!")
     main()
    

def letterGrade(midTerm, final): #find the student letter grade out of their test score sum out of 100
    score = midTerm + final
    if score >= 90:
     return 'A'
    elif score >= 80:
     return 'B'
    elif score >= 70:
     return 'C'
    elif score >= 60:
     return 'D'
    elif score < 60:
     return 'F'
         
    

def calculatedGPA(midTerm, final): #calculate student gpa and print using formula provided
    credits = 4.0
    lGrade= letterGrade(midTerm,final)
    if lGrade == 'A':
        gpaConvert= 4.0
    elif lGrade == 'B':
        gpaConvert= 3.0
    elif lGrade == 'C':
        gpaConvert= 2.0
    elif lGrade == 'D':
        gpaConvert= 1.0
    else:
     gpaConvert= 0.0  
    calculatedGPAStudent = (gpaConvert*credits)/credits
    print ("Your calculated GPA is: ", calculatedGPAStudent)   

   

def unitTest(gradeSum): #test funtion to test function gradesum is logically and working correctly
    if 40.0 + 40.0 == 80.0:
        print("The sum function works")
        return True
    else:
        print ("The function is broken")    
           

def enterAdditionalStudent():  #loop for the end of the program to input an additional student information if user inputs 'y'
    print('Do you want to enter another students information? y/n')
    if input().lower().startswith('y'):
     main()
    else:
     print("Goodbye!") #if user inputs 'n' the program will close
     exit()

    
    
def main():

 studentName = input("What is your name?") #collect user inputs and save to variables to use for function calculations
 studentCourse = input("What class did you take?")
  
 lineRead = open("studentExams.txt", "r") #read exam names from file provided
 lines = lineRead.readlines(1)
 lines2 = lineRead.readlines(2)
 
 midTerm = float(input("What was your grade on the " + str(lines)))
 final = float(input("What was your grade on the " + str(lines2)))
 lineRead.close()


 
 

 gradeSum(midTerm,final,studentName) #call functions
 gradeAverage(midTerm,final,studentName)
 letterGrade(midTerm,final)
 calculatedGPA(midTerm,final)
 unitTest(gradeSum(midTerm, final, studentName))

 print("The student",studentName,"recieved a,", letterGrade(midTerm,final),"in,",studentCourse,",more information on this student can be found at", studentName,".txt")
 #print user name, letter grade, gpa, and where to find .txt file created
 

 

 enterAdditionalStudent() #loop program if user wishes 
 
 

main()
