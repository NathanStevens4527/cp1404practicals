"""
program reads file and processes data for champions and countries
displays how many times each champion has won and their country.
"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    champion_to_win = {}
    countries = {}
    data = get_data(FILENAME)
    print("DONE")


def get_data(file):
    data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            line = line.split(",")
            data.append(line)
        return data


main()