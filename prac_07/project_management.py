from prac_07.project import Project

MENU = "(L) load projects\n" \
       "(S) save projects\n" \
       "(D) display projects\n" \
       "(F) filter projects by date\n" \
       "(A) add new project\n" \
       "(U) update project"
FILENAME = "projects.txt"
NAME_INDEX = 0
START_DATE_INDEX = 1
PRIORITY_INDEX = 2
COST_ESTIMATE_INDEX = 3
COMPLETION_PERCENTAGE_INDEX = 4


def main():
    projects = load_projects()
    print(projects)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "":
        if choice == "L":
            filename = input("Enter filename: ")
            try:
                open(filename, "r")
            except FileNotFoundError:
                print("Invalid filename")
        elif choice == "S":
            pass
        elif choice == "D":
            print(projects)
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid choice")
        choice = input(">>> ").upper()


def load_projects():
    projects = []
    in_file = open(FILENAME, "r")
    in_file.readline()
    for line in in_file:
        line = line.split("\t")
        project = Project(line[NAME_INDEX], line[START_DATE_INDEX], line[PRIORITY_INDEX],
                          line[COST_ESTIMATE_INDEX], line[COMPLETION_PERCENTAGE_INDEX])
        print(project)
        projects.append(project)
    print(projects)
    in_file.close()
    return projects


main()
