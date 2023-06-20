# '오.패.추' 사용자 인터페이스 코드
# 'Today_Fashoin_Recommendation' 's User Interface code

import csv  # CSV 파일을 다루기 위한 모듈
import random  # 임의의 추천을 위한 모듈
import os  # 파일 및 경로 관리를 위한 모듈
import webbrowser # 웹 브라우저를 위한 모
import tkinter as tk  # GUI 개발을 위한 모듈
from tkinter import scrolledtext, messagebox, Label  # GUI 요소를 사용하기 위한 모듈
from PIL import ImageTk, Image  # 이미지 처리를 위한 모듈


####################################################### 인터페이스 상의 이미지 출력 구현 함수. 
def show_high_images(images, recommendations, style, season, max_price_low):
    # tkinter 다중 창 인터페이스 구현. main에 위치한 window tk와 다름.
    new_window = tk.Toplevel()  # 새 창 생성
    new_window.title("상의 추천")# 창 이름 설정
    new_window.geometry("1000x700")  # 창 크기 설정

    canvas = tk.Canvas(new_window)  # 캔버스 생성
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(new_window, orient=tk.VERTICAL, command=canvas.yview)  # 스크롤바 생성
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    frame = tk.Frame(canvas)  # 캔버스의 프레임(틀, 공간) 생성
    canvas.create_window((0, 0), window=frame, anchor=tk.NW)

    photo_list = []  # PhotoImage 객체 리스트

    text_label = tk.Label(frame, text="'상품명' 클릭 시 하의 추천", font=("Arial", 12))
    text_label.grid(row=0, column=2, padx=5, pady=5)

    # 랜덤한 10개의 상의 이미지와 추천 정보를 화면에 출력
    for idx, row in enumerate(random.sample(images, 10)):
        brand, name, original_price, sale_price, row_style, row_season, link, image_path = row
        # 행에서 브랜드명, 제품명, 원가격, 할인가격, 스타일, 계절, 주소, 이미지경로 추출

        # 디폴트 가격 표시 = 세일가격으로 설정
        price = sale_price

        # 세일가격이 없을 시 원가격으로 설정
        if sale_price == '':
            price = original_price
         
        # 이미지 로드 및 크기 조정5
        image = Image.open(image_path.strip('"').replace('/', '\\'))  # 이미지 파일 열기
        image = image.resize((150, 150), Image.Resampling.LANCZOS)  # 이미지 크기 조정
        photo = ImageTk.PhotoImage(image)  # 이미지를 Tkinter에서 사용 가능한 형식으로 변환

        # 이미지를 표시하기 위한 레이블
        label = tk.Label(frame, image=photo)
        label.image = photo
        label.grid(row=idx+1, column=0, padx=5, pady=5)

        # 브랜드 표시를 위한 레이
        brand_label = tk.Label(frame, text=brand, font=("Arial", 12))
        brand_label.grid(row=idx+1, column=1, padx=5, pady=5)

        # 의상 이름 표시를 위한 레이블
        name_label1 = tk.Label(frame, text=name, font=("Arial", 12))
        name_label1.grid(row=idx+1, column=2, padx=5, pady=5)

        # 가격 표시를 위한 레이블
        price_label = tk.Label(frame, text=f"{price}", font=("Arial", 12))
        price_label.grid(row=idx+1, column=3, padx=5, pady=5)

        # 링크 표시를 위한 레이블
        link_button = tk.Button(frame, text="링크", font=("Arial", 12), command=lambda link=link: open_link(link))
        link_button.grid(row=idx+1, column=4, padx=5, pady=5)

        # 숨겨진 버튼. 의상 이름(name_lable1)을 클릭 시 하의 추가 추천 인터페이스로 넘어감.
        name_label1.bind("<Button-1>", lambda e, rec=recommendations[idx],st=style, sn=season, mpl=max_price_low: show_additional_recommendations(e,rec,st,sn,mpl))

        photo_list.append(photo)

    # 스크롤바와 캔버스 연결
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))

########################################################## 하의 추가 추천 인터페이스 함수 구현
def show_additional_recommendations(event, recommendation, style, season, max_price_low):
    low_data = []

    # 스포츠 + 계절
    if style == '스포츠' and season == '봄':
        with open('C:\\파이썬 1조\\하의 목록\\csv파일\\스포츠\\spring_training_low.csv', 'r', encoding='utf-8') as file:
            low_data = list(csv.reader(file))
            
    elif style == '스포츠' and season == '여름':
        with open('C:\\파이썬 1조\\하의 목록\\csv파일\\스포츠\\summer_training_low.csv', 'r', encoding='utf-8') as file:
            low_data = list(csv.reader(file))
            
    elif style == '스포츠' and season == '가을':
        with open('C:\\파이썬 1조\\하의 목록\\csv파일\\스포츠\\fall_long_training_low.csv', 'r', encoding='utf-8') as file:
            low_data = list(csv.reader(file))
            
    elif style == '스포츠' and season == '겨울':
        with open('C:\\파이썬 1조\\하의 목록\\csv파일\\스포츠\\winter_long_training_low.csv', 'r', encoding='utf-8') as file:
            low_data = list(csv.reader(file))

    # 포멀 + 계절
    elif style == '포멀' and season == '봄':
        with open('C:\\파이썬 1조\\하의 목록\\csv파일\\포멀\\spring_formal_low.csv', 'r', encoding='utf-8') as file:
            low_data = list(csv.reader(file))
            
    elif style == '포멀' and season == '여름':
        with open('C:\\파이썬 1조\\하의 목록\\csv파일\\포멀\\summer_formal_low.csv', 'r', encoding='utf-8') as file:
            low_data = list(csv.reader(file))
            
    elif style == '포멀' and season == '가을':
        with open('C:\\파이썬 1조\\하의 목록\\csv파일\\포멀\\fall_formal_low.csv', 'r', encoding='utf-8') as file:
            low_data = list(csv.reader(file))
            
    elif style == '포멀' and season == '겨울':
        with open('C:\\파이썬 1조\\하의 목록\\csv파일\\포멀\\winter_formal_low.csv', 'r', encoding='utf-8') as file:
            low_data = list(csv.reader(file))

    # 캐주얼 + 계절
    elif style == '캐쥬얼' and season == '봄':
        with open('C:\\파이썬 1조\\하의 목록\\csv파일\\캐주얼\\spring_casual_low.csv', 'r', encoding='utf-8') as file:
            low_data = list(csv.reader(file))
            
    elif style == '캐쥬얼' and season == '여름':
        with open('C:\\파이썬 1조\\하의 목록\\csv파일\\캐주얼\\summer_casual_low.csv', 'r', encoding='utf-8') as file:
            low_data = list(csv.reader(file))
            
    elif style == '캐쥬얼' and season == '가을':
        with open('C:\\파이썬 1조\\하의 목록\\csv파일\\캐주얼\\fall_casual_low.csv', 'r', encoding='utf-8') as file:
            low_data = list(csv.reader(file))
            
    elif style == '캐쥬얼' and season == '겨울':
        with open('C:\\파이썬 1조\\하의 목록\\csv파일\\캐주얼\\winter_casual_low.csv', 'r', encoding='utf-8') as file:
            low_data = list(csv.reader(file))
            
    else:
        messagebox.showinfo("추천 결과", "해당하는 데이터가 없습니다.")
        return

    # 하의 리스트 초기화
    filtered_low_data = []

    # csv로부터 하의 리스트 값 삽입
    for row in low_data[1:]:
        brand, name, original_price, sale_price, row_style, row_season, link, image_path = row
        # 행에서 브랜드명, 제품명, 원가격, 할인가격, 스타일, 계절, 주소, 이미지경로 추출
        
        # 디폴트 가격 표시 = 세일가격으로 설정
        price = sale_price

        # 세일가격이 없을 시 원가격으로 설정
        if sale_price == '':
            price = original_price

        if price == '':
            continue
        # 현재 price는 문자형이므로 정수형으로 변환할 필요가 있음
        else:
            price = price.replace(',', '')  # 쉼표 제거
            price = price.replace('원', '')  # '원' 제거
            
        price = int(price)  # 가격 비교를 위한 정수로 변환
        
        if season and row_season != season:  # 계절이 입력되었고 현재 행의 계절과 일치하지 않으면 건너뜀
            continue
        if style and row_style != style:  # 스타일이 입력되었고 현재 행의 스타일과 일치하지 않으면 건너뜀
            continue
        if price != None and max_price_low and int(price) > int(max_price_low):  # 최대 가격이 입력되었고 현재 행의 가격이 최대 가격보다 크면 건너뜀
            continue
        elif price == None and max_price_low and int(price) > int(max_price_low):
            continue
        #if max_price and int(price) > int(max_price):  # 최대 가격이 입력되었고 현재 행의 가격이 최대 가격보다 크면 건너뜀
         #   continue        
        filtered_low_data.append(row)  # 조건을 모두 만족하는 행은 filtered_high_data에 추가

    if len(filtered_low_data) == 0:  # 추천된 데이터가 없는 경우
        messagebox.showinfo("추천 결과", "추천 결과가 없습니다.")  # "추천 결과가 없습니다." 메시지 박스 표시

    else:  # 추천된 데이터가 있는 경우
        # filtered_data와 전체 high_data를 인자로하여 show_images 함수 호출하여 이미지와 추천 정보 출력
        show_low_images(filtered_low_data, low_data)

################################################ 인터페이스 하의 이미지 출력 함수 구현
def show_low_images(images, recommendations):
    # tkinter 다중 창 인터페이스 구현. main에 위치한 window tk와 다름.
    new_window = tk.Toplevel()  # 새 창 생성
    new_window.title("하의 추천")# 창 이름 설정
    new_window.geometry("1000x700")  # 창 크기 설정

    canvas = tk.Canvas(new_window)  # 캔버스 생성
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(new_window, orient=tk.VERTICAL, command=canvas.yview)  # 스크롤바 생성
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    frame = tk.Frame(canvas)  # 캔버스의 프레임(틀, 공간) 생성
    canvas.create_window((0, 0), window=frame, anchor=tk.NW)

    photo_list = []  # PhotoImage 객체 리스트
    
    # 랜덤한 10개의 하의 이미지와 추천 정보를 화면에 출력
    for idx, row in enumerate(random.sample(images, 10)):
        brand, name, original_price, sale_price, row_style, row_season, link, image_path = row
        # 행에서 브랜드명, 제품명, 원가격, 할인가격, 스타일, 계절, 주소, 이미지경로 추출

        # 디폴트 가격 표시 = 세일가격으로 설정
        price = sale_price

        # 세일가격이 없을 시 원가격으로 설정
        if sale_price == '':
            price = original_price
               
        # 이미지 로드 및 크기 조정5
        image = Image.open(image_path.strip('"').replace('/', '\\'))  # 이미지 파일 열기
        image = image.resize((150, 150), Image.Resampling.LANCZOS)  # 이미지 크기 조정
        photo = ImageTk.PhotoImage(image)  # 이미지를 Tkinter에서 사용 가능한 형식으로 변환

        # 이미지를 표시하기 위한 레이블
        label = tk.Label(frame, image=photo)
        label.image = photo
        label.grid(row=idx+1, column=0, padx=5, pady=5)

        # 브랜드 표시를 위한 레이
        brand_label = tk.Label(frame, text=brand, font=("Arial", 12))
        brand_label.grid(row=idx+1, column=1, padx=5, pady=5)

        # 의상 이름 표시를 위한 레이블
        name_label1 = tk.Label(frame, text=name, font=("Arial", 12))
        name_label1.grid(row=idx+1, column=2, padx=5, pady=5)

        # 가격 표시를 위한 레이블
        price_label = tk.Label(frame, text=f"{price}", font=("Arial", 12))
        price_label.grid(row=idx+1, column=3, padx=5, pady=5)

        # 링크 표시를 위한 레이블
        link_button = tk.Button(frame, text="링크", font=("Arial", 12), command=lambda link=link: open_link(link))
        link_button.grid(row=idx+1, column=4, padx=5, pady=5)

    # 스크롤바와 캔버스 연결
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))

# 링크를 열기 위한 웹브라우저 함수
def open_link(link):
    webbrowser.open(link)

########################################## 계절, 스타일 (가격과 체형은 자유)을 인터페이스에 입력받는 함수 구현
def get_recommendation(season, style, max_price_high=None, max_price_low=None, body_type=None):

    high_data = []
    ### 스포츠 + 계절 --> 계절별 또는 스타일별 함수 만들 필요
    if style == '스포츠' and season == '봄':
        with open('C:\\파이썬 1조\\상의 목록\\csv파일\\스포츠\\spring_sports_high.csv', 'r', encoding='utf-8') as file:
            high_data = list(csv.reader(file))

    elif style == '스포츠' and season == '여름':
        with open('C:\\파이썬 1조\\상의 목록\\csv파일\\스포츠\\summer_sports_high.csv', 'r', encoding='utf-8') as file:
            high_data = list(csv.reader(file))

    elif style == '스포츠' and season == '가을':
        with open('C:\\파이썬 1조\\상의 목록\\csv파일\\스포츠\\fall_sports_high.csv', 'r', encoding='utf-8') as file:
            high_data = list(csv.reader(file))

    elif style == '스포츠' and season == '겨울':
        with open('C:\\파이썬 1조\\상의 목록\\csv파일\\스포츠\\winter_sports_high.csv', 'r', encoding='utf-8') as file:
            high_data = list(csv.reader(file))

    ### 포멀 + 계절
    if style == '포멀' and season == '봄':
        with open('C:\\파이썬 1조\\상의 목록\\csv파일\\포멀\\spring_formal_high.csv', 'r', encoding='utf-8') as file:
            high_data = list(csv.reader(file))

    elif style == '포멀' and season == '여름':
        with open('C:\\파이썬 1조\\상의 목록\\csv파일\\포멀\\summer_formal_high.csv', 'r', encoding='utf-8') as file:
            high_data = list(csv.reader(file))

    elif style == '포멀' and season == '가을':
        with open('C:\\파이썬 1조\\상의 목록\\csv파일\\포멀\\fall_formal_high.csv', 'r', encoding='utf-8') as file:
            high_data = list(csv.reader(file))

    elif style == '포멀' and season == '겨울':
        with open('C:\\파이썬 1조\\상의 목록\\csv파일\\포멀\\winter_formal_high.csv', 'r', encoding='utf-8') as file:
            high_data = list(csv.reader(file))

    ### 캐주 + 계절
    if style == '캐쥬얼' and season == '봄':
        with open('C:\\파이썬 1조\\상의 목록\\csv파일\\캐주얼\\spring_casual_high.csv', 'r', encoding='utf-8') as file:
            high_data = list(csv.reader(file))

    elif style == '캐쥬얼' and season == '여름':
        with open('C:\\파이썬 1조\\상의 목록\\csv파일\\캐주얼\\summer_casual_high.csv', 'r', encoding='utf-8') as file:
            high_data = list(csv.reader(file))

    elif style == '캐쥬얼' and season == '가을':
        with open('C:\\파이썬 1조\\상의 목록\\csv파일\\캐주얼\\fall_casual_high.csv', 'r', encoding='utf-8') as file:
            high_data = list(csv.reader(file))

    elif style == '캐쥬얼' and season == '겨울':
        with open('C:\\파이썬 1조\\상의 목록\\csv파일\\캐주얼\\winter_casual_high.csv', 'r', encoding='utf-8') as file:
            high_data = list(csv.reader(file))

    if not season or not style:  # 계절 또는 스타일이 입력되지 않은 경우
        recommendation_text.delete('1.0', tk.END)  # recommendation_text 텍스트 위젯 초기화
        recommendation_text.insert(tk.END, "계절과 스타일 입력은 필수!")  # 메세지 출력
        return

    filtered_high_data = []  # 추천된 데이터를 담을 빈 리스트 생성

    # 헤더 부분 제거를 위해 슬라이싱 [1:] 인덱스 1부터 시
    for row in high_data[1:]:
        brand, name, original_price, sale_price, row_style, row_season, link, image_path = row
        # 행에서 브랜드명, 제품명, 원가격, 할인가격, 스타일, 계절, 주소, 이미지경로 추출
        
        # 디폴트 가격 표시 = 세일가격으로 설정
        price = sale_price

        # 세일가격이 없을 시 원가격으로 설정
        if sale_price == '':
            price = original_price

        if price == '':
            continue
        # 현재 price는 문자형이므로 정수형으로 변환할 필요가 있음
        else:
            price = price.replace(',', '')  # 쉼표 제거
            price = price.replace('원', '')  # '원' 제거
            
        price = int(price)  # 가격 비교를 위한 정수로 변환
        
        if season and row_season != season:  # 계절이 입력되었고 현재 행의 계절과 일치하지 않으면 건너뜀
            continue
        if style and row_style != style:  # 스타일이 입력되었고 현재 행의 스타일과 일치하지 않으면 건너뜀
            continue
        if price != None and max_price_high and int(price) > int(max_price_high):  # 최대 가격이 입력되었고 현재 행의 가격이 최대 가격보다 크면 건너뜀
            continue
        elif price == None and max_price_high and int(price) > int(max_price_high):
            continue
        #if max_price and int(price) > int(max_price):  # 최대 가격이 입력되었고 현재 행의 가격이 최대 가격보다 크면 건너뜀
        #   continue
        filtered_high_data.append(row)  # 조건을 모두 만족하는 행은 filtered_high_data에 추가

    if len(filtered_high_data) == 0:  # 추천된 데이터가 없는 경우
        messagebox.showinfo("추천 결과", "추천 결과가 없습니다.")  # "추천 결과가 없습니다." 메시지 박스 표시

    else:  # 추천된 데이터가 있는 경우
        # filtered_data와 전체 high_data를 인자로하여 show_high_images 함수 호출하여 이미지와 추천 정보 출력
        show_high_images(filtered_high_data, high_data, style, season, max_price_low)

################################ 스타일 설명 인터페이스 구현 -> pc 변경 시 파일 경로 변경 필수
def show_system_description():
    top_level = tk.Toplevel(window)  # (위 코드와 동일) 새 창 생성
    top_level.title("시스템 설명")  # 창 제목 설정
    top_level.geometry("800x600")  # 창 크기 설정

    # 스크롤 가능한 프레임 생성
    canvas = tk.Canvas(top_level)  # 캔버스 생성
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(top_level, orient=tk.VERTICAL, command=canvas.yview)  # 스크롤바 생성
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    frame = tk.Frame(canvas)  # 캔버스의 프레임(틀, 공간) 생성
    canvas.create_window((0, 0), window=frame, anchor=tk.NW)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # 스크롤 가능한 텍스트 위젯 생성
    text_path = "C:\\파이썬 1조\\체형+스타일설명\\설명.txt"  # 설명 텍스트 파일의 경로 설정
    image_dir = r"C:\\파이썬 1조\\체형+스타일설명\\데이터과학 스타일설명"

    image_files = os.listdir(image_dir)
    
    with open(text_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # '#'을 구분으로 프레임 나눔
    sections = content.split('#')


    for i, section in enumerate(sections):
        row_frame = tk.Frame(frame)  # 프레임 생성

         # 이미지 표시를 위한 레이블 생성
        if i < len(image_files):
            image_path = os.path.join(image_dir, image_files[i])  # 이미지 파일 경로 설정
            image = Image.open(image_path)
            image = image.resize((150, 150), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            image_label = tk.Label(row_frame, image=photo)
            image_label.image = photo  # 유지하기 위해 참조 유지
            image_label.pack(side=tk.LEFT, padx=10, pady=10)  # 왼쪽에 이미지 레이블 배치

        #스트롤 가능한 텍스트 위젯 생성
        description_text = scrolledtext.ScrolledText(row_frame, width=40, height=7, wrap=tk.WORD, font=("Arial", 12))
        description_text.pack(side=tk.RIGHT, padx=10, pady=10)  # 위젯을 프레임에 배치
        description_text.insert(tk.END, section.strip())  # 섹션 내용을 위젯에 삽입

        row_frame.pack(pady=10)  # 프레임을 스크롤 가능한 프레임에 배치
      
################################################################ 체형 설명 인터페이스 구현
def show_body_type_images():
    top_level = tk.Toplevel(window)  # (위 코드와 동일) 새 창 생성
    top_level.title("체형 사진")  # 창 제목 설정
    top_level.geometry("1000x800")  # 창 크기 설정

    # top_level 프레임(틀, 공간) 생성
    frame = tk.Frame(top_level)
    frame.pack(padx=5, pady=5)  #좌우 및 상하 여백 설정 -> 위젯 주위에 일정한 여백 생성

    # 'body_types.csv' 파일을 열어서 체형 목록 읽기 -> pc 변경 시 파일 경로 변경 필수
    with open("C:\\파이썬 1조\\체형+스타일설명\\body_types.csv", 'r', encoding='utf-8-sig') as file:
        body_type_images = list(csv.reader(file))
        body_type_images = body_type_images[1:]  # 첫 번째 행 제외

        for idx, body_type in enumerate(body_type_images):
            name, image_path, description = body_type

            # 이미지 로드 및 크기 조정
            image = Image.open(image_path.strip('"'))  # 이미지 파일 열기
            image = image.resize((125, 150), Image.Resampling.LANCZOS)  # 이미지 크기 조정
            photo = ImageTk.PhotoImage(image)  # 이미지를 Tkinter에서 사용 가능한 형식으로 변환

            # 이미지를 표시하기 위한 레이블
            label = tk.Label(frame, image=photo)
            label.image = photo
            label.grid(row=idx, column=0, padx=5, pady=5)

            # 체형 이름 표시를 위한 레이블
            text_label1 = tk.Label(frame, text=name, font=("Arial", 12))
            text_label1.grid(row=idx, column=1, padx=5, pady=5)

            # 체형 설명 표시를 위한 레이블
            text_label2 = tk.Label(frame, text=description, font=("Arial", 12))
            text_label2.grid(row=idx, column=2, padx=5, pady=5)

# 메인 윈도우 창
window = tk.Tk()
window.title("오.패.추")
window.geometry("800x600")
window.configure(bg="#F0F0F0")

# 윈도우창 타이틀 라벨
title_label = Label(window, text="오.패.추", font=("Arial", 24, "bold"), bg="#F0F0F0")
title_label.pack(pady=10)

# 인터페이스 입력 부분 구현
input_frame = tk.Frame(window, bg="#F0F0F0")
input_frame.pack(pady=10)

# 게절 입력창
season_label = tk.Label(input_frame, text="계절", font=("Arial", 12), bg="#F0F0F0")
season_label.grid(row=0, column=0, padx=5, pady=5)

season_entry = tk.Entry(input_frame, width=20, font=("Arial", 12))
season_entry.grid(row=0, column=1, padx=5, pady=5)

# 스타일 입력창
style_label = tk.Label(input_frame, text="스타일", font=("Arial", 12), bg="#F0F0F0")
style_label.grid(row=1, column=0, padx=5, pady=5)

style_entry = tk.Entry(input_frame, width=20, font=("Arial", 12))
style_entry.grid(row=1, column=1, padx=5, pady=5)

# 상의 최대 가격 입력창
max_price_high_label = tk.Label(input_frame, text="상의 최대 가격", font=("Arial", 12), bg="#F0F0F0")
max_price_high_label.grid(row=2, column=0, padx=5, pady=5)

max_price_high_entry = tk.Entry(input_frame, width=20, font=("Arial", 12))
max_price_high_entry.grid(row=2, column=1, padx=5, pady=5)

# 하의 최대 가격 입력창
max_price_low_label = tk.Label(input_frame, text="하의 최대 가격", font=("Arial", 12), bg="#F0F0F0")
max_price_low_label.grid(row=3, column=0, padx=5, pady=5)

max_price_low_entry = tk.Entry(input_frame, width=20, font=("Arial", 12))
max_price_low_entry.grid(row=3, column=1, padx=5, pady=5)

# 추천 받기 버튼 구현
recommend_button = tk.Button(window, text="추천받기", command=lambda: get_recommendation(season_entry.get(), style_entry.get(), max_price_high_entry.get(), max_price_low_entry.get()), font=("Arial", 12))
recommend_button.pack()

recommendation_text = scrolledtext.ScrolledText(window, width=60, height=10, wrap=tk.WORD, font=("Arial", 12))
recommendation_text.pack()

# 설명 인터페이스를 열기 위한 버튼 구현
description_button = tk.Button(window, text="설명", command=show_system_description, font=("Arial", 12))
description_button.pack(side=tk.RIGHT, padx=10, pady=10, anchor=tk.SE)

# 체형 인터페이스를 열기 위한 버튼 구현
body_type_button = tk.Button(window, text="체형 사진", command=show_body_type_images, font=("Arial", 12))
body_type_button.pack(side=tk.LEFT, padx=10, pady=10, anchor=tk.SW)

window.mainloop()
