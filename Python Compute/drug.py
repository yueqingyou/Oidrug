from main import *

drug_id = get_id('csv/cell.xlsx', datatype=str, header=None)  # 待获取的id列表

csv_data = open_sourcefile('csv/DrugSimDB_v1_0_0.csv')

drug_dict = square_matrix(csv_data)

if drug_dict['DB00014.DB00035']:
    print(drug_dict['DB00014.DB00035'])
else:
    print('ERROR')

final = square_output(drug_id, drug_dict, normalize=True)

save_result('drug-result-all', matrix=final)
