from main import *

drug_id = get_id('csv/drug2.xlsx', datatype=str, header=None)  # 待获取的id列表

csv_data = open_sourcefile('csv/GO_Sim_BP_combined.csv', header=None, low_memory=False)

dict_id = []
for _id in range(1, len(csv_data[0])):
    dict_id.append(csv_data[0, _id])
print(dict_id)

chem_dict = square_matrix(dict_id, sourcefile_data=csv_data)

verification(chem_dict, 'DB00050.DB00035', 0.39)

final = square_output(drug_id, chem_dict)

save_result('go_drug', matrix=final)
