from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import csv
import re
import codecs

##############################################################################################################################
# 함수 선언

 # 무신사 웹크롤링 프로그램 시작 함수
def web_crawling() :
    URL = input("링크 입력 : ") # 프로그램 상단에 표시된 URL 찾아서 입력
    options = webdriver.ChromeOptions() # 오류 방지
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(options=options)
    browser.get(URL) # URL을 가져옴
    browser.implicitly_wait(5) # 인터넷 연결 시간 대기

    # 남성 옷으로 한정 -> 버튼 클릭
    man = browser.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/button[2]")
    man.click()
    time.sleep(2)

    return browser

# 전체 검색창 이용 함수
# 함수 이용시 상의 전체나 하의 전체의 링크에서만 이용
def all_search_link():
    
    # 검색창 이용
     # element 사용 => 하나의 객체 사용, elements는 list형 사용
    all_search = browser.find_element(By.XPATH, "//*[@id='search_query']") # 전체 검색창을 불러옴
    all_search.click()
    time.sleep(2)

    # 원하는 종류의 옷 검색
    all_search.send_keys(input("전체 검색창에 검색할 내용 입력 : "))
    all_search.send_keys(Keys.ENTER)
    time.sleep(2)

    view_all = browser.find_element(By.XPATH, "/html/body/div[2]/div[3]/section/nav/a[2]")
    view_all.click()
    time.sleep(2)



# 상세 검색창 이용 함수
# 함수 이용시 특정 종류의 제품들이 나열된 링크에서 이용
def detail_search_link():
    detail_search = browser.find_element(By.XPATH, "//*[@id='searchKeyword']") # 세부 검색창을 불러옴
    detail_search.click()
    time.sleep(2)

    detail_search.send_keys(input("상세 검색창에 검색할 내용 입력 : "))
    detail_search.send_keys(Keys.ENTER)
    time.sleep(2)


# 다음 페이지로 이동하는 함수
def next_page(page_num) :
    try : # 다음 페이지 클릭이 가능한 경우
        page = browser.find_element(By.XPATH, "//*[@id='goods_list']/div[2]/div[1]/div/div/a[{}]".format(page_num)) # 다음 페이지로 이동
        page.click()
        time.sleep(2)
    except : # 다음 페이지 클릭이 불가능한 경우
        page_num = 0
        return page_num

    page_num += 1 # 페이지 숫자 증가

    if page_num == 2: # 페이지 10(마지막 페이지)까지 이동 하였을 때 다음 페이지 목록으로 이동
        page_num = 4 # page_num을 4로 초기화 시킴 (해당 페이지 목록의 1 페이지)
    
    return page_num

# 이미지 파일을 가져올 때는 페이지를 끝까지 내리는 것이 아니라, 특정 부분을 나눠서 내려야 정상적으로 로딩이  됨
# def scroll_page() :
#     body = browser.find_element(By.CSS_SELECTOR, 'body')
#     for i in range (5):
#         body.send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)
##############################################################################################################################
# 프로그램 작동

browser = web_crawling()

# 검색창 이용 여부 확인
use_search = int(input('검색창 이용 (0 - 검색창 미사용 // 1 - 검색창 사용) :'))

# 0 입력 시 전체 검색창에서 내용을 검색
# 1 입력 시 상세 검색창에서 내용을 검색

if use_search == 1:
    search = int(input('검색창 선택 (0 - 전체 검색창 // 1 - 상세 검색창) :'))
    if search == 0:
        all_search_link()
    elif search == 1:
        detail_search_link()

# 상세 검색창 작동
more_search = int(input('추가로 상세 검색할 횟수 입력 (0 - 미사용) : '))
for i in range(more_search):
    detail_search_link()

# 다음 페이지 이동
page_num = 4
m_index = 1

# CSV 파일을 쓰기 모드로 열고 필드 이름을 지정
# 개행 문자 처리를 하기 위해 newline='' 사용
# csvfile 변수에 연결하여 파일 작업 수행을 위해  'as csvfile' 사용
# DictWriter를 사용하여 csv파일에 기록할 수 있도록 함
with open('fashion_receive.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    fieldnames = ['브랜드', '제품명', '원래 가격', '할인 가격']  # 필드 이름 수정
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # 헤더를 작성
    writer.writeheader()

    # 페이지 번호 초기화
    page_num = 1

    while True:
        # 다음 페이지 번호를 가져오기
        page_num = next_page(page_num)

        # 각 제품에 대해 정보 수집
        for i in range(1, 91):
            # 브랜드, 제품명, 가격 요소 가져오기
            # 요소를 찾기 위해 XPATH 사용
            # 웹 페이지를 조작하기 위해 browser 사용
            # 'find_elements' 메서드를 사용하여 XPATH에 해당하는 요소를 가져옴 
            m_brand = browser.find_elements(By.XPATH, f"//*[@id='searchList']/li[{i}]/div/div[2]/p[1]/a")
            m_product = browser.find_elements(By.XPATH, f"//*[@id='searchList']/li[{i}]/div/div[2]/p[2]/a")
            m_price = browser.find_elements(By.XPATH, f"//*[@id='searchList']/li[{i}]/div/div[2]/p[3]")

            # 스크롤 처리
            # scroll_page()

            print("=======================================================")
            print(i, "번 제품")

            # 요소에서 텍스트 추출 (브랜드, 제품명, 가격)
            # 각 요소가 존재하면 할당, 없으면 빈칸
            brand = m_brand[0].text if len(m_brand) > 0 else ''
            product = m_product[0].text if len(m_product) > 0 else ''
            price_text = m_price[0].text if len(m_price) > 0 else ''
            price_list = price_text.split()
            # 원래 가격과 할인 가격을 빈문자열로 초기화
            original_price = ''
            discount_price = ''

            # 가격 정보 분리
            # 가격 정보가 두개 이상이면 원래가격과 할인가격을 분리해서 리스트 저장
            if len(price_list) >= 2:
                original_price = price_list[0]
                discount_price = price_list[1]
            # 가격 정보가 하나이면 원래가격에만 리스트 저장
            elif len(price_list) == 1:
                original_price = price_list[0]

            # CSV 파일에 쓰기
            writer.writerow({'브랜드': brand, '제품명': product, '원래 가격': original_price, '할인 가격': discount_price})
            
            #출력
            print(brand)
            print(product)
            print(original_price)
            print(discount_price)

            print("=======================================================")

        # 마지막 페이지면 반복문 종료
        if page_num == 0:
            break


browser.close
