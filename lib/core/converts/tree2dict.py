import os
import sys
sys.path.append(os.getcwd())
from lib.datastruc.tree import Tree as TreeNode

# Function to convert a tree node and its children to a dictionary
def tree_to_dict(node:TreeNode):
    """
    >>> root = TreeNode('A')
    >>> node_b = TreeNode('B')
    >>> node_c = TreeNode('C')
    >>> node_d = TreeNode('D')
    >>> node_e = TreeNode('E')

    >>> root.children.append(node_b)
    >>> root.children.append(node_c)
    >>> node_b.children.append(node_d)
    >>> node_b.children.append(node_e)

    # Convert Tree to Dictionary
    >>> tree_dict = tree_to_dict(root)
    >>> print(tree_dict)
    """

    if node is None:
        return
    result = {
        'value': node.data,
        'children': []
    }
    for child in node.children:
        result['children'].append(tree_to_dict(child))
    return result

# Crafted Tree
