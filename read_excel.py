import numpy as np
import pandas as pd  
import re

filename= 'DSC_REG8b_alg.xlsx'
data_out_path = 'register.doc'
base_addr = 10240  #2800

# 读取Excel文件  
df = pd.read_excel(filename)  

# 将DataFrame转换为矩阵  
matrix = df.values  

# print(matrix)

[row, col] = np.shape(matrix)

i=0
j=0

addr_col = 1
name_col = 3
msb_col = 5
lsb_col = 6
start_row  = 7

i=start_row
j=addr_col

#分离字符串和int数据
def separate_chars_and_ints(s):  
    match = re.findall(r'(\d+)|[^\d\s]+', s)  
    return [int(i) if i.isdigit() else i for i in match] 
    # return [int(i) for i in match] 
     


with open(data_out_path, "w") as f:  
    while i<row :
        data_addr = matrix[i][addr_col]
        if pd.isna(data_addr): #空的行
            f.write("//" + '      ')
        else:
            f.write("\n\n\n")
            result = separate_chars_and_ints(data_addr)
            data_addr_result = result[1]
            data_addr_w = data_addr_result + base_addr
            f.write("//" + str(hex(data_addr_w).lstrip("0x").zfill(4).upper()) + '  ')
        f.write('[' + str(matrix[i][msb_col]) + ':' + str(matrix[i][lsb_col]) + ']  ' + matrix[i][name_col] + '\n')    
        # while j<lsb_col :
            # d = matrix[i][j]
            # d = str(d)
            # f.write(d + "   ")
            # j += 1
        # f.write("\n\n")
        # j = addr_col
        i += 1   
        print('i=', i)

