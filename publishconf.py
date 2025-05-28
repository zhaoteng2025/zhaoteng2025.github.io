# 导入 pelicanconf.py 中的配置
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# 生产环境设置
SITEURL = 'https://xtt.github.com'
RELATIVE_URLS = False

# 静态文件
DELETE_OUTPUT_DIRECTORY = True

# Feed 生成
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# 额外的元数据
DEFAULT_PAGINATION = 10
