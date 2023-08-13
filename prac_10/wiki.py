import wikipedia

search = input("Search >>> ")
while search != "":
    page = wikipedia.page(search)
    print(page.title, page.summary, page.url)
    search = input("Search >>> ")