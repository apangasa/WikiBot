import getLinks
import listSearching
import time


def breadth_first_search(start_page, end_page):
    visited = []
    queue = []

    visited.append(start_page)
    queue.append(start_page)

    while queue:
        curr = queue.pop(0)
        print(curr)

        if curr == end_page:
            break

        links = getLinks.get_links_on_page(curr)

        if links is not None:
            for link in links:
                if link not in visited:
                    visited.append(link)
                    queue.append(link)


def breadth_first_search_modified(start_page, end_page):
    visited = []
    queue = []

    visited.append(start_page)
    queue.append(start_page)

    while queue:
        curr = queue.pop(0)
        print(curr)

        links = getLinks.get_links_on_page(curr)

        if links is not None:
            if listSearching.binary_search(links, 0, len(links) - 1, end_page) != -1:
                break

        if links is not None:
            for link in links:
                if link not in visited:
                    visited.append(link)
                    queue.append(link)


def depth_limited_search(start_page, end_page, levels):
    print(start_page)
    if start_page == end_page:
        return True
    elif levels == 0:
        return False
    else:
        links = getLinks.get_links_on_page(start_page)
        if links is not None:
            for link in links:
                result = depth_limited_search(link, end_page, levels - 1)
                if result:
                    return True
        else:
            return False


def iterative_deepening(start_page, end_page):
    pass


def bidirectional_bfs(start_page, end_page):
    pass

    
start_time = time.time()
# breadth_first_search_modified("Comethazine", "United States")
# depth_limited_search("Raavi Kondala Rao", "Raghnailt", 8)
end_time = time.time()
print(end_time - start_time)