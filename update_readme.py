#! /usr/bin/python
# coding:utf-8

"""update_readme.py: update readme files automatical"""

__author__      = "Jory Liang"
__copyright__   = "Copyright 2015, Tamer"

import os
import re

# 要扫描的文件夹，默认为当前文件夹
DEFAULT_FOLDER = "."
FOLDER_NAME = "README.md"

# 默认支持的语言，用后缀名来判断
type_of_lang = {"sh":"Shell", "py":"Python", "lua":"Lua", "js":"JavaScript", "java":"Java"}

# 存放所有的列表
rootList = {}
exList = {}

# 匹配后缀
p = re.compile(r'^.*\.(\w+?)$')

def write_with_log(fo, line):
    fo.write(line)
    print(line)

def print_formatted():
    
    with open(DEFAULT_FOLDER + '/' + FOLDER_NAME, 'w') as f:
        # 打印标题
        write_with_log(f, '# PAT Practise - Basic Level!\n')
        write_with_log(f, 'a pat practise of liangzr\n\n')

        # 循环打印标题
        write_with_log(f, '### language\n\n')
        for key in rootList:
            write_with_log(f, '- [' + type_of_lang[key] + '](#' + type_of_lang[key] + ')\n')
        write_with_log(f, '\n')

        # 循环打印各语言
        for key in rootList:
            write_with_log(f, '## ' + type_of_lang[key] + '\n\n')
            pathList = rootList[key]
            for item in pathList:
                try:
                    index, path = item.split('/')
                    write_with_log(f, '- [' + exList[index] + '](' + item + ')\n')
                except Exception as e:
                    pass
            write_with_log(f, '\n')

def scan_folder(sub_dir="", root_dir=DEFAULT_FOLDER, level=1):
    
    for lists in os.listdir(os.path.join(root_dir, sub_dir)):
        # 跳过隐藏文件夹
        if lists[0] == ".":
            continue

        path = os.path.join(sub_dir, lists)
        # print path
        print '│  '*(level-1)+'│--' + lists
        if os.path.isdir(os.path.join(root_dir, path)):
            scan_folder(path, root_dir, level + 1)
        elif os.path.isfile(os.path.join(root_dir, path)):
            handle_files(path)

def handle_files(path):
    m = p.findall(path)
    if m:
        tp = m[0]
        if tp == "md":
            try:
                index, title = path.split('/')
                exList[index] = title
            except Exception as e:
                pass
        elif tp == "png":
            pass
        else:
            if (tp not in rootList) and (tp in type_of_lang):
                rootList[tp] = []
            if rootList.has_key(tp):
                # 将文件添加进列表字典
                rootList[tp].append(path)


def main():
    print "\n-------------- scan your folder --------------\n"
    scan_folder()
    print "\n-------------- printing --------------\n"
    print_formatted()
    print "\n-------------- Done! --------------\n"

if __name__ == '__main__':
    main()