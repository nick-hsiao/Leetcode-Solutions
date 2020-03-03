def allPathsSourceTarget(graph):
    res = []
    last = len(graph) - 1
    def dfs(path,current):
        if current == last:
            res.append(path)
            return
        else:
            for v in graph[current]:
                dfs(path + [v],v)
           
    dfs([0],0)
    return res
    
print(allPathsSourceTarget([[1,2],[3],[3],[]])) 