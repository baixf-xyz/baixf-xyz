import requests
from lxml import etree


url = "https://raw.githubusercontent.com/baixf-xyz/baixf-xyz.github.io/master/index.html"
domain = "https://java8.ml"
page_res = requests.get(url)
html = etree.HTML(page_res.text)
url_list = [f'{domain}{i}' for i in html.xpath('//div[@class="list-group"]/a/@href')]
title_list = html.xpath('//div[@class="list-group"]/a/span/text()')
post_list = [f"- [{post[1]}]({post[0]})" for post in zip(url_list, title_list)]

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(f'''### Welcome To My Github 👋

![今日诗词](https://v2.jinrishici.com/one.svg)

#### You can catch me:

##### [INDEX传送门](https://baixf.tk)         [BLOG传送门](https://blog.baixf.tk)

### 🎨 Latest blogs

''')
    f.write('\n'.join(post_list[:3]))
    f.write(f'''

[>>> More]({domain}/archives/)

![](https://api.moedog.org/count/@baixf-xyz.readme)

![](https://visitor-badge.glitch.me/badge?page_id=baixf-xyz.readme)

![info](https://github-readme-stats.vercel.app/api?username=baixf-xyz&show_icons=true&count_private=true&hide=prs&theme=default_repocard)

![](https://komarev.com/ghpvc/?username=baixf-xyz&color=dc143c)

[![](https://img.shields.io/badge/OS-Linux-blue?style=flat-square&logo=arch-linux&logoColor=ffffff)](https://www.archlinux.org/)
[![](https://img.shields.io/badge/-Raspberry%20Pi%20%204B-red?style=plastic-square&logo=Raspberry-Pi&logoColor=ffffff)](https://www.raspberrypi.org/)
[![](https://img.shields.io/badge/-Java-007396?style=flat-square&logo=java&logoColor=ffffff)](https://reactjs.org/)
[![](https://img.shields.io/badge/-C-inactive?style=flat-square&logo=C&logoColor=ffffff)](https://reactjs.org/)
[![](https://img.shields.io/badge/-Python-blue?style=flat-square&logo=Python&logoColor=ffffff)](https://www.python.org/)
[![](https://img.shields.io/badge/-Spring-green?style=flat-square&logo=Spring&logoColor=ffffff)](https://spring.io/)
[![](https://img.shields.io/badge/-Markdown-inactive?style=flat-square&logo=Markdown&logoColor=ffffff)](https://markdown-here.com)
[![](https://img.shields.io/badge/-LaTeX-green?style=flat-square&logo=LaTeX&logoColor=ffffff)](https://www.latex-project.org/)
[![](https://img.shields.io/badge/Honor-V10-f5010c?style=flat-square&logo=huawei&logoColor=ffffff)](https://www.huawei.com/)
[![](https://img.shields.io/badge/iPhone-8-f5010c?style=flat-square&logo=Apple&logoColor=ffffff)](https://www.apple.com/)

[![](https://img.shields.io/badge/-Adobe-red?style=flat-square&logo=Adobe&logoColor=ffffff)](https://www.adobe.com)
[![](https://img.shields.io/badge/-Adobe%20Photoshop-blue?style=flat-square&logo=Adobe-Photoshop&logoColor=ffffff)](https://www.adobe.com/cn/products/photoshop.html)
[![](https://img.shields.io/badge/-Adobe%20Illustrator-orange?style=flat-square&logo=Adobe-Illustrator&logoColor=ffffff)](https://www.adobe.com/cn/products/illustrator.html)
[![](https://img.shields.io/badge/-Adobe%20Lightroom%20CC-blue?style=flat-square&logo=Adobe-Lightroom-CC&logoColor=ffffff)](https://www.adobe.com/cn/products/photoshop-lightroom-classic.html)
[![](https://img.shields.io/badge/-Adobe%20Premiere%20Pro-blueviolet?style=flat-square&logo=Adobe-Premiere-Pro&logoColor=ffffff)](https://www.adobe.com/cn/products/premiere.html)
[![](https://img.shields.io/badge/-Adobe%20After%20Effects-informational?style=flat-square&logo=Adobe-After-Effects&logoColor=ffffff)](https://www.adobe.com/cn/products/aftereffects.html)
[![](https://img.shields.io/badge/-Adobe%20Audition-blue?style=flat-square&logo=Adobe-Audition&logoColor=ffffff)](https://www.adobe.com/cn/products/audition.html)

''')
