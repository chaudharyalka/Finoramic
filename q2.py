class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        Mat = []
        #check Rows Validity:
        col_dict = [dict() for i in range(0,9)]
        mat_dict = [[dict() for i in range(0,3)] for j in range(0,3)]
        position_mat = []
        
        r_count = 0
        for r in A:
            d = dict()
            c = 0
            r_pos = r_count / 3
        
            for elem in r:
                #new_Row.append(elem)
                colDict = col_dict[c]
                c_pos = c / 3
                matDict = mat_dict[r_pos][c_pos]
            
                if (elem != '.' and elem in d):
                    #print (elem ,d ,"c1")
                    return (0)
                elif (elem != "." and elem in colDict):
                    #print (elem ,colDict , "c2")
                    return (0)
                elif (elem != "." and elem in matDict):
                    #print (elem , matDict , "c3",r_pos,c_pos)
                    return (0)
                else: 
                    d[elem] = 1
                    colDict[elem] = 1
                    matDict[elem] = 1
                
                c += 1
            r_count += 1
            #postion_mat.append(new_Row)
        return 1
                
                
                
        
        
            
        
