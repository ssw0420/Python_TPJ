import csv
import random
import tkinter as tk

def get_recommendation(season, max_price, style):
    # 계절,스타일에 따라 각 csv 파일에서 데이터 읽어오기
    if season=="봄":
        if style =="street":
            with open('result.csv', 'r', encoding='utf-8') as file:
                clothes_data = list(csv.reader(file))
        elif style =="casual":
            with open('C:/Users/이승엽/Desktop/2023 1gkrrl/봄,캐주얼.csv', 'r', encoding='utf-8') as file:
                clothes_data = list(csv.reader(file))
        elif style =="formal":
            with open('result.csv', 'r', encoding='utf-8') as file:
                clothes_data = list(csv.reader(file))
    elif season=="여름":
        if style =="street":
            with open('C:/Users/이승엽/Desktop/2023 1gkrrl/여름,스트릿.csv', 'r', encoding='utf-8') as file:
                clothes_data = list(csv.reader(file))
        elif style =="casual":
            with open('result.csv', 'r', encoding='utf-8') as file:
                clothes_data = list(csv.reader(file))
        elif style =="formal":
            with open('result.csv', 'r', encoding='utf-8') as file:
                clothes_data = list(csv.reader(file))
    elif season=="가을":
        if style =="street":
            with open('result.csv', 'r', encoding='utf-8') as file:
                clothes_data = list(csv.reader(file))
        elif style =="casual":
            with open('result.csv', 'r', encoding='utf-8') as file:
                clothes_data = list(csv.reader(file))
        elif style =="formal":
            with open('result.csv', 'r', encoding='utf-8') as file:
                clothes_data = list(csv.reader(file))
    elif season=="겨울":
        if style =="street":
            with open('result.csv', 'r', encoding='utf-8') as file:
                clothes_data = list(csv.reader(file))
        elif style =="casual":
            with open('result.csv', 'r', encoding='utf-8') as file:
                clothes_data = list(csv.reader(file))
        elif style =="formal":
            with open('result.csv', 'r', encoding='utf-8') as file:
                clothes_data = list(csv.reader(file))                

    # 필터링된 데이터 추출하기
    if max_price:
        filtered_data = [row for row in clothes_data if (row[2]) <= str(max_price)]

    # 결과가 없는 경우
    if not filtered_data:
        recommendation_text.set("해당 조건에 맞는 추천 옷이 없습니다.")
        return

    # 랜덤으로 추천 결과 5개 선택하기
    random_data = random.sample(filtered_data, min(5, len(filtered_data)))
    recommendation_text.set("")

    # 선택된 추천 결과 화면에 보여주기
    for idx, data in enumerate(random_data):
        result = f'{idx + 1}. {data[0]} ({data[1]}, {data[2]}원)\n'
        recommendation_text.set(recommendation_text.get() + result)

# tkinter GUI 생성
window = tk.Tk()
window.title("추천 시스템")

# 계절 입력창 생성
m_weather_label = tk.Label(window, text="계절 입력 (ex. 봄, 여름, 가을, 겨울): ")
m_weather_label.grid(row=0, column=0)

m_weather_entry = tk.Entry(window)
m_weather_entry.grid(row=0, column=1)

# 최대 가격 입력창 생성
m_price_label = tk.Label(window, text="최대 가격 입력 (ex. 10000): ")
m_price_label.grid(row=1, column=0)

m_price_entry = tk.Entry(window)
m_price_entry.grid(row=1, column=1)

# 스타일 입력창 생성
m_style_label = tk.Label(window, text="스타일 입력 (ex. casual, formal, street): ")
m_style_label.grid(row=2, column=0)

m_style_entry = tk.Entry(window)
m_style_entry.grid(row=2, column=1)

# 추천 결과 출력창 생성
recommendation_text = tk.StringVar()
recommendation_label = tk.Label(window, textvariable=recommendation_text, justify='left')
recommendation_label.grid(row=4, column=0, columnspan=2)

# 확인 버튼 생성
login_button = tk.Button(window, text="확인", command=lambda: get_recommendation(m_weather_entry.get(), m_price_entry.get(), m_style_entry.get()))
login_button.grid(row=3, column=1)

# 계절 입력창에 Enter 키 바인딩
def enter_pressed(event):
    get_recommendation(m_weather_entry.get(), m_price_entry.get(), m_style_entry.get())

m_weather_entry.bind('<Return>', enter_pressed)

window.mainloop()