#!/bin/bash

# 生成静态文件
pelican content

# 切换到 output 目录
cd output || { echo "output 目录不存在"; exit 1; }

# 初始化 Git 仓库（如果还没有）
git init

# 添加所有文件
git add .

# 提交更改
git commit -m "Update site"

# 推送到 GitHub Pages
# git push -f https://github.com/zhaoteng2025/zhaoteng2025.github.io.git main:gh-pages

# 检查远程仓库地址
if ! git remote get-url origin &>/dev/null; then
    git remote add origin https://github.com/zhaoteng2025/zhaoteng2025.github.io.git
fi

# 推送到 GitHub Pages
git push -f origin main:gh-pages || {
    echo "推送失败，请检查远程仓库地址和权限";
    exit 1;
}

# 返回项目根目录
cd ..
