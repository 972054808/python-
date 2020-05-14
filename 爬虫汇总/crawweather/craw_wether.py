import requests
from bs4 import  BeautifulSoup
import re
class CrawWether:
    def __init__(self):
        #城市编号这里用的是徐州的城市编号
        city_num = '101190802'
        #爬取的是中国天气网
        self.url = 'http://www.weather.com.cn/weather1d/' + city_num + '.shtml#input'
        #进行爬虫头部伪装
        self.kv = {'user-agent': 'Mozilla/5.0',}
    
    def get_html(self):
        r = requests.get(self.url,headers = self.kv,timeout = 30)
        #修改编码方式，防止乱码
        r.encoding = r.apparent_encoding
        return r.text
    
    def get_inf(self):
        html = self.get_html()
        #使用正则表达式获取需要的信息,需要其他信息可以自行更改表达式
        pattern = re.compile(
            '"hidden_title".*?value="(.*?)".*?class="li1 hot".*?<p>(.*?)</p>.*?class="li2 hot".*?<p>(.*?)</p>.*?class="li3 hot".*?<p>(.*?)</p>.*?class="li6 hot".*?<p>(.*?)</p>',
            re.S)
        item = re.findall(pattern, html)
        r_message = '''{}天气：{}\r\n防晒建议：{}\r\n运动建议：{}\r\n穿衣建议：{}\r\n空气建议：{}'''.format('徐州', item[0][0],
                                                                                     item[0][1], item[0][2], item[0][3],
                                                                                     item[0][4])
        return r_message

if __name__ == '__main__':
    wether = CrawWether()
    print(wether.get_inf())


#成果演示
'''徐州天气：05月14日08时 周四  阴转多云  23/18°C
防晒建议：辐射弱，涂擦SPF8-12防晒护肤品。
运动建议：夏天悄然到，肉已无处藏。天气较舒适，快去运动吧。
穿衣建议：建议穿薄外套或牛仔裤等服装。
空气建议：气象条件较不利于空气污染物扩散。。'''