from QueueClass import Queue


class GraphNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.child_weights = []

class Graph:
    def __init__(self):
        self.nodes = []

    def dfs(self):
        result = []
        self.time = 0
        self.visited = set()
        for node in self.nodes:
            if node not in self.visited:
                result += self._dfs(node)
        node_dict_list = self._create_list_of_node_dict(result)
        return node_dict_list

    def _dfs(self, current_node):
        self.time += 1
        result = [current_node]
        self.visited.add(current_node)
        current_node.discovery_time = self.time
        for child in current_node.children:
            if child not in self.visited:
                result += self._dfs(child)
        self.time += 1
        current_node.finishing_time = self.time
        return result

    def _create_list_of_node_dict(self, node_list):
        output = []
        for node in node_list:
            node_dict = {"data": node.data}
            if hasattr(node, 'discovery_time'):
                node_dict["d"] = node.discovery_time
            if hasattr(node, 'finishing_time'):
                node_dict["f"] = node.finishing_time
            output.append(node_dict)
        return output

    def bfs(self):
        result = []
        self.visited = set()
        for node in self.nodes:
            if node not in self.visited:
                result += self._bfs(node)
        return result

    def _bfs(self, start_node):
        result = []
        queue = Queue()
        queue.add(start_node)
        self.visited.add(start_node)
        while not queue.is_empty():
            output_node = queue.remove()
            for child in output_node.children:
                if child not in self.visited:
                    queue.add(child)
                    self.visited.add(child)
            result += [output_node.data]
        return result

    def bi_directional_search(self, src, dst):
        self._add_inverted_children()
        self.reset_node_paths()
        queue_src = Queue()
        queue_dst = Queue()
        src_visited = set()
        dst_visited = set()
        queue_src.add(src)
        src_visited.add(src)
        queue_dst.add(dst)
        dst_visited.add(dst)
        collided = False
        while not queue_src.is_empty() or not queue_dst.is_empty():
            if len(src_visited.intersection(dst_visited)) > 0:
                collided = True
                break
            if not queue_src.is_empty():
                src_output = queue_src.remove()
                for child in src_output.children:
                    if child not in src_visited:
                        child.forward_pre = src_output
                        queue_src.add(child)
                        src_visited.add(child)

            if len(src_visited.intersection(dst_visited)) > 0:
                collided = True
                break
            if not queue_dst.is_empty():
                dst_output = queue_dst.remove()
                if dst_output in self.inverted:
                    for child in self.inverted[dst_output]:
                        if child not in dst_visited:
                            child.backward_pre = dst_output
                            queue_dst.add(child)
                            dst_visited.add(child)
        if collided:
            intersect = src_visited.intersection(dst_visited).pop()
            forward = []
            ref = intersect
            while ref is not None:
                forward = [ref.data] + forward
                ref = ref.forward_pre
            ref = intersect
            backward = []
            while ref is not None:
                backward += [ref.data]
                ref = ref.backward_pre
            return forward[:-1] + backward
        else:
            return []

    def _add_inverted_children(self):
        self.inverted = {}
        for node in self.nodes:
            for child in node.children:
                if child not in self.inverted:
                    self.inverted[child] = [node]
                elif node not in self.inverted[child]:
                    self.inverted[child] += [node]

    def reset_node_paths(self):
        for node in self.nodes:
            node.forward_pre = None
            node.backward_pre = None

    def topological_sort(self):
        self.visited = set()
        self.sorted_list=[]
        for node in self.nodes:
            if node not in self.visited:
                self.topological_dfs(node)
        return self.sorted_list

    def topological_dfs(self, node):
        for child in node.children:
            if child not in self.visited:
                self.visited.add(child)
                self.topological_dfs(child)
        self.sorted_list.insert(0, node.data)

    def shortest_path(self, src_idx):
        #shortest paths based on Dijkstra algorithm

        #initialize parents, path_weights so far and remaining nodes priority queue
        path_weights = []
        for i in range(len(self.nodes)):
            if i == src_idx:
                path_weights.append(0)
            else:
                path_weights.append(float("inf"))

        parent_indexes = []
        for i in range(len(self.nodes)):
            if i == src_idx:
                parent_indexes.append(-1)
            else:
                parent_indexes.append(None)

        priority_queue_arr = []
        for i in range(len(self.nodes)):
            if i == src_idx:
                priority_queue_arr.append(0)
            else:
                priority_queue_arr.append(float("inf"))


        #start from the source and then update the weights so far for each node that we get to
        while (min(priority_queue_arr) < float("inf")):
            min_weight_node_idx = priority_queue_arr.index(min(priority_queue_arr))
            priority_queue_arr[min_weight_node_idx] = float("inf")


            #traverse on each of the neighbours of the min_weight_node and update weights and parents
            for i in range(len(self.nodes[min_weight_node_idx].children)):
                edge_weight = self.nodes[min_weight_node_idx].child_weights[i]
                neighbor_idx = self.nodes.index(self.nodes[min_weight_node_idx].children[i])
                neighbor_path_weight = path_weights[neighbor_idx]

                new_weight = path_weights[min_weight_node_idx] + edge_weight

                if new_weight < neighbor_path_weight:
                    parent_indexes[neighbor_idx] = min_weight_node_idx
                    path_weights[neighbor_idx] = new_weight
                    priority_queue_arr[neighbor_idx] = new_weight

        return parent_indexes



