import streamlit as st
import pandas as pd
import altair as alt

# 1. 데이터 로드
# 업로드된 파일을 가정하고 직접 로드합니다.
# Streamlit Cloud에 배포할 때는 이 파일을 프로젝트 폴더에 함께 넣어두어야 합니다.
file_name = "countriesMBTI_16types.csv"
try:
    df = pd.read_csv(file_name)
    # 첫 번째 열을 'Country'로 설정
    df = df.rename(columns={df.columns[0]: 'Country'})
except FileNotFoundError:
    st.error(f"❌ 오류: 파일을 찾을 수 없습니다. 파일 이름이 '{file_name}'인지 확인해주세요.")
    st.stop()
except Exception as e:
    st.error(f"❌ 데이터 로드 중 오류가 발생했습니다: {e}")
    st.stop()

# 2. Streamlit 앱 설정
st.set_page_config(
    page_title="🌍 MBTI 국가별 분포 분석",
    layout="wide"
)

st.title("🌍 MBTI 유형별 국가 분포 대시보드")
st.markdown("---")

# MBTI 유형 목록 (Country 열 제외)
mbti_types = df.columns[1:].tolist()

# 3. 사용자 입력 (인터랙티브 선택)
selected_mbti = st.selectbox(
    "**분석할 MBTI 유형을 선택하세요:**",
    mbti_types,
    index=mbti_types.index('ENFP') if 'ENFP' in mbti_types else 0 # 기본값 설정
)

st.header(f"✨ {selected_mbti} 유형 분포 분석 결과")
st.markdown("---")

# 4. 데이터 처리 및 그래프 함수 정의

def create_bar_chart(data, title, color_field, sort_order):
    """Altair 막대 그래프를 생성하는 함수"""
    chart = alt.Chart(data).mark_bar().encode(
        # 정렬 순서 (높은 순 또는 낮은 순)
        x=alt.X(selected_mbti, title=f"'{selected_mbti}' 유형 비율", axis=None),
        y=alt.Y('Country', sort=sort_order, title="국가"),
        # 색상 인코딩
        color=alt.Color(color_field, scale=alt.Scale(range=['#1f77b4', '#d62728']), title=None, legend=None),
        # 툴팁 추가
        tooltip=['Country', alt.Tooltip(selected_mbti, format='.2%')]
    ).properties(
        title=title
    ).configure_axis(
        # Y축 라벨을 오른쪽으로 옮겨서 두 그래프를 나란히 볼 때 시각적 효과 개선
        orient='right' if sort_order == '-x' else 'left'
    ).interactive() # 줌 및 패닝 기능 추가

    return chart.to_streamlit(use_container_width=True) # Streamlit에 맞게 렌더링

# 선택된 MBTI 열을 기준으로 데이터 정렬
sorted_df = df[['Country', selected_mbti]].sort_values(by=selected_mbti, ascending=False).reset_index(drop=True)

# 5. 상위 10개 나라 분석 및 시각화
st.subheader("🥇 MBTI 유형별 **가장 높은** 나라 (상위 10개)")
top_10_df = sorted_df.head(10)

# 그래프 생성 및 표시
chart_top_10 = alt.Chart(top_10_df).mark_bar(color='#2ECC71').encode(
    x=alt.X(selected_mbti, title=f"'{selected_mbti}' 유형 비율", axis=alt.Axis(format='.1%')),
    y=alt.Y('Country', sort='-x', title="국가"),
    tooltip=['Country', alt.Tooltip(selected_mbti, format='.2%')]
).properties(
    title=f"'{selected_mbti}' 유형 비율 상위 10개 국가"
).interactive()

st.altair_chart(chart_top_10, use_container_width=True)

st.markdown("---")

# 6. 하위 10개 나라 분석 및 시각화
st.subheader("📉 MBTI 유형별 **가장 낮은** 나라 (하위 10개)")
bottom_10_df = sorted_df.tail(10).sort_values(by=selected_mbti, ascending=True).reset_index(drop=True)

# 그래프 생성 및 표시
chart_bottom_10 = alt.Chart(bottom_10_df).mark_bar(color='#E74C3C').encode(
    x=alt.X(selected_mbti, title=f"'{selected_mbti}' 유형 비율", axis=alt.Axis(format='.1%')),
    y=alt.Y('Country', sort='x', title="국가"),
    tooltip=['Country', alt.Tooltip(selected_mbti, format='.2%')]
).properties(
    title=f"'{selected_mbti}' 유형 비율 하위 10개 국가"
).interactive()

st.altair_chart(chart_bottom_10, use_container_width=True)
