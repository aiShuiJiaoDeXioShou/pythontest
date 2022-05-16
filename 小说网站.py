import requests
import re

if __name__ == '__main__':
    # 获取小说的网址！
    cc = input("请输入小说的网址：")
    # 访问小说的网址并且获得源代码！
    html = requests.get(cc)
    html.encoding = "utf-8"
    # 通过正则表达式获取每章小说的网址！
    urls = re.findall("<dd><a href='(.*?)' >", html.text)
    cx = len(urls)  # 获取列表长度
    print("总共有：%d" % cx)
    i = 0
    for url in urls:
        i = i + 1
        wz = "http://www.xbiquge.la" + url  # 获取完整的每章网址
        zw = requests.get(wz)  # 获取每章网址的源代码
        zw.encoding = "utf-8"
        nr = re.findall(">&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />", zw.text)  # 获取每章的内容
        mz = re.findall("<h1>(.*?)</h1>", zw.text)  # 获取每章的标题
        mzm = mz[0] + ".text"
        with open(mzm, "w") as object:
            nrn = "".join(nr)
            object.write(nrn)  # 保存
            print("已完成%d" % i)
            if i == cx:
                print("下载完成！")

