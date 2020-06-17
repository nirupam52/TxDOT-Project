from dataFetch import DataFetch 

search_title = str(input("enter Feature Layer title"))
dat = DataFetch.fetch(search_title)
print(dat)