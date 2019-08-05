def floyd_dict(graph):
    length = len(graph)
    path = {}

    for src in graph:
        path.setdefault(src,{})
        for dst in graph[src]:
            if src == dst:
                continue
            path[src].setdefault(dst,[src,dst])
            new_node = None

            for mid in graph:
                if mid == dst:
                    continue
                new_len = graph[src][mid] + graph[mid][dst]
                if graph[src][dst] > new_len:
                    graph[src][dst] = new_len
            if new_node:
                path[src][dst].insert(-1,new_node)

    return graph,path

if __name__ == '__main__':
    graph_dict = {"s1": {"s1": 0, "s2": 2, "s10": 1, "s12": 4},
                  "s2": {"s1": 1, "s2": 0, "s10": 4, "s12": 2},
                  "s10": {"s1": 2, "s2": 1, "s10": 0, "s12": 1},
                  "s12": {"s1": 3, "s2": 5, "s10": 2, "s12": 0},
                  }

    new_graph, path= floyd_dict(graph_dict)
    print (new_graph,'\n', path)