import streamlit as st

# Page settings
st.set_page_config(page_title="MBTI 진로 상담", page_icon="🎀")

# Custom CSS for lovely pink theme
st.markdown(
    """
    <style>
        body {
            background-color: #ffe6f2;
        }
        .stApp {
            background-color: #ffe6f2;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #d63384 !important;
        }
        .pink-box {
            padding: 15px;
            background: #ffd6e8;
            border-radius: 12px;
            border: 2px solid #ffb3d9;
            margin-bottom: 15px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎀 MBTI 진로 상담 웹앱")
st.write("당신의 MBTI를 선택하면, 사랑스러운 핑크 분위기 속에서 ✨맞춤 진로 추천✨을 보여드릴게요! 💗🌸")

# MBTI list
mbti_list = [
    "ISTJ","ISFJ","INFJ","INTJ",
    "ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP",
    "ESTJ","ESFJ","ENFJ","ENTJ"
]

# Career recommendations + explanations
talent_data = {
    "ISTJ": [
        ("회계사 📊", "체계적이고 책임감 있는 ISTJ에게 잘 맞는 직업입니다. 규정과 정확성을 중요하게 여깁니다."),
        ("프로젝트 매니저 📁", "실용적이고 계획적인 성향 덕분에 프로젝트를 안정적으로 이끌 수 있습니다."),
        ("데이터 분석가 🔍", "세부 사항에 강하며 분석적 사고를 활용해 문제 해결에 뛰어납니다.")
    ],
    "ISFJ": [
        ("간호사 🏥", "팀워크와 헌신적 성향이 돋보이는 직업입니다. 사람을 돌보는 일과 잘 맞습니다."),
        ("교사 🍎", "차분하고 따뜻한 성격으로 학생들에게 안정과 배움을 제공합니다."),
        ("인사 담당자 🤝", "조직 구성원의 행복과 발전을 돕는 역할에 적합합니다.")
    ],
    "INFJ": [
        ("상담가 💬", "사람의 마음을 깊이 이해하며 진심으로 돕고자 하는 INFJ에게 잘 맞아요."),
        ("작가 ✍️", "창의성과 통찰력을 글로 표현하는 데 뛰어납니다."),
        ("심리학자 🧠", "내면을 탐구하고 의미 있는 변화를 지원하는 역할이 어울립니다.")
    ],
    # ... (continue for all MBTI types using the same format)
}

user_mbti = st.selectbox("MBTI 유형을 선택하세요:", mbti_list)

if user_mbti:
    st.subheader(f"💖 {user_mbti} 유형에게 딱 맞는 진로 3가지")

    for career, desc in talent_data.get(user_mbti, []):
        st.markdown(f"<div class='pink-box'><strong>{career}</strong><br>{desc}</div>", unsafe_allow_html=True)
