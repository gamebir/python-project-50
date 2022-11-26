import json


def generate_diff(file1, file2):
    file1 = json.load(open(file1))
    file2 = json.load(open(file2))
    all_keys = list(set(file1) | set(file2))
    all_keys.sort()
    result = ''
    for key in all_keys:

        if key in file1 and key in file2:

            if file1[key] != file2[key]:
                result += f'- {key}: {file1[key]}\n+ {key}: {file2[key]}\n'
            else:
                result += f'  {key}: {file1[key]}\n'

        elif key in file1 and key not in file2:
            result += f'- {key}: {file1[key]}\n'

        else:
            result += f'- {key}: {file2[key]}\n'

    return result
