# The program defines a mango seller using some weird signs and BFS.

from _collections import deque


def person_is_seller(person):
    if len(person) == 5 and person[0] == 'M':
        return True
    else:
        return False


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person, 'is a mango seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


graph = {
    'you': ['Ross', 'Peter', 'May'],
    'Ross': ['Peter', 'Monica'],
    'Peter': ['Ross'],
    'May': [],
    'Monica': ['Margo']
}

search('you')
