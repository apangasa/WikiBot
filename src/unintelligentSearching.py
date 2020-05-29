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
    front_visited = []
    back_visited = []

    front_queue = []
    back_queue = []

    front_queue.append(start_page)
    back_queue.append(end_page)

    while front_queue or back_queue:
        curr = front_queue.pop(0)
        print("F " + curr)

        links = getLinks.get_links_on_page(curr)

        if bidirectional_bfs_helper(links, front_queue, front_visited, back_visited, end_page, "F"):
            break

        curr = back_queue.pop(0)
        print("B " + curr)

        backlinks = getLinks.get_links_to_page(curr)

        if bidirectional_bfs_helper(backlinks, back_queue, back_visited, front_visited, start_page, "B"):
            break

    pass


def bidirectional_bfs_helper(links, queue, this_visited, that_visited, goal, p):
    if links is not None:
        if p == "F":
            if listSearching.binary_search(links, 0, len(links) - 1, goal) != -1:
                return True
        else:
            if goal in links:
                return True
        for visited_link in that_visited:
            if visited_link != goal:
                if p == "F": # forward search
                    if listSearching.binary_search(links, 0, len(links) - 1, visited_link) != -1:
                        print(p + " " + visited_link)
                        return True
                else:
                    if visited_link in links:
                        print(p + " " + visited_link)
                        return True
        for link in links:
            if link not in this_visited:
                queue.append(link)
                this_visited.append(link)


start_time = time.time()
# breadth_first_search_modified("Comethazine", "United States")
# depth_limited_search("Raavi Kondala Rao", "Raghnailt", 8)
# bidirectional_bfs("Jean-Claude Bouillaud", "Raavi Kondala Rao")
end_time = time.time()
print(end_time - start_time)
