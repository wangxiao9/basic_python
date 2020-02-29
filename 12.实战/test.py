import re

content = '<use xlink:href="#icon-user_c95acf8"></use></svg>长沙乡村敢死队</h2></div>'

pattern = '<use xlink:href="#icon-user_([\s\S\W]*?)</div>'

result = re.findall(pattern, content)
result1 = re.findall('</use></svg>([\s\S]*?)</h2>',result[0])
print(result1)