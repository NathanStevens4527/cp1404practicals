from prac_07.project import Project

MENU = "(L) load projects\n" \
       "(S) save projects\n" \
       "(D) display projects\n" \
       "(F) filter projects by date\n" \
       "(A) add new project\n" \
       "(U) update project\n" \
       "(Q) quit"
FILENAME = "projects.txt"
NAME_INDEX = 0
START_DATE_INDEX = 1
PRIORITY_INDEX = 2
COST_ESTIMATE_INDEX = 3
COMPLETION_PERCENTAGE_INDEX = 4


def main():
    projects = []
    projects = load_projects(projects, FILENAME)
    print(projects)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename: ")
            try:
                in_file = open(filename)
                in_file.close()
                load_projects(projects, filename)
            except FileNotFoundError:
                print("Invalid filename")
        elif choice == "S":
            filename = input("Enter filename: ")
            try:
                out_file = open(filename)
                out_file.close()
                save_projects(projects, filename)
            except FileNotFoundError:
                print("Invalid filename")
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
    save_projects(projects, FILENAME)


def save_projects(projects, file):
    out_file = open(file, "r")
    initial_line = "Name	Start Date	Priority	Cost Estimate	Completion Percentage"
    print(initial_line, file=out_file)
    for project in projects:
        line = "\t".join(project)
        print(line, file=out_file)
    out_file.close


def load_projects(projects, file):
    in_file = open(file, "r")
    in_file.readline()
    for line in in_file:
        line = line.split("\t")
        project = Project(line[NAME_INDEX], line[START_DATE_INDEX], line[PRIORITY_INDEX],
                          line[COST_ESTIMATE_INDEX], line[COMPLETION_PERCENTAGE_INDEX])
        projects.append(project)
    in_file.close()
    return projects


main()
