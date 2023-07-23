from prac_06.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = load_guitars()
    print(guitars)
    guitars.sort()
    print(guitars)


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