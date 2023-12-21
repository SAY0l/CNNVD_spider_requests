import sys
sys.path.append(r"..\\cnnvd_spider_requests")

import argparse
import banner
from engine import engine_start_one,engine_start_thread
from base import Page,Task
from concurrent.futures import ProcessPoolExecutor

def Gen_cli(information):
    parser = argparse.ArgumentParser(description=information[0],formatter_class=argparse.RawTextHelpFormatter)
    parser.epilog='''
Author: 
    {}  <{}>
Version: 
    {}
Config:
    {}
    '''.format(information[1],information[2],information[3],information[4])

    parser.add_argument('-A', '--all', action='store_true', help='Crawl all cnnvd data')
    parser.add_argument('-U', '--update', action='store_true', help='Update cnnvd data')
    
    parser.add_argument('-s', '--start_page', type=int, help='start page number')
    parser.add_argument('-e', '--end_page', type=int, help='end page number')

    args = parser.parse_args()

    Parse_cli(args,parser)

def Parse_cli(args,parser):
    if args.start_page and args.end_page:
        if args.all:
            get_all(args.start_page,args.end_page)
        elif args.update:
            update_data(args.start_page,args.end_page)
    else:
        parser.print_help()

def update_data(start_page,end_page):
    banner.title()

    Start_page = start_page
    End_page = end_page # 此处配置获取页数

    for i in range(Start_page,End_page+1):
        print(">>> now crawling page ",i)
        Page_info = Page(i,50).info # 此处配置每页想要获取的数据内容
        engine_start_one(Page_info)

        if Task.failure_flag:
            break           #减少冗杂数据
    
    print(">>> task finished, success: {}".format(Task.count))

def get_all_pre(i):
    print(">>> now crawling page ",i)
    Page_info = Page(i,50).info # 此处配置每页想要获取的数据内容
    engine_start_thread(Page_info)


def get_all(start_page,end_page):
    banner.title()

    Start_page = start_page
    End_page = end_page # 此处配置获取页数

    goal = [i for i in range(Start_page,End_page+1)]

    with ProcessPoolExecutor(max_workers=Task.process) as p:
        for i in goal:
            p.submit(get_all_pre,i)

    print(">>> task finished")