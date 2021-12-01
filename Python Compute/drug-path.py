from main import *

drug_id = get_id('csv/drug2.xlsx', datatype=str, header=None)  # 待获取的id列表

csv_data = open_sourcefile('csv/path_similarity_v2.csv', header=None, low_memory=False)

dict_id = []
for _id in range(1, len(csv_data[0])):
    dict_id.append(csv_data[0, _id])

chem_dict = square_matrix(dict_id, sourcefile_data=csv_data)

verification(chem_dict, 'DB00014.DB00091', 0.314363143631436)

final = square_output(drug_id, chem_dict)

save_result('path_drug', matrix=final)
