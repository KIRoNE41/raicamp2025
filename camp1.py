# txt = rai
# print(txt)

#fruits = ["apple","banana"]
#fruits.append("orage")
#fruits.remove("apple")
#fruits.insert(1,"melon")
#for fruit in fruits:
#    print(f"This is a {fruit}.")










##########Dictionary in Mobile Robot
#       A
#      / \
#     B   C
#    / \    \
#   D  E     F

graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

start = 'A'
goal = 'C'
frontier = [start]
explored = set() #Use a set for unique (ignore duplicate append)

while len(frontier) > 0:
    current = frontier.pop()
    print(current)

    if current == goal:
        print("Goal reach")
        break

    for neighbor in graph[current]:
        frontier.append(neighbor)
