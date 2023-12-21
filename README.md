# 描述
通过异步线程池及异步进程池，js逆向api接口，快速爬取cnnvd公开数据并存储至数据库。
# 使用说明
起始页数和结尾页数两个参数是必需的，因为官网会更新数据。
```
usage: main.py [-h] [-A] [-U] [-s START_PAGE] [-e END_PAGE]

CNNVD_spider_requests: Crawl CNNVD Data Rapidly

options:
  -h, --help            show this help message and exit
  -A, --all             Crawl all cnnvd data
  -U, --update          Update cnnvd data
  -s START_PAGE, --start_page START_PAGE
                        start page number
  -e END_PAGE, --end_page END_PAGE
                        end page number

Author:
    sayol  <github@sayol.com>
Version:
    1.0
Config:
    >>> u must indicate start_page and end_page <<<
```

# 注意事项
1. cnnvd通过api接口工作，在base.py中筛选定制每页数据。数据库配置在database.py中修改，推荐以cnnvd编号作为主键。

2. 全量爬取。在标准数据，每页50的数据量下，建议进程为30，线程为17，速度约为5000条/10s。可根据服务器性能、网络状况适当调整。进程不建议超过50，线程不建议超过每页数据量的1/3。

3. 更新爬取。数据量小，使用单线程，速度较慢，安全性较高。

4. 因为是页面爬取，不会有重复数据，仅为停止模式，当有数据错误时为终止程序。

# bug
需要在cli.py中配置页面的相关属性才能真正生效。