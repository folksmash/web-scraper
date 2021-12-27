from bs4 import BeautifulSoup
import requests

def get_citations_needed_count():
    url = "https://en.wikipedia.org/wiki/Template:Citation_needed"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(title="Wikipedia:Citation needed")
    count = 0


    for _ in results:
        count +=1


    print(count)
    return count

def get_citations_needed_report():
    url = "https://en.wikipedia.org/wiki/Template:Citation_needed"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(title="Wikipedia:Citation needed")
    string = ""


    for result in results:
        string += f"{result.parent.parent.parent.text}\n"

    print(string)
    return string




get_citations_needed_count()
get_citations_needed_report()