
import json

json_string = '''
{
    "name": "crise",
    "age": 18,
    "parents": {
        "monther": "妈妈",
        "father": "爸爸"
    }
}
'''

print(type(json_string))

data = json.loads(json_string)

print(type(data))

python_data = {
    "name": "crise",
    "age": 18,
    "parents": {
        "monther": "妈妈",
        "father": "爸爸"
    }
}

print(type(python_data))

json_strings = json.dumps(python_data)

print(json_strings)


def write_json():
    with open('data.json','w',encoding='utf-8') as f:
        json.dump(python_data,f,ensure_ascii=False,indent=2)

write_json()



