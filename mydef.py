from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

def clickClassButton(browser, className, loop):
    try:
        searchButton = browser.find_element_by_class_name(className)
        searchButton.click()
        return True
    except:
        sleep(0.1)
        loop = loop + 1
        print(browser.current_url)
        if loop == 30:
            if browser.current_url == "https://www.pokemoncenter-online.com/maintenance.php":
                browser.get("https://www.pokemoncenter-online.com/?p_cd=4521329241210")
                return False
            else:
                brwoser.refresh()
                clickClassButton(browser, className, loop)
            loop = 0
        

def clickIdButton(browser, idName, loop):
    try:
        searchButton = browser.find_element_by_id(idName)
        searchButton.click()
        return True
    except:
        sleep(0.1)
        loop = loop + 1
        print(browser.current_url)
        if loop == 30:
            if browser.current_url == "https://www.pokemoncenter-online.com/maintenance.php":
                browser.get("https://www.pokemoncenter-online.com/?p_cd=4521329241210")
                return False
            else:
                browser.get("https://www.pokemoncenter-online.com/?p_cd=4521329241210")
                return False
                #clickIdButton(browser, idName, loop)
            loop = 0
        
def cart(browser):
    browser.get("https://www.pokemoncenter-online.com/?main_page=shopping_cart")
    print(browser.current_url)
    sleep(0.1)
    if browser.current_url == "https://www.pokemoncenter-online.com/maintenance.php":
        cart(browser)
    else:
        return True

def clickTextA(browser, text, loop):
    try:
        continue_link = browser.find_element_by_partial_link_text(text)
        continue_link.click()
        return True
    except:
        sleep(0.1)
        loop = loop + 1
        print(browser.current_url)
        if loop == 30:
            if browser.current_url == "https://www.pokemoncenter-online.com/maintenance.php":
                browser.get("https://www.pokemoncenter-online.com/?p_cd=4521329241210")
                return False
            else:
                brwoser.refresh()
                clickTextA(browser, text, loop)
            loop = 0
        

def inputLogin(browser, mail, key, loop):
    try:
        #input タグ id=“login_mail”にneet.2.30ogi@gmail.comを挿入
        #input タグ id=“login_pass”にk83186680を挿入
        form_mail = browser.find_element_by_id("login_mail")
        form_mail.clear()
        form_mail.send_keys(mail)
        form_pass = browser.find_element_by_id("login_pass")
        form_pass.clear()
        form_pass.send_keys(key)
        return True
    except:
        sleep(0.1)
        loop = loop + 1
        print(browser.current_url)
        if loop == 30:
            if browser.current_url == "https://www.pokemoncenter-online.com/maintenance.php":
                browser.get("https://www.pokemoncenter-online.com/?p_cd=4521329241210")
                return False
            else:
                brwoser.refresh()
                inputLogin(browser, mail, key, loop)
            loop = 0

def inputCredit(browser, month, year, num, code, loop):
    try:
        # select タグ id=“cc_expires_monthの選択をクレジットの有効期限月に変更
        # select タグ id=“cc_expires_yearの選択をクレジットの有効期限年に変更
        # input タグ id=“cc_number”にクレジットカード番号を挿入
        # input タグ id=“cc_security_codeにセキュリティコードを挿入
        select_month = browser.find_element_by_id("cc_expires_month")
        select_year = browser.find_element_by_id("cc_expires_year")
        select_month_cast = Select(select_month)
        select_year_cast = Select(select_year)
        select_month_cast.select_by_value(month)
        select_year_cast.select_by_visible_text(year)

        input_num = browser.find_element_by_id("cc_number")
        input_code = browser.find_element_by_id("cc_security_code")
        input_num.clear()
        input_code.clear()
        input_num.send_keys(num)
        input_code.send_keys(code)
        return True
    except:
        sleep(0.1)
        loop = loop + 1
        print(browser.current_url)
        if loop == 30:
            if browser.current_url == "https://www.pokemoncenter-online.com/maintenance.php":
                browser.get("https://www.pokemoncenter-online.com/?p_cd=4521329241210")
                return False
            else:
                brwoser.refresh()
                inputCredit(browser, loop)
            loop = 0
        