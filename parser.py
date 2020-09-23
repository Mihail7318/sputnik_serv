from bs4 import BeautifulSoup
import requests as req
import json

class pars:
    def get_pars(query):
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
        resp = req.get("https://www.kinopoisk.ru/index.php?kp_query="+query, headers=headers)
        soup = BeautifulSoup(resp.text, 'lxml')
        a = soup.find_all("a", class_="js-serp-metrika")[5]
        wen = a.get('href')
        lenght1 = wen.find("/sr/1/")
        n = wen[6:lenght1]
        "accept: application/json"
        resp2 = req.get("https://kinopoiskapiunofficial.tech/api/v2.1/films/"+n, headers={ "accept": "application/json",
"X-API-KEY": "44e89618-60b3-4d35-8cc1-33697bbe833c"})
        decoded = json.loads(resp2.text)
        dec = decoded["data"]
        description = dec["description"]
        year = dec["year"]
        genres = dec["genres"][0]["genre"]
        age = dec["ratingAgeLimits"]
        time = dec["filmLength"]
        posterUrl = dec["posterUrl"]
        Id  = dec["filmId"]
        return {'description': description, 'year': year, 'genres': genres, 'age': age, 'time': time, 'posterUrl':posterUrl}

