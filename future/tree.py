"""
# SQLGO License - Version 1.1

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
class Tree:
    """
    Usage

>>> root = Tree("electronic")

>>> laptop = Tree("laptop")
>>> laptop.add_child(Tree("mac"))
>>> laptop.add_child(Tree("windows"))
>>> root.add_child(laptop)

>>> cellphone = Tree("cellphone")
>>> cellphone.add_child(Tree("iphone"))
>>> cellphone.add_child(Tree("samsung"))
>>> root.add_child(cellphone)

>>> tv = Tree("tv")
>>> tv.add_child(Tree("samsung"))
>>> tv.add_child(Tree("LG"))
>>> root.add_child(tv)

>>> root.print_tree()
    """
    def __init__(self,data) -> None:
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
    def print_child(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.print_child()
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        spaces = '' * self.get_level() *3
        prefix = spaces + "__|" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

