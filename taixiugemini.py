import streamlit as st
import random
import time

# Cấu hình trang
st.set_page_config(page_title="Game Tài Xỉu Online", page_icon="🎲")

# Khởi tạo số dư ban đầu nếu chưa có
if 'balance' not in st.session_state:
    st.session_state.balance = 10000

st.title("🎲 Trò chơi Tài Xỉu")
st.sidebar.header("Thông tin người chơi")
st.sidebar.write(f"💰 Số dư: **{st.session_state.balance:,}** VNĐ")

# Giao diện chính
st.write("### Chào mừng bạn đến với sòng bài Python!")
st.info("Luật chơi: 3-10 là Xỉu, 11-18 là Tài.")

# Input từ người dùng
col1, col2 = st.columns(2)
with col1:
    choice = st.radio("Chọn cửa đặt:", ("Tài", "Xỉu"))
with col2:
    bet_amount = st.number_input("Số tiền cược:", min_value=1, max_value=st.session_state.balance, value=1000, step=500)

if st.button("Lắc Xúc Xắc!"):
    if bet_amount > st.session_state.balance:
        st.error("Bạn không đủ tiền đặt cược!")
    else:
        # Hiệu ứng chờ đợi
        with st.spinner('Đang lắc xúc xắc...'):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            
            # Logic xúc xắc
            d1, d2, d3 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)
            total = d1 + d2 + d3
            result_text = "Xỉu" if total < 11 else "Tài"
            
            # Hiển thị kết quả bằng các cột
            st.markdown(f"## Kết quả: {total} ({result_text})")
            c1, c2, c3 = st.columns(3)
            c1.metric("Xúc xắc 1", d1)
            c2.metric("Xúc xắc 2", d2)
            c3.metric("Xúc xắc 3", d3)

            # Kiểm tra thắng thua
            if (choice == "Tài" and total >= 11) or (choice == "Xỉu" and total < 11):
                st.balloons()
                st.success(f"Chúc mừng! Bạn đã thắng {bet_amount:,} VNĐ!")
                st.session_state.balance += bet_amount
            else:
                st.error(f"Rất tiếc! Bạn đã mất {bet_amount:,} VNĐ.")
                st.session_state.balance -= bet_amount

# Nút reset game
if st.sidebar.button("Nạp lại 10k (Reset)"):
    st.session_state.balance = 10000
    st.rerun()