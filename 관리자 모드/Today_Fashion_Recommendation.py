# '오.패.추' 사용자 인터페이스 코드
# 'Today_Fashoin_Recommendation' 's User Interface code

import csv  # CSV 파일을 다루기 위한 모듈
import random  # 임의의 추천을 위한 모듈
import os  # 파일 및 경로 관리를 위한 모듈
import tkinter as tk  # GUI 개발을 위한 모듈
from tkinter import scrolledtext, messagebox, Label  # GUI 요소를 사용하기 위한 모듈
from PIL import ImageTk, Image  # 이미지 처리를 위한 모듈

# 인터페이스 이미지 출력 구현 함수. 
def show_images(images, recommendations):
    # tkinter 다중 창 인터페이스 구현. main에 위치한 window tk와 다름.
    new_window = tk.Toplevel()  # 새 창 생성
    new_window.title("상의 추천")# 창 이름 설정
    new_window.geometry("800x600")  # 창 크기 설정

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
    text_label.grid(row=0, column=3, padx=5, pady=5)
    
    # 이미지와 추천 정보를 화면에 출력
    for idx, row in enumerate(images):
        name, style, price, season, image_path = row

        # 이미지 로드 및 크기 조정
        image = Image.open(image_path.strip('"'))  # 이미지 파일 열기
        image = image.resize((150, 150), Image.Resampling.LANCZOS)  # 이미지 크기 조정
        photo = ImageTk.PhotoImage(image)  # 이미지를 Tkinter에서 사용 가능한 형식으로 변환

        # 이미지를 표시하기 위한 레이블
        label = tk.Label(frame, image=photo)
        label.image = photo
        label.grid(row=idx+1, column=0, padx=5, pady=5)

        # 의상 이름 표시를 위한 레이블
        recommendation_label1 = tk.Label(frame, text=name, font=("Arial", 12))
        recommendation_label1.grid(row=idx+1, column=1, padx=5, pady=5)

        # 가격 표시를 위한 레이블
        price_label = tk.Label(frame, text=f"{price}원", font=("Arial", 12))
        price_label.grid(row=idx+1, column=2, padx=5, pady=5)

        recommendation_label1.bind("<Button-1>", lambda e, rec=recommendations[idx]: show_additional_recommendations(e, rec))

        photo_list.append(photo)

    canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))

# 하의 추가 추천 인터페이스 함수 구현
def show_additional_recommendations(event, recommendation):

##### csv 파일 형식 변환 확인 필수 -> 이미지 저장 csv 파일 형식이랑 다름 #######
    # 'result2.csv'(하의 데이터를 저장한) 파일을 열어서 하의 목록 읽기
    with open('C:\\Python\\팀플 테스트\\result2.csv', 'r', encoding='utf-8') as file:
        additional_recommendations = list(csv.reader(file))
        random_recommendations = random.sample(additional_recommendations, 3)


    top_level = tk.Toplevel(window)  # 'window'를 기반(부모 창)으로 지정하는 Toplevel 위젯을 top_level변수에 할당하여 새로운 창 생성
    top_level.title("하의 추천")  # 창 이름 설정
    top_level.geometry("800x600")  # 창 크기 설정

    #top_level 프레임(틀, 공간) 생성
    frame = tk.Frame(top_level)
    frame.pack(padx=5, pady=5)  #좌우 및 상하 여백 설정 -> 위젯 주위에 일정한 여백 생성


    # 하의를 랜덤하게 3개 표시
    for idx, recommendation in enumerate(random_recommendations):
        name, style, price, season, image_path = recommendation

        
        # 이미지를 열고 크기를 조정
        try:
            image = Image.open(image_path.strip('"'))
            image = image.resize((150, 150), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)

        # 이미지를 표시하는 나머지 코드. 만약 result2.csv에서 파일 읽기 오류 시 3가지가 불러지지 않을 경우 막는 코
        # 이미지가 3개 출력이 되지 않을 경우 자동 창 닫기
        except FileNotFoundError:
            print(f"다시 클릭해 주세요")
            top_level.destroy()  # top_level 창 닫기
            return
        
        #이미지를 표시할 라벨을 생성하고 그리드에 배치
        label = tk.Label(frame, image=photo)
        label.image = photo
        label.grid(row=idx, column=0, padx=5, pady=5, sticky="w")

        # 아이템 이름을 표시할 라벨을 생성하고 그리드에 배치
        text_label1 = tk.Label(frame, text=name, font=("Arial", 12))
        text_label1.grid(row=idx, column=1, padx=5, pady=5)

        # 아이템 가격을 표시할 라벨을 생성하고 그리드에 배치
        text_label2 = tk.Label(frame, text=f"{price}원", font=("Arial", 12))
        text_label2.grid(row=idx, column=2, padx=5, pady=5)



# 계절, 스타일 (가격과 체형은 자유)을 인터페이스에 입력받는 함수 구현
def get_recommendation(season, style, max_price=None, body_type=None):

    # 'result.csv' 파일을 읽어 clothes_data 리스트로 데이터 저장    
    with open('C:\\Python\\팀플 테스트\\result.csv', 'r', encoding='utf-8') as file:
        clothes_data = list(csv.reader(file))

    if not season or not style:  # 계절 또는 스타일이 입력되지 않은 경우
        recommendation_text.delete('1.0', tk.END)  # recommendation_text 텍스트 위젯 초기화
        recommendation_text.insert(tk.END, "계절과 스타일 입력은 필수!")  # 메세지 출력
        return

    filtered_data = []  # 추천된 데이터를 담을 빈 리스트 생성
    for row in clothes_data:
        name, row_style, price, row_season, image_path = row  # 행에서 의상 이름, 스타일, 가격, 계절, 이미지 경로 추출
        if season and row_season != season:  # 계절이 입력되었고 현재 행의 계절과 일치하지 않으면 건너뜀
            continue
        if style and row_style != style:  # 스타일이 입력되었고 현재 행의 스타일과 일치하지 않으면 건너뜀
            continue
        if max_price and int(price) > int(max_price):  # 최대 가격이 입력되었고 현재 행의 가격이 최대 가격보다 크면 건너뜀
            continue
        filtered_data.append(row)  # 조건을 모두 만족하는 행은 filtered_data에 추가

    if len(filtered_data) == 0:  # 추천된 데이터가 없는 경우
        messagebox.showinfo("추천 결과", "추천 결과가 없습니다.")  # "추천 결과가 없습니다." 메시지 박스 표시
    else:  # 추천된 데이터가 있는 경우
        # filtered_data와 전체 clothes_data를 인자로하여 show_images 함수 호출하여 이미지와 추천 정보 출력
        show_images(filtered_data, clothes_data)

# 스타일 설명 인터페이스 구현 -> pc 변경 시 파일 경로 변경 필수
def show_system_description():
    text_path = "C:\\Python\\팀플 테스트\\설명.txt"  # 설명 텍스트 파일의 경로 설정

    if os.path.exists(text_path):  # 설명 텍스트 파일이 존재하는 경우
        top_level = tk.Toplevel(window)  # (위 코드와 동일) 새 창 생성
        top_level.title("시스템 설명")  # 창 제목 설정
        top_level.geometry("700x500")  # 창 크기 설정

          # 텍스트 파일 열고 내용 읽기
        with open(text_path, 'r', encoding='utf-8-sig') as file:
            content = file.read()

        # 스크롤 가능한 텍스트 위젯 생성
        description_text = scrolledtext.ScrolledText(top_level, width=70, height=100, wrap=tk.WORD, font=("Arial", 12))
        description_text.pack(padx=10, pady=10)  # 위젯을 창에 배치
        description_text.insert(tk.END, content)  # 파일 내용을 위젯에 삽입
    else:  # 설명 텍스트 파일이 존재하지 않는 경우
        messagebox.showinfo("오류", "설명 파일을 찾을 수 없습니다.")

# 체형 설명 인터페이스 구현
def show_body_type_images():
    top_level = tk.Toplevel(window)  # (위 코드와 동일) 새 창 생성
    top_level.title("체형 사진")  # 창 제목 설정
    top_level.geometry("1000x800")  # 창 크기 설정

    # top_level 프레임(틀, 공간) 생성
    frame = tk.Frame(top_level)
    frame.pack(padx=5, pady=5)  #좌우 및 상하 여백 설정 -> 위젯 주위에 일정한 여백 생성

    # 'body_types.csv' 파일을 열어서 체형 목록 읽기 -> pc 변경 시 파일 경로 변경 필수
    with open("C:\\Python\\팀플 테스트\\body_types.csv", 'r', encoding='utf-8-sig') as file:
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

# 최대 가격 입력창
max_price_label = tk.Label(input_frame, text="최대 가격", font=("Arial", 12), bg="#F0F0F0")
max_price_label.grid(row=2, column=0, padx=5, pady=5)

max_price_entry = tk.Entry(input_frame, width=20, font=("Arial", 12))
max_price_entry.grid(row=2, column=1, padx=5, pady=5)

# 추천 받기 버튼 구현
recommend_button = tk.Button(window, text="추천받기", command=lambda: get_recommendation(season_entry.get(), style_entry.get(), max_price_entry.get()), font=("Arial", 12))
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
