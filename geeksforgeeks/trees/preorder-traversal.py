'''
https://practice.geeksforgeeks.org/problems/preorder-traversal/1/

Given a binary tree, print preorder traversal of it. For example, preorder traversal of below tree is "1 10 5 39"

        1
     /     \
   10     39
  /
5

Input:
The task is to complete the method which takes one argument, root of Binary Tree. The struct Node has a data part which stores the data, pointer to left child and pointer to right child.
There are multiple test cases. For each test case, this method will be called individually.

Output:
The function should print preorder traversal.

Constraints:
1 <=T<= 30
1 <=Number of nodes<= 100
1 <=Data of a node<= 1000

Example:
Input:
2
2
1 2 R 1 3 L
4
10 20 L 10 30 R 20 40 L 20 60 R

Output:
1 3 2
10 20 40 60 30

There are two test casess.  First case represents a tree with 3 nodes and 2 edges where root is 1, left child of 1 is 3 and right child of 1 is 2.   Second test case represents a tree with 4 edges and 5 nodes.
'''
class GfG:
    def preorder_traversal_gen(self, node):
        if node is not None:
            yield node.data
            for node_data in self.preorder_traversal_gen(node.left):
                yield node_data
            for node_data in self.preorder_traversal_gen(node.right):
                yield node_data
    
    def preorder(self, node):
        gen = self.preorder_traversal_gen(node)
        for node_data in gen:
            print(node_data, end=' ')
