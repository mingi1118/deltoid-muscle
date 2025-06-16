import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="💪 근육 초성 퀴즈", page_icon="🧠", layout="centered")

st.markdown("""
    <style>
    .title { font-size: 42px; font-weight: bold; color: #6c5ce7; text-align: center; }
    .hint { background-color: #dfe6e9; padding: 15px; border-radius: 10px; margin: 10px 0; font-size: 16px; }
    .explanation { background-color: #ffeaa7; padding: 10px; border-radius: 10px; margin-top: 10px; font-size: 15px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">💪 근육 초성 퀴즈</div>', unsafe_allow_html=True)

# 근육 데이터에 설명 추가
chosung_data = [
    {"name": "삼각근", "chosung": "ㅅㄱㄱ", "hint": "어깨에 위치", "explanation": "삼각근은 어깨를 감싸고 있는 근육으로, 팔을 들어 올리는 역할을 합니다."},
    {"name": "이두근", "chosung": "ㅇㄷㄱ", "hint": "팔 앞쪽", "explanation": "이두근은 팔 앞쪽에 위치하며, 팔을 구부리는 힘을 담당합니다."},
    {"name": "삼두근", "chosung": "ㅅㄷㄱ", "hint": "팔 뒤쪽", "explanation": "삼두근은 팔 뒤쪽에 있으며, 팔을 펴는 역할을 합니다."},
    {"name": "대흉근", "chosung": "ㄷㅎㄱ", "hint": "가슴 근육", "explanation": "대흉근은 가슴 앞쪽에 위치한 근육으로, 팔을 모으거나 돌리는 역할을 합니다."},
    {"name": "광배근", "chosung": "ㄱㅂㄱ", "hint": "등 넓은 근육", "explanation": "광배근은 등 아래쪽에 넓게 퍼진 근육으로, 팔을 당기는 동작에 관여합니다."},
    {"name": "복직근", "chosung": "ㅂㅈㄱ", "hint": "복근", "explanation": "복직근은 복부에 위치해 몸을 앞으로 굽히는 역할을 합니다."},
    {"name": "둔근", "chosung": "ㄷㄱ", "hint": "엉덩이", "explanation": "둔근은 엉덩이 부위 근육으로, 다리를 뒤로 뻗거나 엉덩이를 움직이는 역할을 합니다."},
    {"name": "햄스트링", "chosung": "ㅎㅅㅌㄹ", "hint": "허벅지 뒤", "explanation": "햄스트링은 허벅지 뒤쪽에 위치해 무릎을 구부리는 역할을 합니다."},
    {"name": "대퇴사두근", "chosung": "ㄷㅌㅅㄷㄱ", "hint": "허벅지 앞", "explanation": "대퇴사두근은 허벅지 앞쪽의 큰 근육으로, 무릎을 펴는 역할을 합니다."},
    {"name": "종아리근", "chosung": "ㅈㅇㄹㄱ", "hint": "종아리", "explanation": "종아리근은 종아리 뒤쪽에 있으며, 발끝을 아래로 누르는 역할을 합니다."},
]

def normalize(text):
    return text.replace(" ", "").strip()

if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = random.sample(chosung_data, len(chosung_data))
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.feedback = None  # 정답/오답 메시지 저장
    st.session_state.explanation = None  # 설명 저장

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
                st.session_state.feedback = "✅ 정답입니다!"
                st.session_state.score += 1
            else:
                st.session_state.feedback = f"❌ 오답입니다. 정답은 **{q['name']}** 입니다."
            st.session_state.explanation = q["explanation"]
            st.session_state.q_index += 1
            st.rerun()

    # 제출 후 메시지와 설명 보여주기
    if st.session_state.feedback:
        st.markdown(st.session_state.feedback)
    if st.session_state.explanation:
        st.markdown(f"<div class='explanation'>💡 설명: {st.session_state.explanation}</div>", unsafe_allow_html=True)

else:
    st.balloons()
    st.markdown(f"## 🎉 퀴즈 완료! 점수: **{st.session_state.score} / {len(st.session_state.quiz_data)}**")
    if st.button("🔁 다시 시작하기"):
        del st.session_state.quiz_data
        del st.session_state.feedback
        del st.session_state.explanation
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.rerun()

