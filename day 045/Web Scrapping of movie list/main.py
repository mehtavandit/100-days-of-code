from bs4 import BeautifulSoup
import requests



response = requests.get("https://www.timeout.com/film/best-movies-of-all-time")
content = response.text

soup = BeautifulSoup(content, "html.parser")
#print(soup.prettify())
#print(soup.title.string)

films = soup.find_all(name="h3", class_="_h3_cuogz_1")
#print(films)
films_name = []
for i in films:
    films_name.append(i.get_text())
#print(films_name)

with open("movies.txt", mode='w') as file:
    for i in films_name:
        file.write(f"{i}\n")
