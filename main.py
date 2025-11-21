import streamlit as st

st.set_page_config(page_title="MBTI 진로 상담", page_icon="🎓")

st.title("🎓 MBTI 진로 상담 웹앱")
st.write("아래에서 자신의 MBTI 유형을 선택하면, 성향에 맞는 3가지 진로를 추천해드립니다! 🌱")

# MBTI 리스트
mbti_list = [
    "ISTJ","ISFJ","INFJ","INTJ",
    "ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP",
    "ESTJ","ESFJ","ENFJ","ENTJ"
]

# 각 MBTI에 대한 진로 추천
careers = {
    "ISTJ": ["회계사 📊", "프로젝트 매니저 📁", "데이터 분석가 🔍"],
    "ISFJ": ["간호사 🏥", "교사 🍎", "인사 담당자 🤝"],
    "INFJ": ["상담가 💬", "작가 ✍️", "심리학자 🧠"],
    "INTJ": ["과학자 🔬", "소프트웨어 개발자 💻", "전략 기획자 ♟️"],
    "ISTP": ["엔지니어 ⚙️", "정비사 🔧", "기술 전문가 🛠️"],
    "ISFP": ["디자이너 🎨", "사진가 📷", "수의사 🐾"],
    "INFP": ["작가 📚", "상담사 🌿", "사회복지사 🤲"],
    "INTP": ["연구원 🔎", "프로그래머 🖥️", "시스템 분석가 🧩"],
    "ESTP": ["기업가 🚀", "영업 전문가 💼", "스포츠 코치 🏅"],
    "ESFP": ["공연예술가 🎭", "이벤트 플래너 🎉", "여행 컨설턴트 ✈️"],
    "ENFP": ["크리에이티브 디렉터 🎨", "마케팅 전략가 📣", "라이프 코치 🌈"],
    "ENTP": ["스타트업 창업가 🚀", "컨설턴트 💡", "발명가 ⚡"],
    "ESTJ": ["운영 관리자 🏭", "경찰관 🚓", "행정 관리자 📘"],
    "ESFJ": ["간호사 🩺", "고객 지원 🤗", "커뮤니티 매니저 🏘️"],
    "ENFJ": ["교사 👩‍🏫", "연설가 🎤", "비영리 단체 리더 ❤️"],
    "ENTJ": ["CEO 🏢", "비즈니스 전략가 📈", "경영 컨설턴트 🧠"]
}

# 사용자 선택
user_mbti = st.selectbox("MBTI 유형을 선택하세요:", mbti_list)

if user_mbti:
    st.subheader(f"✨ **{user_mbti}** 유형에게 추천하는 진로")
    for c in careers[user_mbti]:
        st.write(f"- {c}")
