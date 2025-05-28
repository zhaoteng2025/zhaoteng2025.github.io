# 基本配置
SITENAME = '小腾腾的小站'
SITEURL = ''
AUTHOR = '赵腾'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'zh'

# 文章路径
PATH = 'content'
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

# 输出路径
OUTPUT_PATH = 'output'

# 全局时间格式
DATE_FORMATS = {
    'zh': '%Y-%m-%d %H:%M',
}

# 主题设置
THEME = 'themes/flex'

# 插件设置
PLUGIN_PATHS = ['plugins']
PLUGINS = ['neighbors', 'related_posts']

# 主题特定配置
SITETITLE = '我的技术博客'
SITESUBTITLE = '记录技术，分享经验'
SITEDESCRIPTION = '这是一个关于编程和技术的博客'
SITELOGO = '/images/profile.png'
MAIN_MENU = True
MENUITEMS = (
    ('归档', '/archives.html'),
    ('分类', '/categories.html'),
    ('标签', '/tags.html'),
)
COPYRIGHT_NAME = '赵腾'
COPYRIGHT_YEAR = 2024

# 文章和页面的 URL 格式
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# 静态文件
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# 评论系统
DISQUS_SITENAME = 'your-disqus-sitename'

# 社交链接
SOCIAL = (
    ('GitHub', 'https://github.com/xttgithub'),
)

# 额外的元数据
DEFAULT_PAGINATION = 10

# 发布配置
RELATIVE_URLS = False

# GitHub Pages 配置
GITHUB_URL = 'https://github.com/xttgithub/xtt.github.io'

