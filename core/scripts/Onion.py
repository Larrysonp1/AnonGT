from os import path
from requests import get
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from core.config.functions import is_started
from core.assets.alerts import ERROR, red, green


class ONION:

    def ahmia_engine(query):
        site = get(f"https://ahmia.fi/search/?q={query}")
        soup = BeautifulSoup(site.text, "html.parser")

        results = soup.find_all("li", class_="result")
        for result in results:
            title_tag = result.find("h4").find("a")
            title = title_tag.get_text(strip=True) if title_tag else "No Title"
            raw_href = title_tag.get("href") if title_tag else ""
            if "redirect_url=" in raw_href:
                link = raw_href.split("redirect_url=")[-1]
            else:
                link = urljoin(site, raw_href)

            onion_link = result.find("cite").get_text(strip=True) if result.find("cite") else "No URL"
            date_span = result.find("span", class_="lastSeen")
            last_seen = date_span.get("data-timestamp") if date_span else "No Date"

            print(f"{red("Title:")} {green(title)}")
            print(f"{red("URL:")} {green(link)}")
            print(f"{red("Link:")} {green(onion_link)}")
            print(f"{red("Last Seen:")} {green(last_seen)}")
            print(green("-") * 50)


    def check(self):
        # check if started
        if is_started() == 1:
            in_file = input(green("Submit the Directory File: "))
            if path.exists(in_file):
                input_file = open(in_file, 'r')

                for url in input_file:
                    url = url.rstrip('\n')
                    try:
                        data = get(url)
                    except:
                        data = 'error'
                    if data != 'error':
                        url = green(url)
                        status = green('Active')
                        status_code = green(data.status_code)
                        soup = BeautifulSoup(data.text, 'html.parser')
                        page_title = green(str(soup.title))
                        page_title = page_title.replace('<title>', '')
                        page_title = page_title.replace('</title>', '')
                    elif data == 'error':
                        url = red(url)
                        status = red("Inactive")
                        status_code = red('NA')
                        page_title = red('NA')
                    print(url, ': ', status, ': ', status_code, ': ', page_title)
            else:
                ERROR("File Not Exist.")
        else:
            ERROR("Please Start Anonymous Mode.")