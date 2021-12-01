from main import *

# 获取待测id
omim_disease = get_id('csv/disease.xlsx', datatype=int, header=None)

tsv_data = open_sourcefile('csv/combined_similarity_triplet_2019.tsv', header=None)

omim_dict = {}  # 对应关系键值对
for i in range(len(tsv_data)):
    omim_dict.update({str(int(tsv_data[i, 0])) + '.' + str(int(tsv_data[i, 1])): tsv_data[i, 2]})

final = []
for row in omim_disease:
    tmp = []
    for column in omim_disease:
        if omim_dict.get(str(row) + '.' + str(column)):
            tmp.append(omim_dict[str(row) + '.' + str(column)])
        else:
            tmp.append('0')
    final.append(tmp)
print(final)

# 标准化
final = normalized_matrix(final)

# 保存输出文件
save_result('disease-result', final)
