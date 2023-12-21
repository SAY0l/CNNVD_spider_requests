import requests
import json
import time
from base import *
from database import mysql_insert_data
from concurrent.futures import ThreadPoolExecutor,as_completed

def get_page_pocs(Page_info):
    retries = 0
    connected = False
    while not connected and retries < Max_retries:
        try:
            response = requests.post(Pages_url,headers=header,json=Page_info,timeout=Timeout)
            connected = True
        except requests.exceptions.RequestException:
            retries += 1
            print(f'Timeout, retry {retries} ...')

    assert response.status_code == 200 , ">>> network wrong! u can't get page"
    page_pocs = json.loads(response.text)["data"]["records"]

    return page_pocs


def get_poc(poc):
    retries = 0
    connected = False
    goal ={}
    Poc_info={}
    Poc_info['id'] = poc['id']
    Poc_info['vulType'] = poc['vulType']
    Poc_info['cnnvdCode'] = poc['cnnvdCode']
    while not connected and retries < Max_retries:
        try:
            response = requests.post(Poc_url,headers=header,json=Poc_info,timeout=Timeout)
            goal= json.loads(response.text)["data"]["cnnvdDetail"]
            connected = True
        except Exception as e:
            retries += 1
            print(">>> wrong info:",e)
            print(f'>>> something wrong, retry {retries} ... if retry==3 ,we will skip')

    
    return goal

def Delay_time():
    print(">>>> delay..."+str(Time_Delay)+"s")
    time.sleep(Time_Delay)
    

def engine_start_one(Page_info):
    page_pocs = get_page_pocs(Page_info)
    if len(page_pocs) == 0:
        print(">>> no search results, engine stop")
    else:
        for i in page_pocs:
            goal=get_poc(i)
            if len(goal)!=0:
                print(">>> now dealing..."+goal['vulName'])
                mysql_insert_data(goal)
                if Task.failure_flag:
                    break
            Delay_time()

def engine_start_thread(Page_info):
    page_pocs = get_page_pocs(Page_info)
    if len(page_pocs) == 0:
        print(">>> no search results, engine stop")
    else:
        with ThreadPoolExecutor(max_workers=Task.threads) as t:
            goals = [t.submit(get_poc,i) for i in page_pocs]
                
            for goal in as_completed(goals):
                goal = goal.result()
                if len(goal)!=0:
                    print(">>> now dealing..."+goal['vulName'])
                    mysql_insert_data(goal)
                    if Task.failure_flag:
                        break
            
