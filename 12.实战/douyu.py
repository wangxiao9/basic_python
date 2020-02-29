'''
1. 爬取斗鱼
 - 爬取斗鱼二次元页面，热度最高的用户，降序排序
 分析
    - 1. 首先获取二次元页面的html
    - 2. 正则表达式提取用户+用户热度
    - 3. 把获取的内容转化成字典
    - 4. 按照热度，降序排序
    - 5. 重新sort_seed方法，如果有万字*10000
    - 6. 把结果show出来
'''

# 使用requests库
import re, requests

class DouYuHot:
    url = "https://www.douyu.com/g_ecy"
    root_pattern = '<li class="layout-Cover-item">([\s\S]*?)</li>'
    hot_pattern = '</svg>([\s\S]*?)</span>'
    name_pattern_root = '<use xlink:href="#icon-user_([\s\S]*?)</div>'
    name_pattern = '</use></svg>([\s\S]*?)</h2>'

    def __get_htmls(self):
        r = requests.get(DouYuHot.url)
        htmls = r.text
        return htmls

    def __analysis(self, htmls):
        results = re.findall(self.root_pattern, htmls)
        anchors = []
        for html in results:
            name_root = re.findall(DouYuHot.name_pattern_root, html)
            name = re.findall(DouYuHot.name_pattern, name_root[0])
            number = re.findall(DouYuHot.hot_pattern, html)
            anchor = {'name':name,'number':number}
            anchors.append(anchor)
        return anchors
    
    # 转换成字典
    def __refine(self, anchors):
        expression = lambda anchor: {
                'name': anchor['name'][0],
                'number': anchor['number'][0]
            }

        return list(map(expression, anchors))

    # 排序
    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors
    
    # key值排序
    def __sort_seed(self, anchor):
        r = re.findall('\d', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __show(self, anchors):
        for anchor in anchors:
            print(anchor['name'] + '---------------' + anchor['number'])

    def do(self):
        htmls = self.__get_htmls()
        anchors = self.__analysis(htmls)
        anchors = self.__refine(anchors)
        anchors = self.__sort(anchors)
        self.__show(anchors)

if __name__ == "__main__":
    douyuhot = DouYuHot()
    douyuhot.do()   

