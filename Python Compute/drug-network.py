from main import *

drug_id = get_id('csv/cell.xlsx', header=None, datatype=str)  # 待获取的id列表

csv_data = open_sourcefile('../csv/DrugSimDB_v1_0_0_NetworkOnly.csv')

chem_dict = square_matrix(csv_data)

# 验证代码
if chem_dict.get('DB00006.DB00170'):
    print(chem_dict['DB00006.DB00170'], 0.509140611778712)
else:
    print('ERROR')

final = square_output(drug_id, chem_dict)

save_result('net-drug', matrix=final)
