from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import mydef as my



# クレジットカード情報
# month = "XX"
# year = "XX"
# num = "XXXXXXXXXXXXX"
# code = "XXX"

def main(browser):
    flag = False
    # カートに追加
    if my.clickClassButton(browser, "add_cart_btn", 0):
        browser.save_screenshot("1-1.png")
        print("カートに入れたー")

        # カートに移動
        if my.cart(browser):
            browser.save_screenshot("1-2.png")
            print("カート画面に移動したー")

            # ログイン画面に移動
            if my.clickIdButton(browser, "nextStep", 0):
                browser.save_screenshot("1-3.png")
                print("ログイン画面に移動したー")

                # ログイン情報
                mail = "neet.2.10ogi@gmail.com"
                key = "k83186680"
                # ログイン情報入力
                if my.inputLogin(browser, mail, key, 0):
                    browser.save_screenshot("1-4.png")
                    print("ログイン情報入れたー")

                    # ログインボタンクリック
                    if my.clickIdButton(browser, "login_submit", 0):
                        browser.save_screenshot("1-5.png")
                        print("配送先これにしたー")

                        # お届け先画面から移動
                        if my.clickClassButton(browser, "next_step", 0):
                            browser.save_screenshot("1-6.png")
                            print("クレジットで払うぞー")

                            # 支払い方法選択
                            if my.clickClassButton(browser, "next_step", 0):
                                browser.save_screenshot("1-7.png")
                                print("注文確認したぞー")

                                # クレジットカード情報入力（初回購入時のみ）
                                # my.inputCredit(browser, month, year, num, code, 0)

                                # 購入ボタンを押す
                                if my.clickIdButton(browser, "checkout_btn", 0):
                                    flag = True
                                    browser.save_screenshot("1-8.png")
                                    print("買ったー")
    else:
        flag = False

    if flag == False:
        main(browser)

#  テスト
testURL = "https://www.pokemoncenter-online.com/?p_cd=4521329222738"
# 本番(ウルトラシャイニー)
URL = "https://www.pokemoncenter-online.com/?p_cd=4521329241210"

# ブラウザ起動ver
# driver = './chromedriver'
# browser = webdriver.Chrome(driver)

# headless ver
options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=options)
browser.get(URL)

# スクリーンショット用設定
page_width = browser.execute_script('return document.body.scrollWidth')
page_height = browser.execute_script('return document.body.scrollHeight')
browser.set_window_size(page_width, page_height)

main(browser)