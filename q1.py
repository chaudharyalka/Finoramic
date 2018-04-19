# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        allPaths = (self.getPaths(A,B))
        return (map(lambda x: x.split(",") , allPaths))
    
    def getPaths(self,root,S):
        if (root != None):
            rootValue = root.val
            if (rootValue == S and (root.left == None) and (root.right == None)):
                        return [str(rootValue)]
            elif (rootValue != S and (root.left == None and root.right == None )):
                        return []
            else: # (rootValue < S):
                        getRemaining_1 = self.getPaths(root.left,S - rootValue)
                        getRemaining_2 = self.getPaths(root.right,S - rootValue)
                        finalList = getRemaining_1 + getRemaining_2
                        return (map(lambda x : str(rootValue) + "," + x   , finalList))
            
        else:
            return []
            
                
                
                
                
                
                
