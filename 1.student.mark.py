# get student
def student(stu_list = []):
    numofStu = int(input("No of student: "))
    for i in range(numofStu):
        student = {} #-> dictionanry
        stu_name = input("Name: ")
        stu_id = input("ID: ")
        stu_dob = input("DOB: ")
        student['name'] = stu_name
        student['id'] = stu_id
        student['dob'] = stu_dob
        stu_list.append(student)
        
# get course
def course(course_list = [], stu_list = []):
    numofCourse = int(input("No of course: "))
    for i in range(numofCourse):
        course = {'name': {}, 'id': '', 'mark': {}}
        c_name = input("Name: ")
        c_id = int(input("ID: "))
        course['name'] = c_name
        course['id'] = c_id
        course_list.append(course)

        # get mark for course
        print("Enter mark for course id {}".format(course['id']))
        for j in range(stu_list):
            mark = course['mark']
            s_id = stu_list[j]['id']
            stu_mark = int(input("Enter mark for student {}".format(student['name'])))
            mark[s_id] = stu_mark

# show student
def student_out(stu_list = []):
    for i in range(len(stu_list)):
        id = stu_list[i]['id']
        name = stu_list[i]['name']
        dob = stu_list[i]['dob']

# show course
def course_out(course_list = []):
    for i in range(len(course_list)):
        id = course_list[i]['id']
        name = course_list[i]['name']

# show mark
def mark_out(course_list, stu_list):
    n = input("Course ID: ")

    for i in range(len(course_list)):
        if n == course_list[i]['id']:
            m = course_list[i]['mark']

            for key, value in m.item():
                print(key, ": ", value)

# main
def main():
    stu_list = []
    course_list = []

    student(stu_list)
    course(course_list, stu_list)

    while True:
        print("1. Student\n2. Course\n3. Mark\n4. Exit")
        x = int(input("Enter your choice"))
        if (x==1):
            student_out()
        elif (x==2):
            course_out
        elif (x==3):
            mark_out()
        else :
            print("bye!")
            break

# i dont know what this for but this cannot run without these
if __name__ == "__main__": 
    main()


# I dont understand so i use other student's work to "learn" (i guess),
# all i did was looking at their work and try to figure out why is that 
# and why is this. My work may resemble to that student's but i can promise 
# that i dont copy everything, at least i did what know.

# At last, my file isnt running, and I dont khnow why :)