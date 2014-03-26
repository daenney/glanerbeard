import json


def json_print(value):
    return json.dumps(value, indent=2, separators=(',', ': '))