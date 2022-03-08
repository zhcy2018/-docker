from __future__ import print_function
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from ruamel.yaml import YAML

yaml = YAML(typ='safe')
with open("./conf.yaml") as ymlfile:
    cfg = yaml.load(ymlfile)['CONF']
    url = cfg['url']
    username = cfg['username']
    passwd = cfg['passwd']
    user_xpath = cfg['user_xpath']
    passwd_xpath = cfg['passwd_xpath']
    submit_xapth = cfg['submit_xpath']
chrome_opt = Options()
chrome_opt.binary_location = '/usr/bin/google-chrome-stable'
chrome_opt.add_argument('--headless')
chrome_opt.add_argument('--disable-gpu')
chrome_opt.add_argument('--window-size=1366,768')
chrome_opt.add_argument("--no-sandbox")

while 1:
    try:
        res=requests.get('https://www.baidu.com/', timeout=5,proxies={'http':None,'https':None})
        print(res.status_code)
        time.sleep(60)
    except requests.exceptions.ConnectTimeout:
        try:
            browser = webdriver.Chrome(
                executable_path='/var/xssbot/chromedriver', chrome_options=chrome_opt)
            browser.get(url)
            username_ele = browser.find_element_by_xpath(user_xpath)
            username_ele.send_keys(username)
            passwd_ele = browser.find_element_by_xpath(passwd_xpath)
            passwd_ele.send_keys(passwd)
            sub_ele = browser.find_element_by_xpath(submit_xapth)
            sub_ele.click()
            time.sleep(5)
            browser.quit()
        except Exception as e:
            print(e)
            browser.quit()