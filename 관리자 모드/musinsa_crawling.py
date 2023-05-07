###############################################################
"""
--- 프로그램 설명 --- => 임의로 수정 금지
무신사 사이트에서 남성 옷에 대한 정보를 크롤링하여 csv 파일에 저장하는 프로그램

각 사이트에서 브랜드, 제품명, (세일이 적용된) 가격, 상품 종류를 가져옴
아우터는 프로젝트 진행 상황에 따라 추가


--- 상의 --- => 필요 시 업데이트 (2023.05.06)
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
###############################################################

###############################################################
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
###############################################################

###############################################################
"""
--- 변수 명 --- => 필요 시 업데이트 (2023.05.06)
변수 추가 시, 식별 가능한 단어 사용

page : 웹 사이트 페이지 변화


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
###############################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import csv
import re

# 무신사 상의 사이트 연결
URL = input() # 상의 전체
browser = webdriver.Chrome() # 크롬으로 작동
browser.get(URL) # URL을 가져옴
browser.implicitly_wait(5) # 인터넷 연결 시간 대기

# 남성 옷으로 한정 -> 버튼 클릭
man = browser.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[13]/button[2]")
man.click()
time.sleep(2)

# 검색창 
search = browser.find_element(By.XPATH, "//*[@id='search_query']") # element 사용 => 하나의 객체 사용, elements는 list형 사용
search.click()
time.sleep(2)

# 원하는 종류의 옷 검색
search.send_keys('린넨 셔츠')
search.send_keys(Keys.ENTER)

for i in range(1, 10):
    m_product = browser.find_elements(By.XPATH, "//*[@id='searchList']/li[{}]/div[4]/div[2]/p[2]/a".format(i)) # 제품 명을 가져옴
    if len(m_product) > 0:
        print("i: ", i, f"length of name: ", len(m_product),"")
        print(m_product[0].text) # 출력

browser.close() # 종료