import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file) -> list[dict]:
    with open(file) as f:
        list1 = f.readline()[:-1].split(sep=",")
        list2 = [i[:-1].split(sep=",") for i in f.readlines()]
        list_ = [{list1[_]:list2[i][_] for _ in range(9)} for i in range(4)]
    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
