print("====student file manager====")
# function to add a student record
def addstudents():
    roll_no = input("Enter Roll number: ")
    name = input("Enter Name: ")

    # Total marks and percentage of a student
    maths = float(input("enter marks in maths : "))
    science = float(input("enter marks in science : "))
    english = float(input("enter marks in english : "))
    social = float(input("enter marks in social : "))
    telugu = float(input("enter marks in telugu: "))
    urdu = float(input("enter marks in urdu: "))
    # calculate total marks of a student
    total_marks = maths+science+english+social+telugu+urdu
    # calculate percentage of a student
    percentage = (total_marks/600)*100

    # open a file in 'a' append mode so new data will be added at the end
    with open("student_record.txt","a") as file:
        file.write(f"{roll_no} | {name}, | {total_marks}, | {percentage} | \n")
    print("Student record added sucessfully!\n")

# function to view saved student record
def viewstudents():
    try:
        # open file in read mode 'r'
        with open("student_record.txt" , "r") as file:
            content = file.read()
            if (content == ""):
                print("No Student Record found...")
            else:
                print("----Student Record----")
                print("| Roll no. | Name | Total marks | Percentage |")
                print(content,"\n")
    except:
        print("No student file found. add a record first\n")

# function to search the student
def searchstudents():
    student_to_find = input("Enter Student detail to search :") 

    # Open the file in read mode ('r')
    with open("student_record.txt", "r") as file:
        for line in file:
            # Check if the word exists in the current line
            if student_to_find in line:
                # strip() removes trailing newlines so print doesn't add extra blank lines
                print(line.strip(),"\n")

def updatestudent():
    word = input("Enter a student detail you want to update :")
    updateword = input("Enter a student Updated detail you want to update :")

    with open("student_record.txt","r") as f:
        content = f.read()
    contentnew = content.replace(word,updateword)

    with open("student_record.txt", "w") as f:
        f.write(contentnew)

def deletestudent():
    student_to_remove = input("Enter a student detail you want to delete :")

    # Step 1: Read all lines from the file into memory
    with open("student_record.txt", "r") as file:
        lines = file.readlines()

    # Step 2: Overwrite the file, omitting lines that contain the target word
    with open("student_record.txt", "w") as file:
        for line in lines:
            if student_to_remove not in line:
                file.write(line)

# Main menu loop
def main():
    while True:
        print("1. Add student")
        print("2. View student")
        print("3. search student")
        print("4. UPDATE student")
        print("5. DELETE student")
        print("6. Exit")

        choice = input("Enter your choice (1-5) ")
        if choice == '1':
            addstudents()
        elif choice == '2':
            viewstudents()
        elif choice == '3':
            searchstudents()
        elif choice == '4':
            updatestudent()
        elif choice == '5':
            deletestudent()
        elif choice == '6':
            print("Exiting program good bye...")
            break

if __name__ == "__main__":
    main() 