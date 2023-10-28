from ast import Str


def depth_first_search(key: str, graph: dict, qeue = []) -> None:
    if len(graph) == 0:
        return None
    else:
        friends = graph.get(key)
        print(f"{key} friends is: {friends}")
        for friend in friends:
            depth_first_search(friend, graph)

 
def breath_first_search(node: str, graph: dict) -> None:
    queue = []
    cache = []
    nodes = graph.get(node)
    queue += nodes
    while len(queue) > 0:
        node = queue.pop(0)
        queue += graph.get(node)
        if node not in cache:
            print(node)
            cache.append(node)




    
            




graph = {"you": ["Alice", "Bob", "Claire"], "Bob": ["Anuj", "Peggy"], "Alice": ["Peggy"], "Claire": ["Tom", "Johny"], "Anuj": [], "Peggy": [], "Tom": [], "Johny": []}


#depth_first_search(key = "you", graph = graph)
breath_first_search(node = "you", graph = graph)