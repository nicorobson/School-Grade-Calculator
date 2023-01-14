#COURSE GRADE MODE
def course_calculator():
    print("\n-----------------\nCourse Grade Mode\n-----------------\n")
    print("This mode computes your final course mark, based on the weightage of the course's assignments (tests, labs, assignments, etc.)\n\n")

    assignments = []
    weightage = []
    marks = []
    
    course = input("Enter Course Name: ")
    print("\n")
    
    #ASSIGNMENTS
    num_assignments = input("Number of assignments in " + course + ": ")
    while (num_assignments.isdigit() == False) or (int(num_assignments) <= 0):
        print("\n~Invalid Input~\nPlease enter a number only, and ensure you enter a number >= 1\n")
        num_assignments = input("Number of assignments in " + course + ": ")

    print("\nEnter the names of each of the " + num_assignments + " assignments. Ex) Midterm 1, Assignment 2, Exam, Labs.\n\n")
    for assignment in range(int(num_assignments)):
        assign_name = input("Assignment Name: ")
        assignments.append(assign_name)

    #WEIGHTAGE
    print("\nEnter the weightage of each assignment below\n\n")
    for assignment in assignments:
        assign_weight = input("Weightage of " + assignment + ": ")
        weightage.append(assign_weight)

    while course_weightage_error(weightage) == True:
        print("\n~Invalid Weightage~\nPlease ensure the total weightage adds up to 100%\nOnly enter numbers (no letters or special characters)\n")
        weightage.clear()
        for assignment in assignments:
            assign_weight = input("Weightage of " + assignment + ": ")
            weightage.append(assign_weight)

    #MARKS
    print("\nEnter your mark for each assignment below\n\n")
    for assignment in assignments: 
        assign_mark = input("Your mark in " + assignment + ": ")
        marks.append(assign_mark)

    while mark_error(marks) == True:
        print("\n~Invalid Marks~\nPlease ensure marks are between 0-100.\nOnly enter numbers (no letters or special characters)\n")
        marks.clear()
        for assignment in assignments: 
            assign_mark = input("Your mark in " + assignment + ": ")
            marks.append(assign_mark)

    #COMPUTATION
    final_grade = course_compute(weightage, marks, num_assignments)
    grade_point_avg = gpa(final_grade)
    grade_gpa = grade_point_avg[0]
    letter_gpa = grade_point_avg[1]
    print("\nYour final mark in " + course + " is " + str(final_grade) + "%  -->  " + str(grade_gpa) + " GPA (" + str(letter_gpa) + ")\n\n")

    #MENU FUNCTIONALITY
    print("What would you like to do now?\n1) Calculate another course grade (type 'C')\n2) Go back to main menu (type 'Q')\n\n")
    user = input("Select your option: ")
    valid_input = ['C', 'c', 'Q', 'q']
    while user not in valid_input:
        print("\n~Invalid input~\n\nPlease select one of the options:\n1) Calculate another course grade (type 'C')\n2) Go back to main menu (type 'E')\n")
        user = input("Select your option: ")
    if user == 'C' or user == 'c':
        course_calculator()
    elif user == 'Q' or user == 'q':
        alt_menu()



#EXAM MODE
def exam_calculator():
    print("\n---------------\nExam Grade Mode\n---------------\n")
    print("This mode tells you the mark you need on your final exam, in order to achieve a certain course grade.\n\n")

    assignments = []
    weightage = []
    marks = []

    course = input("Enter Course Name: ")
    print("\n")
    
    #ASSIGNMENTS
    print("Please enter the number of assignments (minus final exam)\n")
    num_assignments = input("Number of assignments in " + course + ": ")
    while (num_assignments.isdigit() == False) or (int(num_assignments) <= 0):
        print("\n~Invalid Input~\nPlease enter a number only, and ensure you enter a number >= 1\n")
        num_assignments = input("Number of assignments in " + course + ": ")

    print("\nEnter the names of each of the " + num_assignments + " assignments. Ex) Midterm 1, Assignment 1, Assignment 2, Labs.\n\n")
    for assignment in range(int(num_assignments)):
        assign_name = input("Assignment Name: ")
        assignments.append(assign_name)
    
    #WEIGHTAGE
    print("\nEnter the weightage of each assignment below\n\n")
    for assignment in assignments:
        assign_weight = input("Weightage of " + assignment + ": ")
        weightage.append(assign_weight)
    exam_worth = input("How much is your final exam worth? Weightage: ")

    while exam_weightage_error(weightage, exam_worth) == True:
        print("\n~Invalid Weightage~\nPlease ensure the total weightage adds up to 100%\nOnly enter numbers (no letters or special characters)\n")
        weightage.clear()
        for assignment in assignments:
            assign_weight = input("Weightage of " + assignment + ": ")
            weightage.append(assign_weight)
        exam_worth = input("How much is your final exam worth? Weightage: ")

    #MARKS + EXAM GRADE
    print("\nEnter your mark for each assignment below\n\n")
    for assignment in assignments: 
        assign_mark = input("Your mark in " + assignment + ": ")
        marks.append(assign_mark)

    while mark_error(marks) == True:
        print("\n~Invalid Marks~\nPlease ensure marks are between 0-100.\nOnly enter numbers (no letters or special characters)\n")
        marks.clear()
        for assignment in assignments: 
            assign_mark = input("Your mark in " + assignment + ": ")
            marks.append(assign_mark)
    
    desired = input("What grade would you like to achieve in " + course + "?  -->  Grade: ")
    while desired.isdigit() == False:
        print("\n~Invalid Grade~\nPlease ensure grade is between 0-100.\nOnly enter numbers (no letters or special characters)\n")
        desired = input("What grade would you like to achieve in " + course + "?  -->  Grade: ")

    #COMPUTATION
    need = exam_compute(weightage, marks, num_assignments, exam_worth, desired)
    print("\nYou need a " + str(need) + " on your exam to achieve a " + str(desired) + "%" + " in " + course + ".\n\n")

    #MENU FUNCTIONALITY
    print("What would you like to do now?\n1) Calculate another exam grade (type 'E')\n2) Go back to main menu (type 'Q')\n\n")
    user = input("Select your option: ")
    valid_input = ['E', 'e', 'Q', 'q']
    while user not in valid_input:
        print("\n~Invalid input~\n\nPlease select one of the options:\n1) Calculate another exam grade (type 'C')\n2) Go back to main menu (type 'E')\n")
        user = input("Select your option: ")
    if user == 'E' or user == 'e':
        exam_calculator()
    elif user == 'Q' or user == 'q':
        alt_menu()


#ERROR CHECKS
def course_weightage_error(weightage):
    flag1 = True
    for weight in weightage:
        if weight.isdigit() == False:
            flag1 = False
            break
    if flag1 == True:
        sum_weightage = 0
        for weight in weightage:
            sum_weightage += int(weight)
    if (flag1 == False) or (sum_weightage != 100):
        return True
    else:
        return False

def exam_weightage_error(weightage, exam_worth):
    if (exam_worth.isdigit() == False) or (int(exam_worth) <= 0):
        return True
    flag1 = True
    for weight in weightage:
        if (weight.isdigit() == False):
            flag1 = False
            break
    if flag1 == True:
        sum_weightage = 0
        for weight in weightage:
            sum_weightage += int(weight)
    if (flag1 == False) or ((sum_weightage + int(exam_worth)) != 100):
        return True
    else:
        return False

def mark_error(marks):
    for mark in marks:
        try:
            float(mark)
        except ValueError:
            return True
    flag1 = True
    for mark in marks:
        if (isinstance(float(mark), float) == False) and (mark.isdigit() == False):
            flag1 = False
            break
    flag2 = True
    if flag1 == True:
        for mark in marks:
            if (float(mark) > 100) or (float(mark) < 0):
                flag2 = False
                break
    if (flag1 == False) or (flag2 == False):
        return True
    else:
        return False            
    

#COMPUTATION FUNCTIONS    
def course_compute(weightage, marks, num_assignments):
    numerator = 0
    for i in range(int(num_assignments)):
        numerator += int(weightage[i]) * float(marks[i])
    return round(numerator / 100)

def exam_compute(weightage, marks, num_assignments, exam_worth, desired):
    sum_of_knowns = 0
    for i in range(int(num_assignments)):
        sum_of_knowns += int(weightage[i]) * float(marks[i])
    desired = 100 * int(desired)
    right_side = int(desired) - sum_of_knowns
    return right_side / int(exam_worth)
    

#GPA CONVERSION
def gpa(grade):
    if grade >= 90:
        return [4.33, "A+"]
    elif 85 <= grade <= 89:
        return [4, "A"]
    elif 80 <= grade <= 84:
        return [3.67, "A-"]
    elif 77 <= grade <= 79:
        return [3.33, "B+"]
    elif 73 <= grade <= 76:
        return [3, "B"]
    elif 70 <= grade <= 72:
        return [2.67, "B-"]
    elif 67 <= grade <= 69:
        return [2.33, "C+"]
    elif 63 <= grade <= 66:
        return [2, "C"]
    elif 60 <= grade <= 62:
        return [1.67, "C-"]
    elif 57 <= grade <= 59:
        return [1.33, "D+"]
    elif 53 <= grade <= 56:
        return [1, "D"]
    elif 50 <= grade <= 52:
        return [0.67, "D-"]
    else: 
        return [0, "F"]    


#MAIN MENU INTERFACES
def startup_menu():
    print("\n----------------\nGrade Calculator\n----------------")
    print("\nWelcome to the Interactive Grade Calculator!\n~Please select one of the options below~\n")
    print("Use the Course Grade Calculator if you have received all your assignment grades, and would like to see your final mark.")
    print("Use the Exam Grade Calculator to see what you need on your final exam to achieve your desired course mark.")
    print("\nOptions:\nCourse Grade Calculator (type 'C')\nExam Grade Calculator (type 'E')\nQuit (type 'Q')\n")

    user = input("Select your option: ")
    valid_input = ['Q', 'q', 'C', 'c', 'E', 'e']

    while user not in valid_input:
        print("\n~Invalid input~\n\nPlease select one of the options:\nCourse Grade Calculator (type 'C')\nExam Grade Calculator (type 'E')\nQuit (type 'Q')\n")
        user = input("Select your option: ")
    if user == 'C' or user == 'c':
        course_calculator()
    elif user == 'E' or user == 'e':
        exam_calculator()
    elif user == 'Q' or user == 'q':
        print("\nThanks for using the Interactive Grade Calculator!\n")
        quit()

def alt_menu():
    print("\n\n~Please select one of the options below~")
    print("Use the Course Grade Calculator if you have received all your assignment grades, and would like to see your final mark.")
    print("Use the Exam Grade Calculator to see what you need on your final exam to achieve your desired course mark.")
    print("\nOptions:\nCourse Grade Calculator (type 'C')\nExam Grade Calculator (type 'E')\nQuit (type 'Q')\n")

    user = input("Select your option: ")
    valid_input = ['Q', 'q', 'C', 'c', 'E', 'e']

    while user not in valid_input:
        print("\n~Invalid input~\n\nPlease select one of the options:\nCourse Grade Calculator (type 'C')\nExam Grade Calculator (type 'E')\nQuit (type 'Q')\n")
        user = input("Select your option: ")
    if user == 'C' or user == 'c':
        course_calculator()
    elif user == 'E' or user == 'e':
        exam_calculator()
    elif user == 'Q' or user == 'q':
        print("\nThanks for using the Interactive Grade Calculator!\n")
        quit()


#RUNNING THE APPLICATION
startup_menu()