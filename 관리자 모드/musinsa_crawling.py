##############################################################################################################################
"""
--- 프로그램 설명 --- => 임의로 수정 금지
무신사 사이트에서 남성 옷에 대한 정보를 크롤링하여 csv 파일에 저장하는 프로그램

각 사이트에서 브랜드, 제품명, (세일이 적용된) 가격, 상품 종류를 가져옴
아우터는 프로젝트 진행 상황에 따라 추가


--- 상의 --- => 필요 시 업데이트 (2023.05.06)
전체 제품 검색창을 이용할 시에는 상의 전체나 하의 전체 사이트에서 검색하면 됨

상의 전체 : https://www.musinsa.com/categories/item/001
상의 반소매 티셔츠 : https://www.musinsa.com/categories/item/001001
상의 셔츠/블라우스 : https://www.musinsa.com/categories/item/001002
상의 피케/카라 티셔츠 : https://www.musinsa.com/categories/item/001003
상의 후드 티셔츠 : https://www.musinsa.com/categories/item/001004
상의 맨투맨/스웨트셔츠 : https://www.musinsa.com/categories/item/001005
상의 니트/스웨터 : https://www.musinsa.com/categories/item/001006
상의 기타 : https://www.musinsa.com/categories/item/001008
상의 긴소매 티셔츠 : https://www.musinsa.com/categories/item/001010
상의 민소매 티셔츠 : https://www.musinsa.com/categories/item/001011

--- 하의 --- => 필요 시 업데이트 (2023.05.06)
하의 전체 : https://www.musinsa.com/categories/item/003
하의 데님 팬츠 : https://www.musinsa.com/categories/item/003002
하의 트레이닝/조거팬츠 : https://www.musinsa.com/categories/item/003004
하의 레깅스 : https://www.musinsa.com/categories/item/003005
하의 기타 바지 : https://www.musinsa.com/categories/item/003006
하의 코튼 팬츠 : https://www.musinsa.com/categories/item/003007
하의 슈트 팬츠/슬랙스 : https://www.musinsa.com/categories/item/003008
하의 숏팬츠 : https://www.musinsa.com/categories/item/003009
하의 점프슈트/오버올 : https://www.musinsa.com/categories/item/003010

--- 스포츠 --- => 필요 시 업데이트 (2023.05.06)
스포츠 상의 : https://www.musinsa.com/categories/item/017016
스포츠 하의 : https://www.musinsa.com/categories/item/017020


"""
##############################################################################################################################
##############################################################################################################################
"""
--- 검색할 옷 종류 --- => 자료조사 인원이 브랜치를 따로 만들어서 업데이트 바람 (2023.05.07)
상세 검색창을 이용할 때 사용

아래는 표기 예시
여름 - 댄디(스타일 구분 불가시 미작성) - 상의 셔츠/블라우스 - 린넨 셔츠


"""
##############################################################################################################################

##############################################################################################################################
"""
--- 참고 내용 --- => 필요 시 업데이트 (2023.05.06)

usf-8에서 excel로 csv파일 확인 시 한글이 깨지면 encoding 할 때 utf-8-sig 사용



--- 라이브러리 호출 ---  => 필요 시 업데이트 (2023.05.06)

pandas -> csv 파일 활용
re -> 특수기호 같은 문자 필터링 => (필요 없을 시 삭제할 예정)
csv -> csv 파일 활용
from selenium.webdriver.common.by import By -> 정보를 가져오기 위함
from selenium.webdriver.common.keys import Keys -> 키 작동을 위함
time -> 오류 방지를 위한 대기 시간
from selenium import webdriver -> 크롬 작동
"""
##############################################################################################################################

##############################################################################################################################
"""
--- 변수 명 --- => 필요 시 업데이트 (2023.05.08)
변수 추가 시, 식별 가능한 단어 사용

browser : 사용할 링크 설정
page : 웹 사이트 페이지 변화
man : 남성 옷으로 설정
use_search : 검색창 이용 여부
search : 검색창 선택
all_search : 전체 검색
detail_search : 상세 검색
more_search : 추가 검색
view_all : 전체 제품 보기
page_num : 페이지 클릭
page : 페이지

i : for 문 작동

m_index : 고유 번호 (0)
m_product : 제품 명 (베츠 어센틱 맨투맨 그레이)
m_brand : 브랜드 명 (이벳필드)
m_price : 가격 (50000)
m_sets : 상의 하의 구분
m_type : 상품의 종류 (맨투맨, 셔츠, 티셔츠, 반바지, ...)
m_style : 스타일 (댄디)
m_weather : 계절 (봄)


musinsa_df : 무신사 데이터프레임


row : 행
column : 열
data : 파일 정보


"""
##############################################################################################################################
# 라이브러리 선언
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import csv
import re

##############################################################################################################################
# 함수 선언
# 전역 변수
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


def start_musinsa():
    # 프로그램 작동

    # 검색창 이용 여부 확인
    use_search = int(input('검색창 이용 (0 - 검색창 미사용 // 1 - 검색창 사용) : '))

    # 0 입력 시 전체 검색창에서 내용을 검색
    # 1 입력 시 상세 검색창에서 내용을 검색

    if use_search == 1:
        search = int(input('검색창 선택 (0 - 전체 검색창 // 1 - 상세 검색창) : '))
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

    return page_num, m_index

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

    if page_num == 14: # 페이지 10(마지막 페이지)까지 이동 하였을 때 다음 페이지 목록으로 이동
        page_num = 4 # page_num을 4로 초기화 시킴 (해당 페이지 목록의 1 페이지)
    
    return page_num

#이미지 파일을 가져올 때는 페이지를 끝까지 내리는 것이 아니라, 특정 부분을 나눠서 내려야 정상적으로 로딩이 됨
def scroll_page() :
    body = browser.find_element(By.CSS_SELECTOR, 'body')
    for i in range (50):
        body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)



##############################################################################################################################
# 프로그램 작동
browser = web_crawling()
page_num, m_index = start_musinsa()

while(True):
    page_num = next_page(page_num) # 페이지 선택 후 다음 페이지로 이동
    scroll_page() # 이미지를 불러오기 위해서는 화면 최하단으로 이동하는 것이 아니라 직접 스크롤 하면서 내려가야 함

    for i in range (1, 91):
        m_brand = browser.find_elements(By.XPATH, f"//*[@id='searchList']/li[{i}]/div/div[2]/p[1]/a") # 브랜드 호출
        m_product = browser.find_elements(By.XPATH, f"//*[@id='searchList']/li[{i}]/div/div[2]/p[2]/a") # 상품 명 호출
        m_price = browser.find_elements(By.XPATH, f"//*[@id='searchList']/li[{i}]/div/div[2]/p[3]") # 가격 호출
        
        print("=======================================================")
        
        print(m_index, "번 제품")
        m_index += 1
        if len(m_brand) > 0:
            print(m_brand[0].text)
    
        if len(m_product) > 0:
            print(m_product[0].text)

        if len(m_price) > 0:
            print(m_price[0].text)
        
        print("=======================================================")

    if page_num == 0:
        break


browser.close() # 종료


##############################################################################################################################

# 미구현
# for i in range (30):
#     m_brand = browser.find_elements(By.XPATH, f"//*[@id='searchList']/li[{i}]/div/div[2]/p[1]/a")
#     m_product = browser.find_elements(By.XPATH, f"//*[@id='searchList']/li[{i}]/div/div[2]/p[2]/a")

#     print(m_brand[i])
#     print(m_product[i])


    # # 끝까지 스크롤
    #     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # # 대기 1초 (로딩으로 인해 알맞는 초 조절)
    #     time.sleep(1)

    # # 스크롤 길이 비교로 끝까지 갔는지 확인
    #     new_height = browser.execute_script("return document.body.scrollHeight")
    #     if new_height == last_height:
    #         break
    #     last_height = new_height



##############################################################################################################################



# for i in range(1, 10):
#     m_product = browser.find_elements(By.XPATH, "//*[@id='searchList']/li[{}]/div[4]/div[2]/p[2]/a".format(i)) # 제품 명을 가져옴
#     if len(m_product) > 0:
#         print("i: ", i, f"length of name: ", len(m_product),"")
#         print(m_product[0].text) # 출력
##############################################################################################################################
