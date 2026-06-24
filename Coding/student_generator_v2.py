from Student import Student

def load_students() -> list[Student]:
    # make a data handler
    data_file = open("students.csv", "r")
    print(data_file)
    students = []

    # make a for loop to read the data line by line
    for line_of_data in data_file:
        #split the line at the comma
        split_data = line_of_data.split(",")
        try:
            kid = Student(split_data[0],split_data[1],split_data[2],float(split_data[3]),float(split_data[4]),int(split_data[5]))
        except:
            continue
        students += [kid]
    
    #close the file
    data_file.close()
    return students


def student_to_dictonary(list_of_students: list[Student]) -> list[dict]:
    student_dictonary_list = []
    for student in list_of_students:
        
        student_dictonary = {}


        student_dictonary['first_name'] = student.get_first_name()
        student_dictonary['last_name'] = student.get_last_name()
        student_dictonary['major'] = student.get_major()
        student_dictonary['gpa'] = student.get_gpa()
        student_dictonary['class'] = student.get_class_level()
        student_dictonary['id'] = student.get_id()

        student_dictonary_list.append(student_dictonary)

    return student_dictonary_list




def get_student_dictonaries():
    students = load_students()

    student_dictonaries = student_to_dictonary(students)

    return student_dictonaries


get_student_dictonaries()


