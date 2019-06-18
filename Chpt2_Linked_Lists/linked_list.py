#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 17:45:32 2019

@author: rushit
"""

class ListNode:
    
    def __init__(self, data):
        "Constructor"
        self.data = data
        self.next = None
        return
    
    def hasValue(self, value):
        "Method to compare value with node data"
        if self.data == value:
            return True
        else:
            return False
        
class SingleLinkedList:
    
    def __init__(self):
        "Constructor"
        self.head = None
        self.tail = None
        return
    
    def add_list_item(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)
            
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        
        self.tail = item
        return
    
    def list_length(self):
        
        count = 0
        current_node = self.head
        
        while current_node.next is not None:
            current_node = current_node.next
            count += 1
        return count
    
    def output_list(self):
        current_node = self.head
        
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
            
        return
    
    def unordered_search (self, value):
        "search the linked list for the node that has this value"

        # define current_node
        current_node = self.head

        # define position
        node_id = 1

        # define list of results
        results = []

        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)

            # jump to the linked node
            current_node = current_node.next
            node_id = node_id + 1

        return results
    
    def remove_list_item_by_id(self, item_id):
        "remove the list item with the item id"

        current_id = 1
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_id == item_id:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    # we don't have to look any further
                    return

            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next
            current_id = current_id + 1

        return
    
    def detect_intersection(self, list2):
        
        l1_head = self.head
        l2_head = l2.head
        
        current_node_l1 = self.head
        current_node_l2 = l2.head
        
        len1 = self.list_length()
        len2 = l2.list_length()
#        
#        if len1 == len2:
#            while (current_node_l1 is not None) and (current_node_l2 is not None):
#                current_node_l1 = current_node_l1.next
#                current_node_l2 = current_node_l2.next
#                
#                if current_node_l1==current_node_l2:
#                    return current_node_l1
                
        if len1 >= len2:
            diff = len1 - len2
            for _ in range(diff):
                l1_head = l1_head.next
            
            while (l1_head is not None):
                if l1_head == l2_head:
                    return l1_head
                else:
                    l1_head = l1_head.next
                    l2_head = l2_head.next
                    
        else:
            diff = len2 - len1
            for _ in range(diff):
                l2_head = l2_head.next
            
            while (l1_head is not None):
                if l1_head == l2_head:
                    return l1_head
                else:
                    l1_head = l1_head.next
                    l2_head = l2_head.next
                    
        return None

node0 = ListNode(0)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
#
#l1 = SingleLinkedList()
#for item in [node0, node1, node2, node3, node4, node5]:
#    l1.add_list_item(item)
#    
#l2 = SingleLinkedList()
#for item in [node5, node6]:
#    l2.add_list_item(item)
    
l1 = SingleLinkedList()
for item in [node0]:
    l1.add_list_item(item)
    
l2 = SingleLinkedList()
for item in [node1]:
    l2.add_list_item(item)
    
