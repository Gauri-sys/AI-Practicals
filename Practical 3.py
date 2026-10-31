import sys
import math

# ANSI Colors for visual terminal rendering
C_MAX = '\033[96m' # Cyan
C_MIN = '\033[94m' # Blue
C_LEAF = '\033[92m' # Green
C_PRUNE = '\033[91m' # Red
C_RESET = '\033[0m'

class TreeNode:
    def __init__(self, name, is_max, depth):
        self.name = name
        self.is_max = is_max
        self.depth = depth
        self.value = None
        self.children = []
        self.is_pruned = False
        self.prune_reason = ""

def get_tree_input():
    print(f"\n{C_MAX}--- Alpha-Beta Visualizer Setup ---{C_RESET}")
    try:
        depth = int(input("Enter the depth of the binary tree (e.g., 3): ").strip())
        if depth < 1: raise ValueError
    except ValueError:
        sys.exit("Error: Depth must be a positive integer.")

    expected_leaves = 2 ** depth
    try:
        leaves_input = input(f"Enter {expected_leaves} integers separated by spaces: ").strip().split()
        if len(leaves_input) != expected_leaves:
            sys.exit(f"Error: Expected {expected_leaves} values, got {len(leaves_input)}.")
        leaves = [int(val) for val in leaves_input]
    except ValueError:
        sys.exit("Error: All leaf values must be valid integers.")

    return depth, leaves

def build_tree(depth, leaves):
    def construct_node(current_depth, index, is_max):
        node = TreeNode(f"Node {index}", is_max, current_depth)

        if current_depth == 0:
            node.value = leaves[index]
            node.name = f"Leaf {index}"
            return node

        left_child = construct_node(current_depth - 1, index * 2, not is_max)
        right_child = construct_node(current_depth - 1, index * 2 + 1, not is_max)

        node.children.extend([left_child, right_child])
        return node

    return construct_node(depth, 0, True)

def alpha_beta_evaluate(node, alpha, beta):
    if node.depth == 0:
        return node.value

    if node.is_max:
        best_val = -math.inf
        for child in node.children:
            val = alpha_beta_evaluate(child, alpha, beta)
            best_val = max(best_val, val)
            alpha = max(alpha, best_val)

            if beta <= alpha:
                # Mark the remaining unvisited sibling as pruned
                sibling = node.children[1] if child == node.children[0] else None
                if sibling:
                    sibling.is_pruned = True
                    sibling.prune_reason = f"(α={alpha} >= β={beta})"
                break
        node.value = best_val
        return best_val

    else:
        best_val = math.inf
        for child in node.children:
            val = alpha_beta_evaluate(child, alpha, beta)
            best_val = min(best_val, val)
            beta = min(beta, best_val)

            if beta <= alpha:
                # Mark the remaining unvisited sibling as pruned
                sibling = node.children[1] if child == node.children[0] else None
                if sibling:
                    sibling.is_pruned = True
                    sibling.prune_reason = f"(α={alpha} >= β={beta})"
                break
        node.value = best_val
        return best_val

def render_visual_tree(node, prefix="", is_last=True, is_root=True):
    if is_root:
        print(f"\n{C_MAX}[MAX] ROOT{C_RESET} (Value: {node.value})")
    else:
        connector = "└── " if is_last else "├── "

        if node.is_pruned:
            print(f"{prefix}{connector}{C_PRUNE}✂️ PRUNED {node.name} {node.prune_reason}{C_RESET}")
            return # Stop drawing this branch

        if node.depth == 0:
            print(f"{prefix}{connector}{C_LEAF}🌿 {node.name}: {node.value}{C_RESET}")
        else:
            n_type = f"{C_MAX}[MAX]{C_RESET}" if node.is_max else f"{C_MIN}[MIN]{C_RESET}"
            print(f"{prefix}{connector}{n_type} {node.name} (Value: {node.value})")

    if not node.is_pruned and node.depth > 0:
        new_prefix = prefix + (" " if is_last else "│ ")
        child_count = len(node.children)
        for i, child in enumerate(node.children):
            render_visual_tree(child, new_prefix, i == (child_count - 1), False)

if __name__ == "__main__":
    tree_depth, leaf_scores = get_tree_input()

    root_node = build_tree(tree_depth, leaf_scores)
    optimal_score = alpha_beta_evaluate(root_node, -math.inf, math.inf)

    render_visual_tree(root_node)