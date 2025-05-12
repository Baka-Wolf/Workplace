#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def main():
    # 1. 选择生成选项
    choice = ''
    while choice.lower() not in ('md', 'html','py'):
        choice = input("请选择要生成的文件类型（md/html/py）：").strip()
    
    # 2. 输入名字
    name = ''
    while not name:
        name = input("请输入文件名（不包含后缀）：").strip()
    
    # 3. 确定目录和后缀
    if choice.lower() == 'md':
        folder = 'md'
        ext = '.md'
    elif choice.lower() == 'HTML':
        folder = 'HTML'
        ext = '.html'
    else:
        folder = 'py'
        ext = '.py'
    
    # 4. 创建目录（如果不存在）
    os.makedirs(folder, exist_ok=True)
    
    # 5. 创建文件
    file_path = os.path.join(folder, name + ext)
    if os.path.exists(file_path):
        print(f"⚠ 文件已存在：{file_path}")
    else:
        with open(file_path, 'w', encoding='utf-8') as f:
            # 此处可以写入模板内容，例如：
            # if ext == '.md': f.write(f"# {name}\n\n")
            # else: f.write(f"<!DOCTYPE html>\n<html>\n<head><title>{name}</title></head>\n<body>\n</body>\n</html>")
            pass
        print(f"✅ 已创建文件：{file_path}")

if __name__ == '__main__':
    main()