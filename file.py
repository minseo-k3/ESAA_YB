import pandas as pd

# 변환할 파일 목록
files = [
    "그릭요거트_영양성분_원재료추가.xlsx"
]

for file in files:
    # 엑셀 읽기
    df = pd.read_excel(file)

    # csv 파일명 생성
    csv_file = file.replace(".xlsx", ".csv")

    # CSV 저장 (한글 깨짐 방지)
    df.to_csv(csv_file, index=False, encoding="utf-8-sig")

    print(f"변환 완료: {csv_file}")

print("\n모든 파일 변환 완료!")