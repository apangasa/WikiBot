import wikipedia
import requests
import time

BASE_URL = "https://en.wikipedia.org/w/api.php/w/api.php?action=query&format=json&list=backlinks&bltitle="
CONTINUE = "&blcontinue="
MAX_RES = "&bllimit=max"
FORMATTING = "&formatversion=2"


def get_links_on_page(start_page):
    try:
        links = []
        for link in wikipedia.page(start_page).links:
            if link is not None:
                links.append(link)
        return links
    except:
        return None


def get_links_to_page(end_page):
    full_results = []
    more_results_available = True
    first_run = True
    continue_code = ""
    #j=0
    while more_results_available:
        call = BASE_URL + end_page + MAX_RES + FORMATTING

        if not first_run:
            call += CONTINUE + continue_code

        r = requests.get(call)
        data = r.json()

        if data.get("continue"):
            continue_code = data["continue"]["blcontinue"]
        else:
            more_results_available = False

        results = data["query"]["backlinks"]

        for i in range(len(results)):
            full_results.append(results[i]["title"])

        first_run = False
        #j += 500
        #print(j)
    return full_results


start = time.time()
# print(get_links_to_page("Raghnailt"))
# print(len(get_links_to_page("Raghnailt")))
end = time.time()

print(end - start)
