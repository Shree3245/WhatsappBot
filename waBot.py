from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4
import time
import pyautogui
import openpyxl

autoMsg = "Hello this is .... Please submit your name of the format 'name: abc xyz' and your phone number along with email in three different texts please"

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

time.sleep(10)

input("Press Enter After Scanning QR Code: ")
time.sleep(5)
while True:
    nPE = []
    target = str(input("What is the target number: "))
    time.sleep(8)
    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite('api.whatsapp.com/send?phone=91'+target)
    pyautogui.hotkey('enter')
    time.sleep(10)
    pyautogui.moveTo(650, 350, duration = 0.1)
    pyautogui.click()
    time.sleep(10)
    pyautogui.typewrite(autoMsg)
    driver.find_element_by_class_name("_2lkdt").click()
    time.sleep(2)
    page = driver.page_source
    soup = bs4.BeautifulSoup(page,'html.parser')
    i = 1
    prompt = input("Press y once the other party has sent the required data: I.E. Name, email, phone number:  ")
    time.sleep(5)
    if "y" in prompt:
        xx=soup.findAll("div", {"class": "Tkt2p"})
        for i in xx:
            i = i.text[:-7]
            if autoMsg in i:
                i = ""
            if target in i:
                i.replace(target, "")
            if "name: " in i:
                name= i[5:]
                nPE.insert(0,name)
            else:
                reply1 = "Please put your name in the form of name: "
            if ("@gmail.com" or "@yahoo.com" or "@icloud" or "@outlook") in xx:
                email = i
                nPE.insert(2,email)
            else:
                reply2 = "The email seems to be wrong please try again"
                pyautogui.typewrite(reply2)
                driver.find_element_by_class_name("_2lkdt").click()

            if len(i)==10:
                try:
                    num = int(i)
                    num = str(num)
                    nPE.insert(1,num)
                    
                except:
                    reply = "The phone number you seem to have entered seems wrong please try again"
                    pyautogui.typewrite(reply)
                    driver.find_element_by_class_name("_2lkdt").click()   
            else:
                reply3 = "That doesnt look like a phone number. Leave out the country code please."
                pyautogui.typewrite(reply)
                driver.find_element_by_class_name("_2lkdt").click()
    else:
        pass

    """
    There exists a list called nPE which contains data in the order of Name, Phone Number and email in that order.
    I dont know how you require the information so I stopped the code right here.
    """



