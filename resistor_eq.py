import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from PIL import Image, ImageTk

def calculate():
    try:
        V=1
        Req=0

        R1 = float(entry_R1.get())
        R2 = float(entry_R2.get())
        R3 = float(entry_R3.get())
        R4 = float(entry_R4.get())
        R5 = float(entry_R5.get())

        if R1 <= 0 or R2 <= 0 or R3 <= 0 or R4 <= 0 or R5 <= 0:
            result_label.config(
                text=f"等效電阻 Req = {Req:.2f} Ω",
                fg="#1B5E20"
            )

        else:
            R_th=R1*R2/(R1+R2)+R3*R4/(R3+R4)
            V_th=V*R2/(R1+R2)-V*R4/(R3+R4)
            I_th=V_th*R5/(R_th+R5)

            V_A=(R1*R2/(R1+R2))*(V/R1-I_th)
            V_B=(R3*R4/(R3+R4))*(V/R3+I_th)
            Req=V/((V-V_A)/R1+(V-V_B)/R3)
            print(f"Req={Req:.2f}")

            #顯示於介面上
            result_label.config(
                text=f"等效電阻 Req = {Req:.2f} Ω",
                fg="#1B5E20"
            )




            #print(f"Req = {Req:.4f} Ω")#debug

    except ValueError:
        messagebox.showerror("輸入錯誤", "請輸入數字，例如 100、220、4.7")


def clear_inputs():
    entry_R1.delete(0, tk.END)
    entry_R2.delete(0, tk.END)
    entry_R3.delete(0, tk.END)
    entry_R4.delete(0, tk.END)
    entry_R5.delete(0, tk.END)

    result_label.config(text="等效電阻 Req = 尚未計算", fg="#555555")
    detail_label.config(text="")



# 建立主視窗
window = tk.Tk()
window.title("電阻等效計算器")
window.geometry("900x750")
window.configure(bg="#F4F6F8")

# =========================
# 標題區
# =========================

title_label = tk.Label(
    window,
    text="電阻等效計算器",
    font=("Microsoft JhengHei", 24, "bold"),
    bg="#F4F6F8",
    fg="#263238"
)
title_label.pack(pady=15)

subtitle_label = tk.Label(
    window,
    text="輸入 R1～R5 的電阻值，程式會計算等效電阻 Req",
    font=("Microsoft JhengHei", 12),
    bg="#F4F6F8",
    fg="#607D8B"
)
subtitle_label.pack()


# 圖片區

image_frame = tk.Frame(window, bg="white", bd=2, relief="groove")
image_frame.pack(pady=15)

BASE_DIR = Path(__file__).resolve().parent
image_path = BASE_DIR /  "resistor.png"

try:
    image = Image.open(image_path)
    image = image.resize((650, 300))
    circuit_image = ImageTk.PhotoImage(image)

    image_label = tk.Label(image_frame, image=circuit_image, bg="white")
    image_label.pack(padx=10, pady=10)

except FileNotFoundError:
    image_label = tk.Label(
        image_frame,
        text="找不到圖片，請確認 images/resistor.png 是否存在",
        font=("Microsoft JhengHei", 14),
        fg="red",
        bg="white"
    )
    image_label.pack(padx=50, pady=50)



# 輸入區

input_frame = tk.Frame(window, bg="#F4F6F8")
input_frame.pack(pady=10)

left_frame = tk.Frame(input_frame, bg="#F4F6F8")
left_frame.grid(row=0, column=0, padx=30)

right_frame = tk.Frame(input_frame, bg="#F4F6F8")
right_frame.grid(row=0, column=1, padx=30)


def create_input(parent, label_text, row):
    label = tk.Label(
        parent,
        text=label_text,
        font=("Microsoft JhengHei", 13),
        bg="#F4F6F8",
        fg="#263238"
    )
    label.grid(row=row, column=0, padx=8, pady=8, sticky="e")

    entry = tk.Entry(
        parent,
        font=("Arial", 13),
        width=12,
        justify="center",
        bd=2,
        relief="groove"
    )
    entry.grid(row=row, column=1, padx=8, pady=8)

    unit = tk.Label(
        parent,
        text="Ω",
        font=("Microsoft JhengHei", 13),
        bg="#F4F6F8",
        fg="#263238"
    )
    unit.grid(row=row, column=2, padx=5, pady=8)

    return entry


entry_R1 = create_input(left_frame, "R1 =", 0)
entry_R2 = create_input(left_frame, "R2 =", 1)
entry_R3 = create_input(left_frame, "R3 =", 2)

entry_R4 = create_input(right_frame, "R4 =", 0)
entry_R5 = create_input(right_frame, "R5 =", 1)


# 按鈕區

button_frame = tk.Frame(window, bg="#F4F6F8")
button_frame.pack(pady=15)

calculate_button = tk.Button(
    button_frame,
    text="計算等效電阻",
    command=calculate,
    font=("Microsoft JhengHei", 14, "bold"),
    bg="#1976D2",
    fg="white",
    width=15,
    relief="flat",
    cursor="hand2"
)
calculate_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(
    button_frame,
    text="清除輸入",
    command=clear_inputs,
    font=("Microsoft JhengHei", 14, "bold"),
    bg="#78909C",
    fg="white",
    width=12,
    relief="flat",
    cursor="hand2"
)
clear_button.grid(row=0, column=1, padx=10)



# 結果顯示區
result_frame = tk.Frame(window, bg="white", bd=2, relief="groove")
result_frame.pack(pady=15, padx=30, fill="x")

result_label = tk.Label(
    result_frame,
    text="等效電阻 Req = 尚未計算",
    font=("Microsoft JhengHei", 18, "bold"),
    bg="white",
    fg="#555555"
)
result_label.pack(pady=15)

detail_label = tk.Label(
    result_frame,
    text="",
    font=("Consolas", 12),
    bg="white",
    fg="#37474F",
    justify="left"
)
detail_label.pack(pady=10)

# 主迴圈
window.mainloop()