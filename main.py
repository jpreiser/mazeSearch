# Graph representation of a maze and implementations of BFS and DFS.
from collections import deque


def bfs(graph, start, goal):
    print("Breadth-First Search")
    frontier = deque([start])
    visited = {start: None}
    while frontier:
        s = frontier.popleft()
        print(s, end=" ")
        if s == goal:
            break
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited[neighbor] = s
                frontier.append(neighbor)
    path = [goal]
    while visited[goal] is not None:
        path.insert(0, visited[goal])
        goal = visited[goal]
    print("\nPath:", path)


def dfs(graph, start, goal):
    print("\nDepth-First Search")
    frontier = [(start, [start])]
    while frontier:
        (s, path) = frontier.pop()
        print(s, end=" ")
        if s == goal:
            break
        for neighbor in graph[s]:
            if s == goal:
                path = path + [neighbor]
                break
            else:
                frontier.append((neighbor, path + [neighbor]))
    print("\nPath:", path)


if __name__ == '__main__':
    mazeGraph = {
        'Start': ['0'],
        '0': ['1', '2'],
        '1': [],
        '2': ['3', '4'],
        '3': [],
        '4': ['5', '8'],
        '5': ['6', '7'],
        '6': [],
        '7': [],
        '8': ['9', '10'],
        '9': [],
        '10': ['11', '12'],
        '11': ['13', '14'],
        '12': [],
        '13': [],
        '14': ['15', '16'],
        '15': [],
        '16': ['17', '18'],
        '17': ['Finish'],
        '18': ['19', '20'],
        '19': [],
        '20': ['21', '22'],
        '21': [],
        '22': ['23', '24'],
        '23': [],
        '24': [],
        'Finish': ['17']
    }
    bfs(mazeGraph, 'Start', 'Finish')
    dfs(mazeGraph, 'Start', 'Finish')

# Here are some websites I used beyond the book to either create the graphs
# or find the logic and syntax for the search functions.
# https://www.python.org/doc/essays/graphs
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph
# https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
# https://gist.github.com/wanderingstan/4b8ae84dd77eadf716b012f2a5e74790
# https://www.baeldung.com/cs/dfs-vs-bfs-vs-dijkstra
