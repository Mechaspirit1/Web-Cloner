from bs4 import BeautifulSoup
import requests

while True:
    try:
        url_input = input("Insert URL here: ")
        create_file = open("test_file.html", "x")
        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(f"{url_input}", headers=headers)
        res_parsed = response.text

        soup = BeautifulSoup(res_parsed, 'html.parser')
        minor_headings = soup.find_all('h3')

        print(soup.prettify())
        #print(soup.head.prettify())
        #print(soup.h1.prettify())
        #print(minor_headings)

        create_file.write(soup.prettify())
        break

    except requests.RequestException:
        print("Error !")