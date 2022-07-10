#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 13:09:10 2022

@author: jpburns
"""

# Implement a linked list without using lists (i.e. unordered data structures)
# Constraints: data must be the same type, and that type must be comparable

#TODO tidy up this code a little.


class Node():
    
    # initialize with data, pointer to next, and whether it is the head node
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        self.is_head = False
        
        
    # for pretty-printing
    def __repr__(self):
        out = ""
        if self.is_head:
            out += "<HEAD> "
        out += self.data
        if self.next_node:
            out += " --> " + self.next_node.data
        else:
            out += " <END>"
        return out
    
    
    # change pointer to another node
    def set_next(self, next_node):
        self.next_node = next_node
        
        
def Insert(linked_list, new_node):
    
    # insert new node at the correct position
    
    for n in linked_list:
        # does the new element goes first?
        if new_node.data <= n.data and n.is_head:
            new_node.next_node = n
            new_node.is_head = True
            n.is_head = False
            break
        
        # or does it get appended at the end?
        elif new_node.data >= n.data and not n.next_node:
            n.next_node = new_node
            break
        
        # otherwise, it must go somewhere in the middle
        elif n.data <= new_node.data <= n.next_node.data:
            new_node.next_node = n.next_node
            n.next_node = new_node
            break
        else:
            continue

    linked_list.add(new_node)


#
# 1: turning a vanilla list into a linked list represented as a set of nodes.
#

people = ['Bender', 'Fry', 'Calculon', 'Dwight', 'Amy', 'Elzar']
people.sort()
ll = set()

for i in range(0, len(people)):
    try:
        new_node = Node(people[i], Node(people[i+1]))
    except IndexError:
        new_node = Node(people[i])
    if i==0:
        new_node.is_head = True
    ll.add(new_node)
    
#
# 2: Insertion of new elements
#

newpeople = ['Donbot', 'Professor Farnsworth', 'Alcazar', 'Mom', 'Nibbler', 'Flexo', 'Zapp Branigan']

for p in newpeople:
    Insert(ll, Node(p))

for n in ll:
    if n.is_head:
        current_node = n

breakpoint()
while current_node.next_node:
    print(current_node)
    current_node = current_node.next_node