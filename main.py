import streamlit as st
import random
import os

# 페이지 설정
st.set_page_config(page_title="💪 근육 퀴즈", page_icon="🧠", layout="centered")

st.markdown("""
    <style>
    .title { font-size: 42px; font-weight: bold; color: #6c5ce7; text-align: center; }
    .hint { background-color: #dfe6e9; padding: 15px; border-radius: 10px; margin: 10px 0; font-size: 16px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">💪 근육 이름 퀴즈</div>', unsafe_allow_html=True)

# 📷 사진 퀴즈 데이터
photo_data = [
    {"filename": "deltoid.jpg", "answer": "삼각근"},
    {"filename": "biceps.jpg", "answer": "이두근"},
    {"filename": "triceps.jpg", "answer": "삼두근"},
    {"filename": "pectoralis_major.jpg", "answer": "대흉근"},
    {"filename": "latissimus_dorsi.jpg", "answer": "광배근"},
    {"filename": "rectus_abdominis.jpg", "answer": "복직근"},
    {"filename": "gluteus_maximus.jpg", "answer": "둔근"},
    {"filename": "hamstrings.jpg", "answer": "햄스트링"},
    {"filename": "quadriceps.jpg", "answer": "대퇴사두근"},
    {"filename": "gastrocnemius.jpg", "answer": "종아리근"},
]

# 🧩 초성 퀴즈 데이터
chosung_data = [
    {"name": "삼각근", "chosung": "ㅅㄱㄱ", "hint": "어깨에 위치"},
    {"name": "이두근", "chosung": "ㅇㄷㄱ", "hint": "팔 앞쪽"},
    {"name": "삼두근", "chosung": "ㅅㄷㄱ", "hint": "팔 뒤쪽"},
    {"name": "대흉근", "chosung": "ㄷㅎㄱ", "hint": "가슴 근육"},
    {"name": "광배근", "chosung": "ㄱㅂㄱ", "hint": "등 넓은 근육"},
    {"name": "복직근", "chosung": "ㅂㅈㄱ", "hint": "복근"},
    {"name": "둔근", "chosung": "ㄷㄱ", "hint": "엉덩이"},
    {"name": "햄스트링", "chosung": "ㅎㅅㅌㄹ", "hint": "허벅지 뒤"},
    {"name": "대퇴사두근", "chosung": "ㄷㅌㅅㄷㄱ", "hint": "허벅지 앞"},
    {"name": "종아리근", "chosung": "ㅈㅇㄹㄱ", "hint": "종아리"},
]

# 폴더 경로
IMAGE_FOLDER = "muscle_images"

# 퀴즈 유형 선택
quiz_type = st.radio("퀴즈 유형을 선택하세요:", ["🧩 초성 퀴즈", "📷 사진 퀴즈"])

# 세션 상태 초기화
if "quiz_data" not in st.session_state or st.session_state.get("quiz_type") != quiz_type:
    st.session_state.quiz_type = quiz_type
    st.session_state.q_index = 0
    st.session_state.score = 0

    if quiz_type == "📷 사진 퀴즈":
        # 실제 존재하는 파일만 필터링
        valid_photos = [q for q in photo_data if os.path.exists(os.path.join(IMAGE_FOLDER, q["filename"]))]
        st.session_state.quiz_data = random.sample(valid_photos, len(valid_photos))
    else:
        st.session_state.quiz_data = random.sample(chosung_data, len(chosung_data))

# 퀴즈 진행
if st.session_state.q_index < len(st.session_state.quiz_data):
    q = st.session_state.quiz_data[st.session_state.q_index]
    st.markdown(f"### 문제 {st.session_state.q_index + 1} / {len(st.session_state.quiz_data)}")

    if quiz_type == "📷 사진 퀴즈":
        img_path = os.path.join(IMAGE_FOLDER, q["filename"])
        st.image(img_path, caption="이 근육의 이름은?", use_column_width=True)
        answer = q["answer"]
    else:
        st.markdown(f"**초성:** `{q['chosung']}`")
        st.markdown(f"<div class='hint'>💡 힌트: {q['hint']}</div>", unsafe_allow_html=True)
        answer = q["name"]

    user_input = st.text_input("정답을 입력하세요 (한글)").strip()

    if st.button("제출"):
        if user_input == answer:
            st.success("✅ 정답입니다!")
            st.session_state.score += 1
        else:
            st.error(f"❌ 오답입니다. 정답은 **{answer}** 입니다.")
        st.session_state.q_index += 1
        st.experimental_rerun()

else:
    st.balloons()
    st.markdown(f"## 🎉 퀴즈 완료! 점수: **{st.session_state.score} / {len(st.session_state.quiz_data)}**")
    if st.button("🔁 다시 시작하기"):
        del st.session_state.quiz_data
        st.experimental_rerun()
