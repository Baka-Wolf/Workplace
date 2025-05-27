#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def hex_to_rgb(hex_code):
    """将 HEX 转换为 RGB"""
    hex_code = hex_code.lstrip('#')
    if len(hex_code) == 6:
        return tuple(int(hex_code[i:i + 2], 16) for i in (0, 2, 4))
    else:
        raise ValueError("HEX 颜色代码格式不正确！")

def rgb_to_hex(rgb):
    """将 RGB 转换为 HEX"""
    if len(rgb) != 3 or not all(0 <= x <= 255 for x in rgb):
        raise ValueError("RGB 颜色代码格式不正确！")
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def rgba_to_hex(rgba):
    """将 RGBA 转换为 HEX"""
    if len(rgba) != 4 or not all(0 <= x <= 255 for x in rgba[:3]) or not (0 <= rgba[3] <= 1):
        raise ValueError("RGBA 颜色代码格式不正确！")
    alpha = int(rgba[3] * 255)
    return '#{:02x}{:02x}{:02x}{:02x}'.format(*rgba[:3], alpha)

def hex_to_rgba(hex_code, alpha=1.0):
    """将 HEX 转换为 RGBA"""
    rgb = hex_to_rgb(hex_code)
    return (*rgb, alpha)

def rgb_to_rgba(rgb, alpha=1.0):
    """将 RGB 转换为 RGBA"""
    return (*rgb, alpha)

def rgba_to_rgb(rgba):
    """将 RGBA 转换为 RGB"""
    return rgba[:3]

def is_valid_hex(hex_code):
    """验证是否是合法 HEX 代码"""
    return bool(re.fullmatch(r"#?[0-9A-Fa-f]{6}|[0-9A-Fa-f]{8}", hex_code))

def main():
    print("欢迎使用颜色转换工具！")
    print("支持的转换格式：")
    print("1️⃣ HEX ➡️ RGB / RGBA")
    print("2️⃣ RGB ➡️ HEX / RGBA")
    print("3️⃣ RGBA ➡️ HEX / RGB")

    choice = input("\n请选择转换类型（1/2/3）：").strip()

    if choice == '1':
        hex_code = input("请输入 HEX 颜色代码（例如 #ff5733）：").strip()
        if is_valid_hex(hex_code):
            print(f"RGB 格式：{hex_to_rgb(hex_code)}")
            alpha = float(input("请输入透明度（0~1），默认1：") or 1)
            print(f"RGBA 格式：{hex_to_rgba(hex_code, alpha)}")
        else:
            print("❌ 输入的 HEX 代码无效！")

    elif choice == '2':
        rgb_input = input("请输入 RGB 颜色（例如 255,87,51）：").strip()
        try:
            rgb = tuple(map(int, rgb_input.split(',')))
            print(f"HEX 格式：{rgb_to_hex(rgb)}")
            alpha = float(input("请输入透明度（0~1），默认1：") or 1)
            print(f"RGBA 格式：{rgb_to_rgba(rgb, alpha)}")
        except ValueError:
            print("❌ 输入的 RGB 代码无效！")

    elif choice == '3':
        rgba_input = input("请输入 RGBA 颜色（例如 255,87,51,0.5）：").strip()
        try:
            rgba = rgba_input.split(',')
            rgba = (int(rgba[0]), int(rgba[1]), int(rgba[2]), float(rgba[3]))
            print(f"HEX 格式：{rgba_to_hex(rgba)}")
            print(f"RGB 格式：{rgba_to_rgb(rgba)}")
        except ValueError:
            print("❌ 输入的 RGBA 代码无效！")

    else:
        print("❌ 选择无效，请输入 1、2 或 3。")

if __name__ == '__main__':
    main()