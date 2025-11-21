import streamlit as st

# 🌸 Lovely Pink Theme
st.set_page_config(page_title='MBTI 고전문학 추천', page_icon='📚', layout='centered')
st.markdown(
    """
    <style>
        body {
            background-color: #ffe6f2;
        }
        .title {
            color: #ff4da6;
            text-align: center;
            font-size: 40px;
            font-weight: bold;
        }
        .subtitle {
            color: #ff66b3;
            text-align: center;
            font-size: 20px;
        }
        .recommend-box {
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 0px 10px #ffb3d9;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 제목
st.markdown('<div class="title">🌸 MBTI 기반 고전문학 추천 웹 앱 🌸</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">학생들의 MBTI 유형에 맞춰 어울리는 고전을 추천해드려요! 📖✨</div>', unsafe_allow_html=True)

# MBTI 선택
type_selected = st.selectbox(
    "학생의 MBTI 유형을 선택해주세요 💕",
    ["INTJ", "INFP", "ENFP", "ISTJ", "ESFJ", "ENTP", "ISFP", "ESTJ", "ENTJ", "INFJ", "ISTP", "ENFJ", "ESFP", "ESTP", "ISFJ", "INTP"]
)

# 고전문학 추천 데이터
recommendations = {
    "INTJ": ("📘 '군주론' - 니콜로 마키아벨리", "분석적이고 전략적인 INTJ에게 딱 맞는 고전!"),
    "INFP": ("📗 '어린 왕자' - 생텍쥐페리", "감성적이고 이상주의적인 INFP에게 어울려요 💖"),
    "ENFP": ("📙 '변신' - 프란츠 카프카", "호기심 많은 ENFP에게 사고의 확장을! ✨"),
    "ISTJ": ("📕 '논어' - 공자", "전통과 원칙을 중시하는 ISTJ에게 잘 맞아요."),
    "ESFJ": ("📘 '작은 아씨들' - 루이자 메이 올컷", "따뜻함을 중요시하는 ESFJ에게 딱! 💞"),
    "ENTP": ("📗 '도덕경' - 노자", "새로운 시각을 좋아하는 ENTP에게 추천!"),
    "ISFP": ("📙 '월든' - 소로우", "자연과 조화를 사랑하는 ISFP에게 🌿"),
    "ESTJ": ("📕 '국가' - 플라톤", "체계적이고 실용적인 ESTJ에게 아주 적합!"),
    "ENTJ": ("📘 '손자병법' - 손자", "리더십 강한 ENTJ에게 전략적 도움 💡"),
    "INFJ": ("📗 '데미안' - 헤르만 헤세", "깊이 있는 성찰을 중시하는 INFJ에게 🌙"),
    "ISTP": ("📙 '노인과 바다' - 헤밍웨이", "실용적이고 모험심 있는 ISTP에게 어울려요."),
    "ENFJ": ("📕 '위대한 유산' - 찰스 디킨스", "타인을 돕는 ENFJ에게 따뜻한 메시지 💗"),
    "ESFP": ("📘 '돋보기 속의 세상' - 체스터턴", "즐거움을 추구하는 ESFP에게 ✨"),
    "ESTP": ("📗 '삼국지' - 나관중", "액션과 전략을 좋아하는 ESTP에게🔥"),
    "ISFJ": ("📙 '죄와 벌' - 도스토예프스키", "책임감 있는 ISFJ에게 깊이 있는 이야기 💭"),
    "INTP": ("📕 '괴테의 파우스트' - 괴테", "사고를 즐기는 INTP에게 철학적 자극!"),
}

# 추천 결과 출력
if type_selected:
    book, desc = recommendations[type_selected]
    st.markdown(f"<div class='recommend-box'><h3>{book}</h3><p>{desc}</p></div>", unsafe_allow_html=True)
