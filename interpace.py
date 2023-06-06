import csv
import random
import os
import tkinter as tk
from tkinter import scrolledtext, messagebox, Label
from PIL import ImageTk, Image

def show_images(images, recommendations):
    # 새로운 윈도우 생성
    new_window = tk.Toplevel()
    new_window.title("상의 추천")
    new_window.geometry("800x600")

    canvas = tk.Canvas(new_window)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(new_window, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor=tk.NW)

    photo_list = []  # PhotoImage objects list

    # 이미지와 추천 정보 표시
    for idx, row in enumerate(images):
        name, style, price, season, image_path = row

        image = Image.open(image_path.strip('"'))
        image = image.resize((150, 150), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(frame, image=photo)
        label.image = photo
        label.grid(row=idx, column=0, padx=5, pady=5)

        recommendation_label1 = tk.Label(frame, text=name, font=("Arial", 12))
        recommendation_label1.grid(row=idx, column=1, padx=5, pady=5)

        price_label = tk.Label(frame, text=f"{price}원", font=("Arial", 12))
        price_label.grid(row=idx, column=2, padx=5, pady=5)

        recommendation_label1.bind("<Button-1>", lambda e, rec=recommendations[idx]: show_additional_recommendations(e, rec))

        photo_list.append(photo)

    canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))


def show_additional_recommendations(event, recommendation):
    top_level = tk.Toplevel(window)
    top_level.title("하의 추천")
    top_level.geometry("800x600")

    frame = tk.Frame(top_level)
    frame.pack(padx=5, pady=5)

    with open('result2.csv', 'r', encoding='utf-8') as file:
        additional_recommendations = list(csv.reader(file))
        filtered_recommendations = []

        for rec in additional_recommendations:    
            if rec[3] == recommendation[3] and rec[1] == recommendation[1] and (not max_price_entry.get() or int(rec[2]) <= int(max_price_entry.get()) - int(recommendation[2])):
                filtered_recommendations.append(rec)

                #계절,스타일 동일 시 나오도록 [3] = [3] [1] = [1]

                #가격 필터링 
                # int(rec[2])(하의 가격) <= int(max_price_entry.get()) (최대 가격) - int(recommendation[2])(상의 가격)
                # max_price_entry에 50000이 입력되었고, 추천 상의의 가격이 30000이라고 가정 했을때 , 하의의 가격이 최대 가격을 넘지 않으려면 최대 가격인 50000에서 상의의 가격인 30000을 뺀 값인 20000보다 하의의 가격이 작거나 같아야 함

        random_recommendations = random.sample(filtered_recommendations, min(3, len(filtered_recommendations)))

    if len(random_recommendations) == 0:
        messagebox.showinfo("하의 추천", "가격에 맞는 하의 상품이 없습니다.")
        return

    for idx, recommendation in enumerate(random_recommendations):
        name, style, price, season, image_path = recommendation

        image = Image.open(image_path.strip('"')) 
        image = image.resize((150, 150), Image.Resampling.LANCZOS) 
        photo = ImageTk.PhotoImage(image)  

        label = tk.Label(frame, image=photo)
        label.image = photo
        label.grid(row=idx, column=0, padx=5, pady=5, sticky="w")

        text_label1 = tk.Label(frame, text=name, font=("Arial", 12))
        text_label1.grid(row=idx, column=1, padx=5, pady=5)

        text_label2 = tk.Label(frame, text=f"{price}원", font=("Arial", 12))
        text_label2.grid(row=idx, column=2, padx=5, pady=5)


def get_recommendation(season, style, max_price=None, body_type=None):
    with open('result.csv', 'r', encoding='utf-8') as file:
        clothes_data = list(csv.reader(file))

    if not season or not style:
        recommendation_text.delete('1.0', tk.END)
        recommendation_text.insert(tk.END, "계절과 스타일 입력은 필수!")
        return

    filtered_data = []     
    for row in clothes_data:
        name, row_style, price, row_season, image_path = row
        if season and row_season != season:
            continue
        if style and row_style != style:
            continue
        if max_price and int(price) > int(max_price):
            continue
        filtered_data.append(row)

    if len(filtered_data) == 0:
        messagebox.showinfo("추천 결과", "추천 결과가 없습니다.")
    else:
        show_images(filtered_data, filtered_data)


def show_system_description():
    text_path = "C:\\Users\\user\\Desktop\\설명.txt"
    if os.path.exists(text_path):
        top_level = tk.Toplevel(window)
        top_level.title("시스템 설명")
        top_level.geometry("400x300")

        with open(text_path, 'r', encoding='utf-8') as file:
            content = file.read()

        description_text = scrolledtext.ScrolledText(top_level, width=50, height=10, wrap=tk.WORD, font=("Arial", 12))
        description_text.pack(padx=10, pady=10)
        description_text.insert(tk.END, content)
    else:
        messagebox.showinfo("오류", "설명 파일을 찾을 수 없습니다.")


def show_body_type_images():
    top_level = tk.Toplevel(window)
    top_level.title("체형 사진")
    top_level.geometry("800x600")

    frame = tk.Frame(top_level)
    frame.pack(padx=5, pady=5)

    with open("C:\\Users\\user\\Desktop\\body_types.csv", 'r', encoding='utf-8') as file:
        body_type_images = list(csv.reader(file))
        body_type_images = body_type_images[1:]  # 첫 번째 행 제외

    for idx, body_type in enumerate(body_type_images):
        name, image_path, description = body_type

        image = Image.open(image_path.strip('"'))
        image = image.resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(frame, image=photo)
        label.image = photo
        label.grid(row=idx, column=0, padx=5, pady=5)

        text_label1 = tk.Label(frame, text=name, font=("Arial", 12))
        text_label1.grid(row=idx, column=1, padx=5, pady=5)

        text_label2 = tk.Label(frame, text=description, font=("Arial", 12))
        text_label2.grid(row=idx, column=2, padx=5, pady=5)


# Main window
window = tk.Tk()
window.title("오.패.추")
window.geometry("800x600")
window.configure(bg="#F0F0F0")

# Title label
title_label = Label(window, text="오.패.추", font=("Arial", 24, "bold"), bg="#F0F0F0")
title_label.pack(pady=10)

# Input form
input_frame = tk.Frame(window, bg="#F0F0F0")
input_frame.pack(pady=10)

season_label = tk.Label(input_frame, text="계절", font=("Arial", 12), bg="#F0F0F0")
season_label.grid(row=0, column=0, padx=5, pady=5)

season_entry = tk.Entry(input_frame, width=20, font=("Arial", 12))
season_entry.grid(row=0, column=1, padx=5, pady=5)

style_label = tk.Label(input_frame, text="스타일", font=("Arial", 12), bg="#F0F0F0")
style_label.grid(row=1, column=0, padx=5, pady=5)

style_entry = tk.Entry(input_frame, width=20, font=("Arial", 12))
style_entry.grid(row=1, column=1, padx=5, pady=5)

max_price_label = tk.Label(input_frame, text="최대 가격", font=("Arial", 12), bg="#F0F0F0")
max_price_label.grid(row=2, column=0, padx=5, pady=5)

max_price_entry = tk.Entry(input_frame, width=20, font=("Arial", 12))
max_price_entry.grid(row=2, column=1, padx=5, pady=5)

recommend_button = tk.Button(window, text="추천받기", command=lambda: get_recommendation(season_entry.get(), style_entry.get(), max_price_entry.get()), font=("Arial", 12))
recommend_button.pack()

recommendation_text = scrolledtext.ScrolledText(window, width=60, height=10, wrap=tk.WORD, font=("Arial", 12))
recommendation_text.pack()

description_button = tk.Button(window, text="설명", command=show_system_description, font=("Arial", 12))
description_button.pack(side=tk.RIGHT, padx=10, pady=10, anchor=tk.SE)

body_type_button = tk.Button(window, text="체형 사진", command=show_body_type_images, font=("Arial", 12))
body_type_button.pack(side=tk.LEFT, padx=10, pady=10, anchor=tk.SW)

window.mainloop()
