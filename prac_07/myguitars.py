from prac_06.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = load_guitars()
    guitars.sort()
    print(guitars)
    name = input("Name: ")
    while name != "":
        valid_year = False
        try:
            while not valid_year:
                year = int(input("Year: "))
                valid_year = True
        except ValueError:
            print("year must be an integer")
        valid_cost = False
        try:
            while not valid_cost:
                cost = float(input("cost: "))
                valid_cost = True
        except ValueError:
            print("cost must be a number")
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ")
    save_guitars(guitars)


def save_guitars(guitars):
    out_file = open(FILENAME, "w")
    for guitar in guitars:
        line = f"{guitar.name},{guitar.year},{guitar.cost}"
        print(line, file=out_file)
    out_file.close()


def load_guitars():
    guitars = []
    in_file = open(FILENAME)
    for line in in_file:
        line = line.strip().split(",")
        guitar = Guitar(line[0], line[1], line[2])
        guitars.append(guitar)
    in_file.close()
    return guitars


main()