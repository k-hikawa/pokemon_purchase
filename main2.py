from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import mydef as my

# ログイン情報
mail = "XXXXXX"
key = "XXXXXXX"

# クレジットカード情報
month = "XX"
year = "XX"
num = "XXXXXXXXXXXXXXX"
code = "XXX"

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

# カートに追加
my.clickClassButton(browser, "add_cart_btn", 0)
browser.save_screenshot("2-1.png")
print("カートに入れたー")

# カートに移動
my.clickTextA(browser, "カートを見る", 0)
browser.save_screenshot("2-2.png")
print("カート画面に移動したー")

# ログイン画面に移動
my.clickIdButton(browser, "nextStep", 0)
browser.save_screenshot("2-3.png")
print("ログイン画面に移動したー")

# ログイン情報入力
my.inputLogin(browser, mail, key, 0)
browser.save_screenshot("2-4.png")
print("ログイン情報入れたー")

# ログインボタンクリック
my.clickIdButton(browser, "login_submit", 0)
browser.save_screenshot("2-5.png")
print("配送先これにしたー")

# お届け先画面から移動
my.clickClassButton(browser, "next_step", 0)
browser.save_screenshot("2-6.png")
print("クレジットで払うぞー")

# 支払い方法選択
my.clickClassButton(browser, "next_step", 0)
browser.save_screenshot("2-7.png")
print("注文確認したぞー")

# クレジットカード情報入力（初回購入時のみ）
my.inputCredit(browser, month, year, num, code, 0)

# 購入ボタンを押す
my.clickIdButton(browser, "checkout_btn", 0)
browser.save_screenshot("2-8.png")
print("買ったー")