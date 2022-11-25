import json


def get_matching_keys(file1, file2):
    return set(sorted(file1)) & set(sorted(file2))


def get_matching_keys_matching_values(file1, file2):
    matching_keys = get_matching_keys(file1, file2)
    return [key for key in matching_keys if file1[key] == file2[key]]


def get_matching_keys_not_matching_values(file1, file2):
    matching_keys = get_matching_keys(file1, file2)
    return [key for key in matching_keys if file1[key] != file2[key]]


def get_not_matching_keys(file1, file2):
    keys_f1 = sorted(file1)
    keys_f2 = sorted(file2)
    return list(set(keys_f1) - set(keys_f2)) + list(set(keys_f2) - set(keys_f1))


def generate_diff(file1, file2):
    file1 = json.load(open('file1.json'))
    file2 = json.load(open('file2.json'))
    combined_list = list(set(sorted(file1) + sorted(file2)))
    combined_list.sort()
    for key in combined_list:

        if key in get_matching_keys_matching_values(file1, file2):
            print(f'  {key}: {file1[key]}')
        if key in get_matching_keys_not_matching_values(file1, file2):
            print(f'- {key}: {file1[key]}\n+ {key}: {file2[key]} ')
        if key in get_not_matching_keys(file1, file2):

            if key in file1:
                print(f'- {key}: {file1.get(key)}')
            else:
                print(f'+ {key}: {file2.get(key)}')
