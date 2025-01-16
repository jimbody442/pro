#python

import datetime

#csv 파일로 저장, 프로그램을 다시 실행해도 이전 기록을 불러오도록 구현
import csv

import matplotlib.pyplot as plt

FileName = "expense_tracker.csv"

#수입/ 지출 데이터를 저장할 리스트
datas =[]

def add_data():
    date = input("날짜 (YYYY-MM-DD) :")
    category = input("카테고리 (예 : 식비, 교통비) :")
    amount = float(input("금액(+수입, -지출): "))
    datas.append({"date": date, "category": category, "amount": amount})
    print("기록이 추가 되었습니다!")


def view_data():
    print("\n[가계부 기록지]")
    for data in datas:
        print(f"닐짜 : {data['date']}, 카테고리 :{data['category']}, 금액 : {data['amount']}원 ")
    print()

#총합의 대한 잔액 계산.
def calculate_balance():
    total_income = sum(data["amount"] for data in datas if data["amount"]>0)
    total_expense = sum(data["amount"] for data in datas if data["amount"]<0)
    balance = total_income + total_expense
    print("\n[잔액 계산]")
    print(f"총 지출 : {total_income}원")
    print(f"총 지출 : {abs(total_expense)}원")
    print(f"잔액: {balance}원\n")


def category_statistics():
    stats ={}
    for data in datas:
        if data["amount"] < 0: #지출만 포함
            category = data["category"]
            stats[category] = stats.get(category,0) + abs(data["amount"])
        
    print("\n[카테고리별 지출 통계]")
    for category, total in stats.items():
        print(f"{category}: {total}원")
    print()



#csv파일에 새로운 데이터 내용 저장하기.
def save_data_to_csv():
    with open(FileName, "w", newline ="", encoding="utf-8") as f:
        write = csv.writer(f)
        # 헤더 저장
        write.writerow(["date","category","amount"])
        # 각 기록 저장
        for data in datas:
            write.writerow([data["date"], data["category"],data["amount"]])
    print("데이터가 저장되었습니다.")


#csv파일 내 저장된 내용 가져와서 출력
def load_datas_from_csv():
    try:
        with open(FileName, "r" ,encoding="utf-8")as f:
            reader = csv.DictReader(f)
            for row in reader:
                datas.append({
                    "date" : row["date"],
                    "category" : row["category"],
                    "amount" : float(row["amount"])
                })
        print("기록이 불러와졌습니다!")
    except FileNotFoundError:
        print("저장된 파일이 없습니다. 새로운 파일을 생성합니다.")


def plot_category_statistics():
    stats ={}
    
    for data in datas:
        if data["amount"] < 0: #지출만 포함
            category = data["category"]
            stats[category] = stats.get(category,0) + abs(data["amount"])
    
    #데이터가 없을 경우 처리
    if not stats:
        print("지출 데이터가 없습니다.")
        return

    # 파이 차트 그리기
    labels = stats.keys()
    sizes = stats.values()
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("카테고리별 지출 비율")
    plt.axis("equal")  # 원형으로 출력
    plt.show()


import tkinter as tk
from tkinter import messagebox

def add_record_gui():
    def save_record():
        date = entry_date.get()
        category = entry_category.get()
        amount = float(entry_amount.get())
        datas.append({"date": date, "category": category, "amount": amount})
        messagebox.showinfo("저장 완료", "기록이 저장되었습니다!")
        entry_date.delete(0, tk.END)
        entry_category.delete(0, tk.END)
        entry_amount.delete(0, tk.END)

    root = tk.Tk()
    root.title("가계부 프로그램")
    
    # 레이블
    tk.Label(root, text="날짜 (YYYY-MM-DD):").grid(row=0, column=0)
    tk.Label(root, text="카테고리:").grid(row=1, column=0)
    tk.Label(root, text="금액 (+수입, -지출):").grid(row=2, column=0)

    # 입력 필드
    entry_date = tk.Entry(root)
    entry_category = tk.Entry(root)
    entry_amount = tk.Entry(root)

    entry_date.grid(row=0, column=1)
    entry_category.grid(row=1, column=1)
    entry_amount.grid(row=2, column=1)

    # 저장 버튼
    save_button = tk.Button(root, text="저장", command=save_record)
    save_button.grid(row=3, columnspan=2)

    root.mainloop()

def main():
    load_datas_from_csv() #기록 불러오기.
    while True:
        print("1. 수입/지출 추가")
        print("2. 기록 보기")
        print("3. 잔액 계산")
        print("4. 카테고리별 통계 보기")
        print("5. 카테고리별 지출 그래프 보기")
        print("6. 데이터 저장")
        print("7. GUI 수입/지출 추가")
        print("8. 종료")
        choice = input("선택 :")

        if choice == "1":
            add_data()
        elif choice =="2":
            view_data()
        elif choice =="3":
            calculate_balance()
        elif choice =="4":
            category_statistics() #통계 함수 호출
        elif choice == "5":
            plot_category_statistics()
        elif choice =="6":
            save_data_to_csv() #기록 저장
        elif choice == "7":
            add_record_gui()
        elif choice =="8":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ =="__main__":
    main()