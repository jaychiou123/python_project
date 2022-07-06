from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_web = response.text
soup = BeautifulSoup(empire_web, "html.parser")
movie_tag = soup.find_all(class_="title")

movie_lists = []
for i in movie_tag:
    movie_name = i.get_text()
    movie_lists.append(movie_name)
movie_lists = movie_lists[10:]
print(movie_lists)
with open("100_must_see_movie.txt", "w", encoding='UTF-8') as file:
    for line in list(reversed(movie_lists)):
        file.write(line)
        file.write('\n')