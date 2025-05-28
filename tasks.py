# tasks.py
"""
Invoke tasks. Run 'invoke --help' for help.
执行命令：invoke clean/build/publish等
远程部署到github命令 .\deploy.sh
"""

import os
import shutil
from invoke import task

@task
def clean(c):
    """清除输出目录"""
    if os.path.exists('output'):
        shutil.rmtree('output')

@task(pre=[clean])
def build(c):
    """生成静态文件"""
    c.run('pelican content -s pelicanconf.py')

@task(pre=[clean])
def rebuild(c):
    """重新生成静态文件"""
    c.run('pelican content -s pelicanconf.py -r -w')

@task
def regenerate(c):
    """实时生成静态文件"""
    c.run('pelican content -r -w -s pelicanconf.py')

@task
def serve(c):
    """启动本地服务器"""
    c.run('cd output && python -m http.server 8000')

@task(pre=[build])
def preview(c):
    """预览博客"""
    c.run('cd output && python -m http.server 8000')

@task(pre=[clean])
def livereload(c):
    """实时预览博客"""
    from livereload import Server
    server = Server()
    server.watch('content', lambda: c.run('pelican content -s pelicanconf.py'))
    server.serve(root='output')

@task(pre=[clean, build])
def publish(c):
    """发布博客"""
    c.run('pelican content -s publishconf.py')
