import tkinter as tk
from tkinter import messagebox
import random

class TaiXiuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Tài Xỉu - Tkinter")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Khởi tạo vốn
        self.tien_goc = 10000
        self.dice_chars = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅'] # Ký tự xúc xắc Unicode

        # --- Giao diện ---
        
        # Tiêu đề
        self.lbl_title = tk.Label(root, text="TÀI XỈU", font=("Arial", 24, "bold"), fg="red")
        self.lbl_title.pack(pady=10)

        # Hiển thị tiền
        self.lbl_money = tk.Label(root, text=f"Vốn hiện có: {self.tien_goc:,} đ", font=("Arial", 14), fg="blue")
        self.lbl_money.pack(pady=5)

        # Khu vực hiển thị xúc xắc
        self.frame_dice = tk.Frame(root)
        self.frame_dice.pack(pady=20)
        
        self.dice_labels = []
        for i in range(3):
            lbl = tk.Label(self.frame_dice, text="?", font=("Times New Roman", 60))
            lbl.grid(row=0, column=i, padx=10)
            self.dice_labels.append(lbl)

        # Hiển thị kết quả (Tổng điểm và Tài/Xỉu)
        self.lbl_result = tk.Label(root, text="Mời đặt cược", font=("Arial", 14, "bold"))
        self.lbl_result.pack(pady=10)

        # Nhập tiền cược
        tk.Label(root, text="Nhập tiền cược:").pack()
        self.entry_bet = tk.Entry(root, font=("Arial", 12), justify='center')
        self.entry_bet.pack(pady=5)

        # Các nút bấm chọn
        self.frame_buttons = tk.Frame(root)
        self.frame_buttons.pack(pady=20)

        self.btn_tai = tk.Button(self.frame_buttons, text="CƯỢC TÀI (>=11)", font=("Arial", 12, "bold"), bg="#ffcccc", width=15, command=lambda: self.start_game('Tai'))
        self.btn_tai.grid(row=0, column=0, padx=10)

        self.btn_xiu = tk.Button(self.frame_buttons, text="CƯỢC XỈU (<11)", font=("Arial", 12, "bold"), bg="#ccffcc", width=15, command=lambda: self.start_game('Xiu'))
        self.btn_xiu.grid(row=0, column=1, padx=10)

    def validate_bet(self):
        """Kiểm tra số tiền nhập vào có hợp lệ không"""
        try:
            bet = int(self.entry_bet.get())
            if bet <= 0:
                messagebox.showwarning("Lỗi", "Tiền cược phải lớn hơn 0")
                return None
            if bet > self.tien_goc:
                messagebox.showwarning("Lỗi", "Bạn không đủ tiền để cược số này!")
                return None
            return bet
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số tiền hợp lệ")
            return None

    def start_game(self, user_choice):
        """Bắt đầu lượt chơi"""
        bet_amount = self.validate_bet()
        if bet_amount is None:
            return

        # Trừ tiền tạm thời (nếu thua thì mất luôn, thắng thì cộng lại sau)
        self.current_bet = bet_amount
        self.current_choice = user_choice
        
        # Khóa nút bấm để tránh spam
        self.btn_tai.config(state="disabled")
        self.btn_xiu.config(state="disabled")
        self.entry_bet.config(state="disabled")

        # Bắt đầu hiệu ứng lắc
        self.animation_count = 0
        self.roll_animation()

    def roll_animation(self):
        """Tạo hiệu ứng xúc xắc thay đổi liên tục"""
        if self.animation_count < 15: # Lắc 15 lần (khoảng 1.5 giây)
            fake_dice = [random.randint(1, 6) for _ in range(3)]
            for i, val in enumerate(fake_dice):
                self.dice_labels[i].config(text=self.dice_chars[val-1], fg="gray")
            
            self.animation_count += 1
            self.root.after(100, self.roll_animation) # Gọi lại hàm sau 100ms
        else:
            self.finish_game()

    def finish_game(self):
        """Tính toán kết quả cuối cùng"""
        # Ra kết quả thật
        dice_values = [random.randint(1, 6) for _ in range(3)]
        total = sum(dice_values)
        
        # Cập nhật hình ảnh xúc xắc thật
        for i, val in enumerate(dice_values):
            self.dice_labels[i].config(text=self.dice_chars[val-1], fg="black")

        # Xác định Tài/Xỉu
        result_str = "Tai" if total >= 11 else "Xiu"
        
        # Hiển thị thông báo
        msg = f"Tổng: {total} - {result_str.upper()}"
        
        # Kiểm tra thắng thua
        # Logic: Ban đầu trừ tiền, thắng thì cộng lại (vốn + cược) + tiền thắng (cược) = vốn + 2*cược?
        # Cách đơn giản: Nếu thắng thì cộng tiền. Nếu thua thì trừ tiền.
        
        if (user_choice := self.current_choice) == result_str:
            # Thắng
            winnings = self.current_bet
            self.tien_goc += winnings
            self.lbl_result.config(text=f"{msg}\nBẠN THẮNG! (+{winnings:,})", fg="green")
        else:
            # Thua
            self.tien_goc -= self.current_bet
            self.lbl_result.config(text=f"{msg}\nBẠN THUA! (-{self.current_bet:,})", fg="red")

        # Cập nhật lại số dư trên giao diện
        self.lbl_money.config(text=f"Vốn hiện có: {self.tien_goc:,} đ")

        # Mở khóa nút bấm
        self.btn_tai.config(state="normal")
        self.btn_xiu.config(state="normal")
        self.entry_bet.config(state="normal")

        # Kiểm tra hết tiền
        if self.tien_goc <= 0:
            messagebox.showinfo("Game Over", "Bạn đã cháy túi! Game sẽ reset về 10,000đ.")
            self.tien_goc = 10000
            self.lbl_money.config(text=f"Vốn hiện có: {self.tien_goc:,} đ")
            self.lbl_result.config(text="Đã reset game", fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaiXiuGame(root)
    root.mainloop()