# 상의, 하의 이미지 파일 위치경로를 csv에 저장하는 코드
# Download top/bottom's image from csv file
import csv
import os

# 상의 이미지 파일이 있는 디렉토리 경로
image_dir = r'C:\\Python\\이미지테스트'

image_files = os.listdir(image_dir)

##########################################################
# 결과를 저장할 CSV 파일 경로                            #
# CSV에 이미지 파일 경로 저장 시 csv 파일 형식 변환 필수 #
# 변환 후 인터페이스 실행 시 다시 파일 형식 복구 필수    #
##########################################################
csv_file = 'result.csv'

# 각 이미지 파일에 대해 이미지 경로를 추가하여 저장
for i, file_name in enumerate(image_files):
    # 파일 확장자 확인 (예: .jpg, .png 등)
    #os.path.splitext 파일 확장자 확인하는 splitext 함수
    ext = os.path.splitext(file_name)[-1].lower()

    # 이미지 파일인 경우에만 처리
    if ext in ['.jpg', '.jpeg', '.png', '.gif']:
        # 이미지 파일의 전체 경로 생성
        file_path = os.path.join(image_dir, file_name)

        # 이미지 파일의 이름을 추출
        name = os.path.splitext(file_name)[0]

        # 기존 CSV 파일의 내용을 모두 읽어오기
        rows = []
        with open(csv_file, 'r', newline='') as read_file:
            reader = csv.reader(read_file)
            rows = list(reader)

        # 이미지 경로를 해당 행의 바로 아래에 추가
        rows[i+1].insert(4, file_path)

        # 수정된 내용을 새로운 CSV 파일로 저장
        with open(csv_file, 'w', newline='') as write_file:
            writer = csv.writer(write_file)
            writer.writerows(rows)

print("상의 이미지 경로가 성공적으로 추가되었습니다.")

# 하의 이미지 파일이 있는 디렉토리 경로
image_dir2 = r'C:\Python\이미지테스트2'

image_files2 = os.listdir(image_dir2)

##########################################################
# 결과를 저장할 CSV 파일 경로                            #
# CSV에 이미지 파일 경로 저장 시 csv 파일 형식 변환 필수 #
# 변환 후 인터페이스 실행 시 다시 파일 형식 복구 필수    #
##########################################################
csv_file2 = 'result2.csv'



# 각 이미지 파일에 대해 이미지 경로를 추가하여 저장
for i, file_name2 in enumerate(image_files2):
    # 파일 확장자 확인 (예: .jpg, .png 등)
    #os.path.splitext 파일 확장자 확인하는 splitext 함수
    ext2 = os.path.splitext(file_name2)[-1].lower()

    # 이미지 파일인 경우에만 처리
    if ext2 in ['.jpg', '.jpeg', '.png', '.gif']:
        # 이미지 파일의 전체 경로 생성
        file_path2 = os.path.join(image_dir2, file_name2)

        # 이미지 파일의 이름을 추출
        name2 = os.path.splitext(file_name2)[0]

        # 기존 CSV 파일의 내용을 모두 읽어오기
        rows2 = []
        with open(csv_file2, 'r', newline='') as read_file2:
            reader2 = csv.reader(read_file2)
            rows2 = list(reader2)

        # 이미지 경로를 해당 행의 바로 아래에 추가
        rows2[i+1].insert(4, file_path2)

        # 수정된 내용을 새로운 CSV 파일로 저장
        with open(csv_file2, 'w', newline='') as write_file2:
            writer2 = csv.writer(write_file2)
            writer2.writerows(rows2)

print("하의 이미지 경로가 성공적으로 추가되었습니다.")
