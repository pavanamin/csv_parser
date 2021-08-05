"""
Created on 3/8/2021 

@author: Pavan Amin
"""
import csv


def csv_dict(file, label):
    column_list = []
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        for i in reader:  # each row is in the form {k1 : v1, ... kn : vn}
            for k, v in i.items():
                if k == label:
                    column_list.append(v)
    return column_list


def get_unique_ids(dup_list):
    tmp_list = list(set(dup_list))
    tmp_list1 = []
    for i in tmp_list:
        if i != '':
            tmp_list1.append(i[i.rfind("=")+1:])
    return tmp_list1


file_name = 'example.csv'
column_label = 'Serial'
column_list = csv_dict(file_name, column_label)
sn_list = get_unique_ids(column_list)
print(sn_list)
