from bs4 import BeautifulSoup
import requests


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
content = response.text

soup = BeautifulSoup(content, "html.parser")
list_movies_name = [movie.text for movie in soup.find_all(name="h3", class_="title")]
list_movies_name.reverse()
list_movies_name[0] = f"1) {list_movies_name[0]}"

with open("movies.txt", "w", encoding="utf8") as f:
    for movie in list_movies_name:
        f.write(f"{movie}\n")
