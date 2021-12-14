#coding:utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import ctypes

username_str = '21110010001'
password_str = 'FDU123456'

whnd = ctypes.windll.kernel32.GetConsoleWindow()

class Login:
    def login(self):
        try:
            # chrome_driver=r"C:\ProgramData\Miniconda3\Lib\site-packages\selenium\chromedriver.exe"
            chrome_driver=r"chromedriver.exe"
            # driver = webdriver.Firefox()
            driver=webdriver.Chrome(executable_path=chrome_driver)
            driver.get("http://10.108.255.249/srun_portal_pc.php?ac_id=1&&phone=1")
            time.sleep(1)
            
            username_input = driver.find_element_by_name('username')
            password_input = driver.find_element_by_id('password')
            login_button = driver.find_element_by_id('button')

            username_input.send_keys(username_str)
            password_input.send_keys(password_str)
            login_button.click()
        except:
            print(self.getCurrentTime(), u"登陆函数异常")
        finally:
            driver.close()


    #获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

    #判断当前是否可以连网
    def canConnect(self):
        try:
            baidu_request=requests.get("http://www.baidu.com")
            if(baidu_request.status_code==200):
                baidu_request.encoding = 'utf-8'
                baidu_request_bsObj = BeautifulSoup(baidu_request.text, 'html.parser')
                baidu_input = baidu_request_bsObj.find(value="百度一下")
                if baidu_input==None:
                    return False
                return True
            else:
                return False
        except:
            print ('error')

    #主函数
    def main(self):
        print (self.getCurrentTime(), u"Hi，FDU-net自动登陆脚本正在运行")
        while True:
            can_connect = self.canConnect()
            if not can_connect:
                print (self.getCurrentTime(),u"断网了...")
                try:
                    self.login()
                except:
                    print(self.getCurrentTime(), u"浏览器出了bug")
                finally:
                    time.sleep(1)
                    if self.canConnect():
                        print(self.getCurrentTime(), u"重新登陆成功! 将在后台运行，保证网络断开时重连。")
                        time.sleep(2)
                        if whnd != 0:
                            ctypes.windll.user32.ShowWindow(whnd, 0)
                            ctypes.windll.kernel32.CloseHandle(whnd)
                    else:
                        print(self.getCurrentTime(), u"登陆失败，再来一次")
            else:
                print (self.getCurrentTime(), u"宁已连接网络... 将在后台运行，保证网络断开时重连。")
                time.sleep(2)
                if whnd != 0:
                    ctypes.windll.user32.ShowWindow(whnd, 0)
                    ctypes.windll.kernel32.CloseHandle(whnd)
                time.sleep(10)
            time.sleep(1)

login = Login()
login.main()
