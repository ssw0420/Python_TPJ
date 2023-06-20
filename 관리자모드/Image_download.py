#상의, 하의 이미지 파일 위치경로를 csv에 저장하는 코드
import csv
import os

# 상의 이미지 파일이 있는 디렉토리 경로
image_dir = r'C:\\파이썬 1조\\상의 목록\\캐주얼\\spring_casual_high'

image_files = os.listdir(image_dir)

##########################################################
# 결과를 저장할 CSV 파일 경로                            #
# CSV에 이미지 파일 경로 저장 시 csv 파일 형식 변환 필수 #
# 변환 후 인터페이스 실행 시 다시 파일 형식 복구 필수    #
##########################################################
csv_file = 'C:\\파이썬 1조\\상의 목록\\csv파일\\캐주얼\\spring_casual_high_read.csv'



# 각 이미지 파일에 대해 이미지 경로를 추가하여 저장
for i, file_name in enumerate(image_files):
    # 파일 확장자 확인 (예: .jpg, .png 등)
    #os.path.splitext 파일 확장자 확인하는 splitext 함수
    ext = os.path.splitext(file_name)[-1].lower()

    # 이미지 파일인 경우에만 처리
    if ext in ['.jpg', '.jpeg', '.png', '.gif']:
        # 이미지 파일의 전체 경로 생성
        file_path = os.path.join("C:\\\\파이썬 1조\\\\상의 목록\\\\캐주얼\\\\spring_casual_high\\\\", str(i+1))

        # 이미지 파일 확장자 추가
        file_path += ".jpg"
        
        # 이미지 파일의 이름을 추출
        name = os.path.splitext(file_name)[0]

        # 기존 CSV 파일의 내용을 모두 읽어오기
        rows = []
        with open(csv_file, 'r', newline='') as read_file:
            reader = csv.reader(read_file)
            rows = list(reader)

        # 이미지 경로를 해당 행의 바로 아래에 추가
        rows[i+1].insert(7, file_path)

        # 수정된 내용을 새로운 CSV 파일로 저장
        with open(csv_file, 'w', newline='') as write_file:
            writer = csv.writer(write_file)
            writer.writerows(rows)

print("상의 이미지 경로가 성공적으로 추가되었습니다.")

# 하의 이미지 파일이 있는 디렉토리 경로
image_dir1 = r'C:\\파이썬 1조\\하의 목록\\캐주얼\\spring_casual_low'

image_files1 = os.listdir(image_dir1)

##########################################################
# 결과를 저장할 CSV 파일 경로                            #
# CSV에 이미지 파일 경로 저장 시 csv 파일 형식 변환 필수 #
# 변환 후 인터페이스 실행 시 다시 파일 형식 복구 필수    #
##########################################################
csv_file1 = 'C:\\파이썬 1조\\하의 목록\\csv파일\\캐주얼\\spring_casual_low_read.csv'



# 각 이미지 파일에 대해 이미지 경로를 추가하여 저장
for i, file_name1 in enumerate(image_files1):
    # 파일 확장자 확인 (예: .jpg, .png 등)
    #os.path.splitext 파일 확장자 확인하는 splitext 함수
    ext1 = os.path.splitext(file_name1)[-1].lower()

    # 이미지 파일인 경우에만 처리
    if ext1 in ['.jpg', '.jpeg', '.png', '.gif']:
        # 이미지 파일의 전체 경로 생성
        file_path1 = os.path.join("C:\\\\파이썬 1조\\\\하의 목록\\\\캐주얼\\\\spring_casual_low\\\\", str(i+1))

        # 이미지 파일 확장자 추가
        file_path1 += ".jpg"

        # 이미지 파일의 이름을 추출
        name1 = os.path.splitext(file_name1)[0]

        # 기존 CSV 파일의 내용을 모두 읽어오기
        rows1 = []
        with open(csv_file1, 'r', newline='') as read_file1:
            reader1 = csv.reader(read_file1)
            rows1 = list(reader1)

        # 이미지 경로를 해당 행의 바로 아래에 추가
        rows1[i+1].insert(7, file_path1)

        # 수정된 내용을 새로운 CSV 파일로 저장
        with open(csv_file1, 'w', newline='') as write_file1:
            writer1 = csv.writer(write_file1)
            writer1.writerows(rows1)

print("하의 이미지 경로가 성공적으로 추가되었습니다.")
