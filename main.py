import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="💪 근육 초성 퀴즈", page_icon="🧠", layout="centered")

st.markdown("""
    <style>
    .title { font-size: 42px; font-weight: bold; color: #6c5ce7; text-align: center; }
    .hint { background-color: #dfe6e9; padding: 15px; border-radius: 10px; margin: 10px 0; font-size: 16px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">💪 근육 초성 퀴즈</div>', unsafe_allow_html=True)

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

# 사용자 입력 비교 함수
def normalize(text):
    return text.replace(" ", "").strip()

# 세션 상태 초기화
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = random.sample(chosung_data, len(chosung_data))
    st.session_state.q_index = 0
    st.session_state.score = 0

# 퀴즈 진행
if st.session_state.q_index < len(st.session_state.quiz_data):
    q = st.session_state.quiz_data[st.session_state.q_index]
    st.markdown(f"### 문제 {st.session_state.q_index + 1} / {len(st.session_state.quiz_data)}")
    st.markdown(f"**초성:** `{q['chosung']}`")
    st.markdown(f"<div class='hint'>💡 힌트: {q['hint']}</div>", unsafe_allow_html=True)

    with st.form("quiz_form", clear_on_submit=True):
        user_input = st.text_input("정답을 입력하세요 (한글)", key="answer_input")
        submitted = st.form_submit_button("제출")

        if submitted:
            if normalize(user_input) == normalize(q["name"]):
                st.success("✅ 정답입니다!")
                st.session_state.score += 1
            else:
                st.error(f"❌ 오답입니다. 정답은 **{q['name']}** 입니다.")
            st.session_state.q_index += 1
            st.experimental_rerun()

else:
    st.balloons()
    st.markdown(f"## 🎉 퀴즈 완료! 점수: **{st.session_state.score} / {len(st.session_state.quiz_data)}**")
    if st.button("🔁 다시 시작하기"):
        del st.session_state.quiz_data
        st.experimental_rerun()

