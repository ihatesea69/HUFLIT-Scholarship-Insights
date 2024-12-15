import streamlit as st
import numpy as np

# Load mô hình và mapping nhãn
import joblib
model = joblib.load("./trained_model.pkl")
label_mapping = {'Học bổng SV nỗ lực': 0, 'Học bổng SV tài năng': 1, 'Khen thưởng SV giỏi': 2}
reverse_label_mapping = {v: k for k, v in label_mapping.items()}

# Tiêu đề ứng dụng
st.title("Dự Đoán Danh Hiệu Sinh Viên")

# Nhập liệu từ người dùng
behavior_score = st.number_input("Nhập điểm rèn luyện (ĐRL)", min_value=0.0, max_value=100.0, step=0.1)
academic_score = st.number_input("Nhập GPA (TBHT)", min_value=0.0, max_value=4.0, step=0.1)

# Dự đoán khi người dùng nhấn nút
if st.button("Dự Đoán"):
    # Chuẩn hóa dữ liệu
    input_data = np.array([[behavior_score, academic_score]])
    prediction = model.predict(input_data)
    predicted_label = reverse_label_mapping[prediction[0]]
    
    # Hiển thị kết quả
    st.success(f"Loại danh hiệu dự đoán: {predicted_label}")
