graph = {
    "1":["2","3"],
    "2":["4", "5"],
    "3":[],
    "4":["6"],
    "5":["7"],
    "6":[],
    "7":[],
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '1')
