#%%
import os
from time import sleep
#selenium libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from modules.cswait import SWait
from modules.Metamask import SMetamask

options = Options()
options.add_argument("user-data-dir=E:/Chrome_Portable/chrome_4/Data/profile")
driver = webdriver.Chrome(executable_path='E:/tools/webdriver/chromedriver.exe', options=options)
cswait = SWait(driver)
metamask = SMetamask(driver,cswait)
metamask.Login('tuan0910')
sleep(2)
metamask.OpenTab()

#%%
# metamask = SMetamask()

print(metamask.GetNextWalletCurrentTab())

# metamask.BackupWithoutKey('backup_without_key_chrome_7.txt')
# metamask.BackupWithKey('backup_with_key_3.txt')






