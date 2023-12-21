Pages_url= "https://www.cnnvd.org.cn/web/homePage/cnnvdVulList"

Poc_url = "https://www.cnnvd.org.cn/web/cnnvdVul/getCnnnvdDetailOnDatasource"

class Page :
    info = {
    "pageIndex": 1, #页数
    "pageSize": 50, #每页数量
    "keyword": "", #CNNVD编号，CVE编号
    "hazardLevel": "", #1:超危；2:高危；3:中危；4:低危
    "vulType": "", #漏洞类型，需要在页面获取hash值，没有在代码实现
    "vendor": "", #参考vendor.json
    "product": "", #暂无
    "dateType": "", #publishTime/updateTime

    #以下为可选参数，需要配合dateType使用
    #beginTime:"2023-09-23", 
    #endTime:"2024-06-06",
}
    def __init__(self,pageIndex:int,pageSize:int,keyword="",hazardLevel="",vulType="",vendor="",product="",dateType=""):
        self.info['pageIndex'] = pageIndex
        self.info['pageSize'] = pageSize
        self.info['keyword'] = keyword
        self.info['hazardLevel'] = hazardLevel
        self.info['vulType'] = vulType
        self.info['vendor'] = vendor
        self.info['product'] = product
        self.info['dateType'] = dateType

header = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://www.cnnvd.org.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://www.cnnvd.org.cn/home/loophole',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site': 'same-origin',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}

Timeout = 6

Time_Delay = 1

Max_retries = 3

class Task:
    count = 0

    failure_flag = False
    
    process = 30 #更改进程数

    threads = 17 #更改线程数
    