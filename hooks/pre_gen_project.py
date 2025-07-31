#!/usr/bin/env python3
"""
Cookiecutter pre-generation hook.
驗證使用者輸入的有效性。
"""

import re
import sys

# 取得 cookiecutter 變數
project_name = "{{ cookiecutter.project_name }}"
project_slug = "{{ cookiecutter.project_slug }}"
python_version = "{{ cookiecutter.python_version }}"


def validate_project_name():
    """驗證專案名稱"""
    if not project_name or project_name.strip() == "":
        print("❌ 錯誤：專案名稱不能為空")
        return False

    if len(project_name) > 50:
        print("❌ 錯誤：專案名稱太長（超過50字元）")
        return False

    return True


def validate_project_slug():
    """驗證專案 slug"""
    if not re.match(r"^[a-z0-9\-]+$", project_slug):
        print(f"❌ 錯誤：專案 slug '{project_slug}' 只能包含小寫字母、數字和連字號")
        return False

    if project_slug.startswith("-") or project_slug.endswith("-"):
        print(f"❌ 錯誤：專案 slug '{project_slug}' 不能以連字號開頭或結尾")
        return False

    return True


def validate_python_version():
    """驗證 Python 版本"""
    valid_versions = ["3.8", "3.9", "3.10", "3.11", "3.12", "3.13"]

    if python_version not in valid_versions:
        print(f"❌ 錯誤：不支援的 Python 版本 '{python_version}'")
        print(f"   支援的版本：{', '.join(valid_versions)}")
        return False

    return True


def main():
    """主要驗證流程"""
    print("🔍 正在驗證輸入參數...")

    validations = [
        ("專案名稱", validate_project_name),
        ("專案 slug", validate_project_slug),
        ("Python 版本", validate_python_version),
    ]

    for name, validator in validations:
        if not validator():
            print(f"\n💡 提示：請修正 {name} 後重新執行")
            sys.exit(1)

    print("✅ 所有參數驗證通過！")
    print(f"   專案名稱：{project_name}")
    print(f"   專案 slug：{project_slug}")
    print(f"   Python 版本：{python_version}")


if __name__ == "__main__":
    main()
