from bs4 import BeautifulSoup
import requests


def main():
    source = requests.get("http://ruokalistat.net/").text
    soup = BeautifulSoup(source, 'lxml')
    title = soup.find("title").text

    message = [title]

    for element in soup.find_all("div", class_="inner"):
        message.append(element.text)

    return message




