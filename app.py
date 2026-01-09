from bs4 import BeautifulSoup
import requests

#todo
def website_cloning():
    return

#funcão que retorna conteudo de uma tag HTML como texto e a disponibiliza como um arquivo txt
def fetch_tag_contents(tags, param):
    tag_type = param.find_all(tags)
    create_txt = open("tag_contents.txt", "w")
    file_txt = ""

    #Loop que printa o texto da tag HTML e o adiciona a variavel file_txt
    if tags == "a":
        for href in tag_type:
            print(href.get("href"))
            file_txt += (href.get("href").replace("#", "") + "\n")
    else:
        for text in tag_type:
            print(text.get_text(strip=True))
            file_txt += (text.get_text(strip=True)+ "\n")

    file_option = input("Do you wish to write this to a file ? (y/n): ")
    if file_option == "y":
        create_txt.write(file_txt)
    elif file_option == 'n':
        return

while True:
    try:
        url_input = input("Insert URL here: ")
        create_file = open("test_file.html", "w")
        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(f"{url_input}", headers=headers)
        res_parsed = response.content
        soup = BeautifulSoup(res_parsed, 'html.parser')

        tag_input = input("Fetch specific HTML tag: ")
        fetch_tag_contents(tag_input, soup)

        #print(soup.head.prettify())
        #print(soup.h1.prettify())
        #print(minor_headings)

        create_file.write(soup.prettify())
        break

    except requests.RequestException:
        print("Error !")
        continue
