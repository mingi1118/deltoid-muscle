import streamlit as st
import random

# 🌈 페이지 설정
st.set_page_config(page_title="💪 인체 근육 퀴즈", page_icon="🦴", layout="centered")

# 🎨 기본 스타일
st.markdown("""
    <style>
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #d63031;
        text-align: center;
        margin-top: 20px;
    }
    .subtitle {
        font-size: 20px;
        text-align: center;
        color: #2d3436;
    }
    .question-box {
        background-color: #ffeaa7;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">💪 인체 근육 맞추기 퀴즈</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">몸의 주요 근육 30가지를 맞혀보세요! 단답형으로 입력하세요 🧠</div>', unsafe_allow_html=True)

# 🧠 주요 근육 문제 데이터
muscle_quiz = [
    {"korean": "가슴근", "english": "pectoralis major"},
    {"korean": "이두근", "english": "biceps brachii"},
    {"korean": "삼두근", "english": "triceps brachii"},
    {"korean": "승모근", "english": "trapezius"},
    {"korean": "삼각근", "english": "deltoid"},
    {"korean": "광배근", "english": "latissimus dorsi"},
    {"korean": "복직근", "english": "rectus abdominis"},
    {"korean": "외복사근", "english": "external oblique"},
    {"korean": "둔근", "english": "gluteus maximus"},
    {"korean": "햄스트링", "english": "hamstrings"},
    {"korean": "대퇴사두근", "english": "quadriceps"},
    {"korean": "종아리근", "english": "gastrocnemius"},
    {"korean": "경판상근", "english": "splenius capitis"},
    {"korean": "복횡근", "english": "transversus abdominis"},
    {"korean": "전완근", "english": "forearm flexors"},
    {"korean": "척추기립근", "english": "erector spinae"},
    {"korean": "경흉쇄근", "english": "sternocleidomastoid"},
    {"korean": "장요근", "english": "iliopsoas"},
    {"korean": "중둔근", "english": "gluteus medius"},
    {"korean": "장내전근", "english": "adductor longus"},
    {"korean": "전경골근", "english": "tibialis anterior"},
    {"korean": "대원근", "english": "teres major"},
    {"korean": "소원근", "english": "teres minor"},
    {"korean": "능형근", "english": "rhomboid"},
    {"korean": "상완삼두근", "english": "triceps brachii"},
    {"korean": "상완이두근", "english": "biceps brachii"},
    {"korean": "쇄골하근", "english": "subclavius"},
    {"korean": "횡격막", "english": "diaphragm"},
    {"korean": "대흉근", "english": "pectoralis major"},
]

# 세션 상태 관리
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.q_index = 0
    st.session_state.quiz = random.sample(muscle_quiz, 30)

# 현재 문제
current = st.session_state.quiz[st.session_state.q_index]
st.markdown(f"<div class='question-box'>🦴 <b>Q{st.session_state.q_index + 1}</b>: '{current['korean']}'의 영어 이름은?</div>", unsafe_allow_html=True)

# ✍️ 사용자 입력
answer = st.text_input("정답 입력 (예: biceps brachii)").strip().lower()

if st.button("제출"):
    if answer == current['english']:
        st.success("🎉 정답입니다!")
        st.session_state.score += 1
    else:
        st.error(f"❌ 오답입니다. 정답은 **{current['english']}** 입니다.")
    
    st.session_state.q_index += 1

    if st.session_state.q_index >= len(st.session_state.quiz):
        st.balloons()
        st.markdown(f"## ✅ 퀴즈 종료! 총 점수: **{st.session_state.score} / 30**")
        st.markdown("🔄 새로고침해서 다시 시작할 수 있어요.")
        st.stop()
    else:
        st.experimental_rerun()

