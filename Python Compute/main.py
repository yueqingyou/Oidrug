import os
import pandas
from sklearn.preprocessing import MinMaxScaler


def normalized_matrix(matrix):
    scale = MinMaxScaler(copy=True, feature_range=(0, 1))
    scale.fit(matrix)
    norm_mat = scale.transform(matrix)

    return norm_mat


def get_id(filename, datatype, header=0):
    df = pandas.read_excel(filename, header=header)  # header设置为None
    data = df.values
    _id = []  # 待获取的id列表

    if datatype == str:
        for row in data:
            _str = ''.join(row)
            _id.append(_str)  # str化
    elif datatype == int:
        for row in data:
            _id.append(int(row))
    else:
        print('请输入数据类型！')

    return _id


def open_sourcefile(filename, header=0, low_memory=True):
    if 'tsv' in filename:
        with open(filename, 'r', encoding='utf-8') as tsv_file:
            tsv = pandas.read_csv(tsv_file, header=header, low_memory=low_memory, sep='\t')
            __data = tsv.values
        tsv_file.close()
    elif 'csv' in filename:
        with open(filename, 'r', encoding='utf-8') as csv_file:
            csv = pandas.read_csv(csv_file, header=header, low_memory=low_memory)
            __data = csv.values
        csv_file.close()
    else:
        print('请输入文件类型！')

    return __data


def square_matrix(id_data, sourcefile_data):
    __dict = {}
    for row in range(1, len(id_data)):
        for column in range(1, len(id_data)):
            __dict.update({id_data[row - 1] + '.' + id_data[column - 1]: sourcefile_data[row, column]})

    return __dict


def normal_matrix(id_data):
    __dict = {}
    for i in range(len(id_data)):
        __dict.update({id_data[i, 0] + '.' + id_data[i, 1]: str(id_data[i, 2])})

    return __dict


def square_output(id_name, dict_name, normalize=False):
    final = []

    for row in id_name:
        tmp = []
        for column in id_name:

            if dict_name.get(str(row) + '.' + str(column)):
                tmp.append(dict_name[str(row) + '.' + str(column)])
            else:
                tmp.append(0)

        final.append(tmp)

    for i in range(len(id_name)):
        for j in range(len(id_name)):

            if pandas.isnull(final[i][j]) or final[i][j] == 0:
                if i == j:
                    final[i][j] = 1
                else:
                    final[i][j] = 0

    if normalize:
        final = normalized_matrix(final)

    return final


def verification(dict_name, key, value):
    if dict_name.get(key) == str(value) or int(value):
        print('验证成功！')
    else:
        print('验证出错！')


def save_result(filename, matrix):
    path = 'result'
    folder = os.path.exists(path)

    if not folder:
        os.makedirs(path)

    with open('result/' + filename + '.csv', 'w') as f:
        save = pandas.DataFrame(matrix)
        save.to_csv(f, index=False, header=False)

    print('输出文件位于：', 'result/' + filename + '.csv')
