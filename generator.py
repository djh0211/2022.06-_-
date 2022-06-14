from typing import *
import fnmatch
import yaml
import os

def get_list_of_files(dir_name: str):
    fileList = os.listdir(dir_name)
    result = []
    for entry in fileList:
        full_path = os.path.join(dir_name, entry)
        if os.path.isdir(full_path):
            result = result + get_list_of_files(full_path)
        else:
            result.append(full_path)
    return result

# file_list = get_list_of_files(path)

def make_list():
    path = os.getcwd()
    file_list = fnmatch.filter(get_list_of_files(path), "*.py")

    baek_result = []
    other_result = []
    for file in file_list:
        # print(file)
        prob_num = file.split("/")[-1].split(".")[0]
        if prob_num.isdigit():
            baek_result.append(prob_num)
        elif prob_num != 'generator':
            other_result.append(prob_num)

    return baek_result, other_result

def make_markdown_table(hlist: list[dict]):
    """
    흠..
    """
    result = []

    columns = [
        {"name": "#", "size": 5},
        {"name": "문제 이름", "size": 20},
        {"name": "유형", "size": 15},
        {"name": "풀이", "size": 10},
        {"name": "완료", "size": 6},
    ]
    result.append('|'.join([key["name"] for key in columns]))
    result.append('|'.join([key["size"]*'-' for key in columns]))

    # for index, header in enumerate(hlist):
    #     done = '✔️' if header["done"] else '❌'
    #     result.append(
    #         f"{index+1}|[{header['name']}]({header['src']})|{', '.join(header['tags'])}|[{header['file_name']}]({header['file']})|{done}")
    # result.append('')
    return '\n'.join(result)

def file_read_to_end(path: str):
    f = open(path, "r", encoding='utf-8')
    content = f.read()
    f.close()
    return content


a,b = make_list()
# print(a)
# print(b)
md_table = make_markdown_table(a)

# print(md_table)

template = file_read_to_end('template.md')
readme_text = template.replace("__baekjoon_table__", md_table)
path = os.getcwd()

f = open(os.path.join(path, 'README2.md'), "w", encoding='utf-8')
f.write(readme_text)
f.close()

