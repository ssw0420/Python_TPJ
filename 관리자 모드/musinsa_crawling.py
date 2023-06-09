##############################################################################################################################
"""
--- 프로그램 설명 ---
무신사 사이트에서 남성 옷에 대한 정보를 크롤링하여 csv 파일에 저장하는 프로그램

--- 상의 ---
전체 제품 검색창을 이용할 시에는 상의 전체나 하의 전체 사이트에서 검색

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

--- 하의 ---
하의 전체 : https://www.musinsa.com/categories/item/003
하의 데님 팬츠 : https://www.musinsa.com/categories/item/003002
하의 트레이닝/조거팬츠 : https://www.musinsa.com/categories/item/003004
하의 레깅스 : https://www.musinsa.com/categories/item/003005
하의 기타 바지 : https://www.musinsa.com/categories/item/003006
하의 코튼 팬츠 : https://www.musinsa.com/categories/item/003007
하의 슈트 팬츠/슬랙스 : https://www.musinsa.com/categories/item/003008
하의 숏팬츠 : https://www.musinsa.com/categories/item/003009
하의 점프슈트/오버올 : https://www.musinsa.com/categories/item/003010

--- 스포츠 ---
스포츠 상의 : https://www.musinsa.com/categories/item/017016
스포츠 하의 : https://www.musinsa.com/categories/item/017020


"""
##############################################################################################################################
##############################################################################################################################
"""
--- 검색할 옷 종류 ---
상세 검색창을 이용할 때 사용

상의
	봄
	스트릿 :  여름,스트릿,긴소매 + 여름,스트릿,반소매 (봄, 스트릿 시에 표본 수가 적어 얇은 여름원단에 긴소매,반소매를 합침)
	캐주얼 : 여름,캐주얼,긴소매 + 여름,캐주얼,반소매
	포멀 : 여름,포멀,긴소매 +여름,포멀,반소매
	스포츠 : 스포츠,아노락 + 스포츠,스웻셔츠 +스포츠,반소매
 
	여름
	스트릿 : 여름,스트릿,반소매
	캐주얼 : 여름,캐주얼,반소매
	포멀 : 여름,포멀,반소매
	스포츠 : 스포츠,아노락 + 스포츠,스웻셔츠,반소매 +스포츠,반소매

	가을
	스트릿 : 가을,스트릿,긴소매
	캐주얼 : 가을,캐주얼,긴소매
	포멀 : 가을,포멀,긴소매,셔츠 + 가을,포멀,긴소매,터틀넥 + 니트,포멀,긴소매
	스포츠 : 스포츠,아노락 + 스포츠,스웻셔츠,긴소매 

	겨울
	스트릿 : 겨울,스트릿,긴소매
	캐주얼 : 겨울,캐주얼,긴소매
	포멀 : 겨울,포멀,긴소매,셔츠 + 겨울,포멀,긴소매,터틀넥 + 니트,포멀,긴소매
	스포츠 : 스포츠,아노락 + 스포츠,스웻셔츠,긴소매 


하의
	봄
	스트릿 : 여름,스트릿
	캐주얼 : 여름,캐주얼
	포멀 : 치노,포멀 + 슬렉스,포멀 + 데님,포멀
	스포츠 : 트레이닝	
 
	여름
	스트릿 : 여름,스트릿
	캐주얼 : 여름,캐주얼
	포멀 : 치노,포멀 + 슬렉스,포멀 + 데님,포멀
	스포츠 : 트레이닝

	가을
	스트릿 : 겨울,스트릿
	캐주얼 : 겨울,캐주얼
	포멀 : 치노,포멀,긴바지+ 슬렉스,포멀,긴바지 + 데님,포멀,긴바지
	스포츠 : 트레이닝,긴바지

	겨울
	스트릿 :  겨울,스트릿
	캐주얼 : 겨울,캐주얼
	포멀 : 치노,포멀,긴바지 + 슬렉스,포멀,긴바지 + 데님,포멀,긴바지
	스포츠 : 트레이닝,긴바지


"""
##############################################################################################################################

##############################################################################################################################
"""
--- 참고 내용 ---

usf-8에서 excel로 csv파일 확인 시 한글이 깨지면 encoding 할 때 utf-8-sig 사용


--- 라이브러리 호출 ---

csv -> csv 파일 활용
from selenium.webdriver.common.by import By -> 정보를 가져오기 위함
from selenium.webdriver.common.keys import Keys -> 키 작동을 위함
time -> 오류 방지를 위한 대기 시간
from selenium import webdriver -> 크롬 작동
os -> 이미지 저장 폴더 설정
requests -> 이미지 파일 저장
Image -> 이미지 파일 크기 조정
"""
##############################################################################################################################

##############################################################################################################################
"""
--- 변수 명 ---

image_folder, image_resize_folder, csv_folder : 경로 설정
browser : 크롤링 링크 지정
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
page_input : 페이지 입력
count_page : 총 페이지 개수 설정

i : for 문 작동
k : for 문 페이지 식별

m_index : 고유 번호 (0)
m_product : 제품 명 (베츠 어센틱 맨투맨 그레이)
m_brand : 브랜드 명 (이벳필드)
m_price : 가격 (50000)
m_style : 스타일 (댄디)
m_weather : 계절 (봄)
m_image : 이미지 파일
m_link : 링크 호출
product_link : 제품 상세 링크
original_price : 원래 가격
discount_price : 할인 가격


brand : 브랜드 정보 저장
product : 제품 정보 저장
price_text : 가격 정보 저장
price_list : 가격 정보 분리


field : 행 이름
writer : csv 작성


"""
##############################################################################################################################
# 라이브러리 선언
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
import os
import requests
from PIL import Image

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
    browser.maximize_window() # 이미지 불러올 떄 전체화면을 해야 오류가 생기지 않음

    # 남성 옷으로 한정 -> 버튼 클릭
    man = browser.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/button[2]")
    man.click()
    time.sleep(2)

    return browser


def start_m():
    # 프로그램 작동
    search = 1
    # 검색창 이용 여부 확인
    use_search = int(input('검색창 이용 (0 - 검색창 미사용 // 1 - 검색창 사용) : '))

    # 0 입력 시 전체 검색창에서 내용을 검색
    # 1 입력 시 상세 검색창에서 내용을 검색

    if use_search == 1:
        search = int(input('검색창 선택 (0 - 전체 검색창 // 1 - 상세 검색창) : '))
        if search == 0:
            all_search_link()
        elif search == 1:
            # 상세 검색창 작동
            # 전체 검색창을 사용한 경우에는 상세 검색창 사용이 불가능 함
            detail_search_link()
            more_search = int(input('추가로 상세 검색할 횟수 입력 (0 - 미사용) : '))
            for i in range(more_search):
                detail_search_link()

    # 다음 페이지 이동
    page_num = 3
    m_index = 1

    # 전체 검색창 이용시 search 0 반환, 상세 검색창 이용시 search 1 반환
    return page_num, m_index, search

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
def next_page(page_num, search, count_page, page_input) :
    try : # 다음 페이지 클릭이 가능한 경우
        # 탐색할 페이지가 한 페이지 목록을 넘지 않는 경우
        if page_input == count_page:
            browser.close()
            exit()
        
        if search == 0:
            page = browser.find_element(By.XPATH, "//*[@id='goodsList']/div[1]/div/div/a[{}]".format(page_num)) # 다음 페이지로 이동

        elif search == 1:
            page = browser.find_element(By.XPATH, "//*[@id='goods_list']/div[2]/div[1]/div/div/a[{}]".format(page_num)) # 다음 페이지로 이동
        
        page.click()
        time.sleep(2)
        page_num += 1 # 페이지 숫자 증가
        count_page += 1 # 현재 페이지 수 카운트 증가

        if page_num == 14: # 페이지 10(마지막 페이지)까지 이동 하였을 때 다음 페이지 목록으로 이동
            page_num = 3 # page_num을 3으로 초기화 시킴 (해당 페이지 목록의 1 페이지)
    
    except : # 페이지 목록이 끝까지 이동을 하여 다음 페이지 클릭이 불가능한 경우
        browser.close()
        exit()
    
    return page_num, count_page

# 무신사 사이트에서 이미지 파일을 가져올 때는 페이지를 끝까지 내리는 것이 아니라, 특정 부분을 나눠서 내려야 정상적으로 로딩이 됨
def scroll_page() :
    body = browser.find_element(By.CSS_SELECTOR, 'body')
    for _ in range (10):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
    time.sleep(2)

# 이미지 찾기 함수
def image_search(i, k):
    img_src = m_image[0].get_attribute("src") # 이미지 형태로 가져옴
    response = requests.get(img_src)
    # 이미지를 저장할 때는 'byte'로 '작성(w)'해야함 -> wb로 이미지 파일 생성
    with open(f"C:\\파이썬 1조\\하의 목록\\summer_street\\{i+k}.jpg", "wb") as f:
        f.write(response.content) #.content를 사용하여 byte 단위의 데이터를 있는 그대로 가져옴

# 이미지 크기 변환
def image_resize(i, k):
    img = f"C:\\파이썬 1조\\하의 목록\\summer_street\\{i+k}.jpg"
    img_re = Image.open(img).convert('RGB')
    img_re = img_re.resize((125, 150)) # 이미지 파일 크기 조정
    img_re.save(f"C:\\파이썬 1조\\하의 목록\\summer_street\\resize\\{i+k}.jpg")


##############################################################################################################################
# 프로그램 작동
# 여름 스트릿 코드

browser = web_crawling()
page_num, m_index, search = start_m()
image_folder = 'C:\\파이썬 1조\\하의 목록\\summer_street' # 폴더 설정
if not os.path.isdir(image_folder): # 폴더가 존재하는지 확인
    os.mkdir(image_folder) # 존재하지 않으면 해당 폴더 생성

image_resize_folder = 'C:\\파이썬 1조\\하의 목록\\summer_street\\resize' # 폴더 설정
if not os.path.isdir(image_resize_folder): # 폴더가 존재하는지 확인
    os.mkdir(image_resize_folder) # 존재하지 않으면 해당 폴더 생성

csv_folder = 'C:\\파이썬 1조\\하의 목록\\csv 파일' # 폴더 설정
if not os.path.isdir(csv_folder):
    os.mkdir(csv_folder)
k = 0 # 이미지 저장을 위한 변수

# csv 파일을 생성하거나 열음
with open('C:\\파이썬 1조\\하의 목록\\csv 파일\\summer_street.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    field = ['브랜드', '제품명', '원래 가격', '할인 가격', '스타일', '계절', '링크']  # 필드 이름 수정
    writer = csv.DictWriter(csvfile, fieldnames=field)
    writer.writeheader()

    count_page = 1 # 현재 페이지 카운트
    # 페이지 입력
    page_input = int(input("검색할 페이지 수 입력 : "))
    page_input += 1
    while(True):
        page_num, count_page = next_page(page_num, search, count_page, page_input) # 페이지 선택 후 다음 페이지로 이동

        scroll_page()

        for i in range (1, 91):
            m_brand = browser.find_elements(By.XPATH, f"//*[@id='searchList']/li[{i}]/div/div[2]/p[1]/a") # 브랜드 호출
            m_product = browser.find_elements(By.XPATH, f"//*[@id='searchList']/li[{i}]/div/div[2]/p[2]/a") # 상품명 호출
            m_price = browser.find_elements(By.XPATH, f"//*[@id='searchList']/li[{i}]/div/div[2]/p[3]") # 가격 호출
            m_link = browser.find_elements(By.XPATH, f"//*[@id='searchList']/li[{i}]/div/div[1]/a") # 링크 호출
            m_style = "스트릿"
            m_weather = "여름"
            product_link = m_link[0].get_attribute("href") # m_link를 링크 형태로 변환


            # 텍스트 추출 (브랜드, 제품명, 가격)
            brand = m_brand[0].text if len(m_brand) > 0 else ''
            product = m_product[0].text if len(m_product) > 0 else ''
            price_text = m_price[0].text if len(m_price) > 0 else ''
            price_list = price_text.split()

            original_price = ''
            discount_price = ''

            # 가격 정보 분리 (원래 가격, 할인 가격)
            if len(price_list) >= 2:
                original_price = price_list[0]
                discount_price = price_list[1]
            elif len(price_list) == 1:
                original_price = price_list[0]
        
            # CSV 파일에 쓰기
            writer.writerow({'브랜드': brand, '제품명': product, '원래 가격': original_price, '할인 가격': discount_price, '스타일': m_style, '계절': m_weather, '링크' : product_link})


            # 프로그램이 정상적으로 작동되는지 확인
            print("=======================================================")
        
            print(m_index, "번 제품")
            m_index += 1

            print(brand)
            print(product)
            print(original_price)
            print(discount_price)
            print(m_style)
            print(m_weather)

            print("=======================================================")


        for i in range (1, 91):
            m_image = browser.find_elements(By.XPATH, f"//*[@id='searchList']/li[{i}]/div/div[1]/a/img") # 이미지 링크

            # 이미지 저장 및 크기 조정
            image_search(i, k)
            image_resize(i, k)

        # 페이지 이동
        k = k + 90