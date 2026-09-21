from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


headers = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36"
    )
}


def fetch_website_contents(url):
    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.title.string.strip() if soup.title else "No title found"

    if soup.body:
        for irrelevant in soup.body(
            ["script", "style", "img", "input"]
        ):
            irrelevant.decompose()

        text = soup.body.get_text(
            separator="\n",
            strip=True
        )
    else:
        text = ""

    return title + "\n\n" + text


def fetch_website_links(url):
    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    links = []

    for link in soup.find_all("a"):
        href = link.get("href")

        if href:
            absolute_url = urljoin(url, href)
            links.append(absolute_url)

    return links