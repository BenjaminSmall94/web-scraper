import requests
from bs4 import BeautifulSoup


def get_soup_results(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup.find_all(title="Wikipedia:Citation needed")


def get_citations_needed_count(url):
    return len(get_soup_results(url))


def get_citations_needed_report(url):
    soup_results = get_soup_results(url)
    report_string = ""
    for element in soup_results:
        report_string += element.parent.parent.parent.text + "\n"
    return report_string


if __name__ == "__main__":
    print(get_citations_needed_count("https://en.wikipedia.org/wiki/Inca_Empire"))
    print(get_citations_needed_report("https://en.wikipedia.org/wiki/Inca_Empire"))