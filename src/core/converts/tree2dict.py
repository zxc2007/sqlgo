#!/usr/bin/env python
"""
# SQLGO License - Version 1.4

Copyright (C) 2023-2024 Heisenberg

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""
import os
import sys
from src.datastruc.tree import Tree as TreeNode

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

