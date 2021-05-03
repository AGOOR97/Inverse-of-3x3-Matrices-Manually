#Question No. 2
print("================================ Coded By Mohammed AGooR ===================================")
print("")


matA = [[1,1,1],[0,2,5],[2,5,-1]]

def det2x2(mat1):
    '''this function calculates the 2x2 matrix detrminant'''
    assert (len(mat1) == 2 and len(mat1[0]) == 2) ,"it should be 2x2 Matrix"
    det2x2 = (mat1[0][0] * mat1[1][1]) - (mat1[0][1] * mat1[1][0])
   
    return det2x2


def get2x2(mat2,row,col):
    '''this function returns the sub 2x2 matrix of the big matrix 3x3'''
    mat2x2 = []    
    for i in range(len(mat2)):
        matRow = [] 
        for j in range(len(mat2[0])):
            if i!=row and j!=col:
                matRow.append(mat2[i][j])            
        if matRow:
            mat2x2.append(matRow)
            
    return mat2x2


def calDet(mat3):
    '''this function calculates the final Determinant of 3x3 Matrix'''
    come0 = get2x2(mat3,0,0)
    come1 = get2x2(mat3,0,1)
    come2 = get2x2(mat3,0,2)

    det0 = det2x2(come0) * mat3[0][0]
    det1 = det2x2(come1) * mat3[0][1]
    det2 = det2x2(come2) * mat3[0][2]

    det = det0 - det1 + det2
    
    if det == 0 :
        return 'this Matrix is non-Invertible has no Inverse , Determinant = 0 , Singular Matrix'

    return det

# we want to generate the method of cofactors

def cofactor(mat4):
    '''this function returns the cofactor matrix 3x3'''
    matSigns = [[1,-1,1],[-1,1,-1],[1,-1,1]]

    matCofact = []
    for i in range(len(mat4)):
        matChild = []
        for j in range(len(mat4[0])):
            comeNum = get2x2(mat4,i,j)
            get_det2x2 = det2x2(comeNum) 
            each_num =  get_det2x2 * matSigns[i][j]
            matChild.append(each_num)
        if matChild:
            matCofact.append(matChild)
    
    
    return matCofact


# we want to get Transpose of cofactor Matrix

def cofactTranspose(mat5):
    '''this function is to transpose the cofactor Matrix'''
    matTrans = []
    matCofactor = cofactor(mat5)
    for i in range(len(mat5)):
        matChildTrans = []
        for j in range(len(mat5[0])):
            value_Trans = matCofactor[j][i]
            matChildTrans.append(value_Trans)
        if matChildTrans:
            matTrans.append(matChildTrans)
            
    return matTrans


pre_final_mat = cofactTranspose(matA)   # pre final matrix , we almost done 


# we now finally to divide the Transposed Cofacroer Matrix by Determinant

def lastCal(mat6):
    '''this function is the last function , divide the Transposed Cofactor Matrix by Deteminant'''
    matFinal = []
    
    for i in range(len(mat6)):
        matChildFinal = []
        for j in range(len(mat6[0])):
            final_value = pre_final_mat[i][j] / calDet(mat6)
            matChildFinal.append(final_value)
        if matChildFinal:
            matFinal.append(matChildFinal)
    return matFinal


print("Here we are ,... the Final Result of the Inverse of Matrix matA ..... ")
print("")

print(lastCal(matA))

print("")
print("================================ Coded By Mohammed AGooR ===================================")
