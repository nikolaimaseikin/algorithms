import math


def dijkstra_search(start_node: str, graph: dict) -> dict:
    if start_node not in graph:
        raise KeyError(f"Node: \"{start_node}\" not in this graph")
    path_weights = {}
    for key in graph.keys():
        if key == start_node:
            path_weights[key] = 0
        else:
            path_weights[key] = math.inf
    nodes_queue = [start_node]
    nodes_cache = []
    while len(nodes_queue) > 0:
        current_node_name = nodes_queue.pop(0)
        current_node_values = graph.get(current_node_name)
        #print(f'{current_node_name}, {current_node_values}')
        #Обновление значений кратчайших путей до нод 
        for node, weight in current_node_values.items(): 
            if path_weights[current_node_name] + weight < path_weights[node] and node not in nodes_cache: 
                path_weights[node] = path_weights[current_node_name] + weight
        #Кэширование пройденных нод
        nodes_cache.append(current_node_name) 
        #Добавление в очередь ноды с кратчайшим путём до неё
        min_path_weight_value = math.inf 
        append_queue_node_candidate = None 
        for node, weight in path_weights.items():
            if weight < min_path_weight_value and node not in nodes_cache:
                min_path_weight_value = weight
                append_queue_node_candidate = node
        if append_queue_node_candidate:
            nodes_queue.append(append_queue_node_candidate)
    return path_weights
        

test_graph = {
'node_1': {'node_2': 3, 'node_3': 1, 'node_4': 3},
'node_2':{'node_1': 3, 'node_3': 4},
'node_3':{'node_1': 1, 'node_2': 4, 'node_5': 7, 'node_6': 5},
'node_4':{'node_1': 3,'node_6': 2},
'node_5':{'node_3': 7, 'node_6': 4},
'node_6':{'node_3': 5, 'node_4': 2, 'node_6': 5}
}
print(dijkstra_search('node_4', test_graph))