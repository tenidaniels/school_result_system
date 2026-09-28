# Enter student scores
#function to clculate total
#function to calculate the average
#function to determine the grade
#function to generate a report
#function to search for a student

#funct to sum all scores (total)
def calc_total(scores):
    return sum(scores)
#funct to calculate the average
def calc_average(scores):
    return sum(scores) / len(scores)

def calc_grade(avg):
    if avg >= 70:
        return "A"
    elif avg>=60:
        return "B"
    elif avg>=50:
        return "C"
    elif avg >= 45:
        return "D"
    else:
        return "F"

def generate_report(name, scores):
    total= calc_total(scores)
    average=calc_average(scores)
    grade= calc_grade(average)

    print("STUDENT REPORT")
    print(f"Name: {name}")
    print(f"Scores: {scores}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"Grade: {grade}")
    print(f"---------------------------------------------------------------------------\n")

def search_student(records, name):
    if name in records:
        print(f"\n Student {name} found!\n\n")
        generate_report(name, records[name])
    else:
        print(f"\n Student {name} Not found in the records. \n")

#main function
def main():
    records= {}
    # Add students
    # search for student
    # view all student(optional)
    # exit
    while True:
        print("-----STUDENT RESULT SYSTEM--------")
        print("1. Add student results")
        print("2. Search for student")
        print("3. View all students")
        print("4. Exit")

        option= input("Enter choice (from 1-4):")

        if option == "1":
            name= input("\n Enter student name :")

            scores= []
            subjects= ["Math", "English", "Science", "Programming"]
            for subject in subjects:
                score= float(input(f"Enter {subject} score: "))
                scores.append(score)

            records[name] = scores
            print(f"\n {name}'s result saved successfully!")

        elif option == "2":
            name= input(f"\n Enter student name to search: ")
            search_student(records, name)
        elif option == "3":
            if not records:
                print("\n no student records yet. \n")
            else:
                print("\n -----------------------All student records!!---------------------------")
                for name,scores in records.items():
                    generate_report(name, scores)

        elif option == "4":
            print("\n Exiting program....")
            break

        else:
            print("Invalid Option, try again!!!")


main()


