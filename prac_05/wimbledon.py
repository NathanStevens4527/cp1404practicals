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
    champion_to_win, countries = process_data(data)
    print(countries, champion_to_win)
    print("DONE")


def get_data(file):
    data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            line = line.split(",")
            data.append(line)
        return data


def process_data(data):
    champion_to_win = {}
    countries = []
    for line in data:
        champion = line[CHAMPION_INDEX]
        if champion not in champion_to_win:
            champion_to_win[champion] = 1
        else:
            champion_to_win[champion] += 1
        country = line[COUNTRY_INDEX]
        if country not in countries:
            countries.append(country)
        countries.sort()
    return champion_to_win, countries

main()