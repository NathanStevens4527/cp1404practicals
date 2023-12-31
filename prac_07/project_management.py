"""
program for loading and managing projects
unfortunately this program is incomplete
"""

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
    print(projects[3])

    print(projects[4].is_completed(projects[4].completion_percentage))
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
            projects.sort()
            completed_projects = []
            incomplete_projects = []
            for project in projects:
                if project.is_completed(project.completion_percentage):
                    completed_projects.append(project)
                else:
                    incomplete_projects.append(project)
            print(incomplete_projects)
            print(completed_projects)
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
    out_file = open(file, "w")
    initial_line = "Name	Start Date	Priority	Cost Estimate	Completion Percentage"
    print(initial_line, file=out_file)
    for project in projects:
        line = f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}"
        print(line, file=out_file)
    out_file.close


def load_projects(projects, file):
    in_file = open(file, "r")
    in_file.readline()
    for line in in_file:
        line = line.strip().split("\t")
        project = Project(line[NAME_INDEX], line[START_DATE_INDEX], line[PRIORITY_INDEX], line[COST_ESTIMATE_INDEX], line[COMPLETION_PERCENTAGE_INDEX])
        projects.append(project)
    in_file.close()
    return projects


main()
