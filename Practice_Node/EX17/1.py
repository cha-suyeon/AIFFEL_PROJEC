def print_json_tree(data, indent=""):
    for key, value in data.items():
        if type(value) == list: # list 형태의 item은 첫 번째 item만 출력
            print(f'{indent}-{key}: [{len(value)}]')
            print_json_tree(value[0], indent+" ")
        else:
            print(f'{indent}-{key}:{value}')
            