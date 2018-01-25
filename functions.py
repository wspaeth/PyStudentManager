
###########

studentInfo = []

def getStudents():
    students = [];
    for student in studentInfo:
        students.append(student["Name"]);
    return students;


def printStudents():
    for student in getStudents():
        print(student);


def addStudent(name):
    student = {"Name": name};
    studentInfo.append(student);

def save_file(student):
    try:
        f = open("students.txt", "a");
        f.write(student + '\n');
        f.close();
    except:
        print("Could not save file");

def read_file():
    try:
        f = open("students.txt", "r");
        for student in f.readlines():
            addStudent(student);
        f.close();
    except:
        print("Could not read file");

read_file();


keepGoing = True;
while keepGoing:
    response = input("Would you like to add another student? (yes/no)").upper();
    if response == "YES":
        studentName = input("Enter Student Name: ");
        save_file(studentName)
        addStudent(studentName);
    elif response == "NO":
        printStudents()
        keepGoing = False;
    else:
        print("Sorry, I don't recognize that command.  Please try again");



