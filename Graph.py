from QueueClass import Queue


class GraphNode:
    def __init__(self, data):
        self.data = data
        self.children = []


class Graph:
    def __init__(self):
        self.nodes = []

    def dfs(self):
        result = []
        self.visited = set()
        for node in self.nodes:
            if node not in self.visited:
                result += self._dfs(node)
        return result

    def _dfs(self, current_node):
        result = [current_node.data]
        self.visited.add(current_node)
        for child in current_node.children:
            if child not in self.visited:
                result += self._dfs(child)
        return result

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



