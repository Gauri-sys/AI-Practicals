class MenuDFS:
    def __init__(self):
        self.graph = {}

    def build_user_graph(self):
        self.graph.clear()
        num_edges = int(input("Enter total number of edges: "))
        print("Enter edges format (Source Target):")
        for _ in range(num_edges):
            u, v = input().split()
            if u not in self.graph:
                self.graph[u] = []
            if v not in self.graph:
                self.graph[v] = []
            self.graph[u].append(v)

    def run_dfs_with_transitions(self, start_node, goal_node=None):
        stack = [start_node]
        visited = []
        parent_map = {start_node: None}
        step = 1

        print("\n" + "="*70)
        print("DFS STEP-BY-STEP STATE TRANSITION TRACE")
        print("="*70)

        while stack:
            current = stack.pop()

            if current not in visited:
                visited.append(current)
                action = f"VISITED node {current}"

                if current == goal_node:
                    print(f"Step {step} | Node: {current} | Action: GOAL REACHED | Stack: {stack} | Visited: {visited}")

                    # Path Reconstruction
                    path = []
                    curr = goal_node
                    while curr is not None:
                        path.append(curr)
                        curr = parent_map[curr]
                    return path[::-1]

                # Push neighbors in reverse order to preserve left-to-right order
                neighbors = self.graph.get(current, [])
                for neighbor in reversed(neighbors):
                    if neighbor not in visited:
                        stack.append(neighbor)
                        if neighbor not in parent_map:
                            parent_map[neighbor] = current

                print(f"Step {step} | Node: {current} | Action: {action} | Stack: {stack} | Visited: {visited}")
                step += 1
            else:
                print(f"Step {step} | Node: {current} | Action: BACKTRACK (Already visited) | Stack: {stack} | Visited: {visited}")
                step += 1

        return visited


if __name__ == "__main__":
    dfs_system = MenuDFS()
    dfs_system.graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': []}
    path = dfs_system.run_dfs_with_transitions('A', 'F')
    print("Discovered Path:", path)