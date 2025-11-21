import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 데이터 로드 및 전처리
@st.cache_data
def load_data(file_path):
    """CSV 파일을 읽어 DataFrame을 반환합니다."""
    try:
        df = pd.read_csv(file_path)
        # MBTI 컬럼 이름 (첫 번째 'Country' 컬럼 제외)
        mbti_types = df.columns[1:].tolist()
        return df, mbti_types
    except FileNotFoundError:
        st.error(f"오류: 파일을 찾을 수 없습니다. '{file_path}' 파일이 같은 경로에 있는지 확인해주세요.")
        return None, None
    except Exception as e:
        st.error(f"데이터 로딩 중 오류 발생: {e}")
        return None, None

# 2. Plotly 그래프 생성 함수
def create_bar_chart(df, mbti_type, title, ascending=False):
    """
    MBTI 비율을 기준으로 상위/하위 10개국 막대 그래프를 생성합니다.
    """
    # 선택된 MBTI 비율을 기준으로 정렬
    if ascending:
        # 가장 낮은 10개국
        data_to_plot = df.sort_values(by=mbti_type, ascending=True).head(10)
    else:
        # 가장 높은 10개국
        data_to_plot = df.sort_values(by=mbti_type, ascending=False).head(10)
    
    # Plotly 막대 그래프 생성
    fig = px.bar(
        data_to_plot,
        x='Country', 
        y=mbti_type,
        title=title,
        # 정렬 순서에 맞게 x축 순서 지정
        category_orders={"Country": data_to_plot['Country'].tolist()},
        labels={'Country': '국가', mbti_type: f'{mbti_type} 비율'},
        color=mbti_type, # 비율에 따라 막대 색상 변화
        color_continuous_scale=px.colors.sequential.Viridis # 색상 스케일
    )
    
    # 레이아웃 업데이트 (보기 좋게 조정)
    fig.update_layout(
        xaxis_title='국가',
        yaxis_title=f'{mbti_type} 비율 (0~1)',
        hovermode="x unified",
        title_font_size=20,
        margin=dict(t=50, b=20)
    )
    
    # 비율을 백분율로 표시
    fig.update_traces(hovertemplate='%{y:.2%}<extra></extra>')
    
    return fig

# 3. Streamlit 앱 메인 함수
def main():
    st.set_page_config(
        page_title="MBTI 국가별 비율 분석",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.title("🌍 MBTI 국가별 비율 TOP & BOTTOM 10 분석")
    st.markdown("---")
    
    # 데이터 로드
    file_path = "countriesMBTI_16types.csv"
    df, mbti_types = load_data(file_path)
    
    if df is None:
        return

    # 사이드바에 MBTI 선택 드롭다운 생성
    st.sidebar.header("⚙️ 분석 설정")
    selected_mbti = st.sidebar.selectbox(
        "분석할 MBTI 유형을 선택하세요:",
        mbti_types
    )

    # 4. 가장 높은 나라 10개 그래프
    st.header(f"📈 {selected_mbti} 비율이 **가장 높은** 국가 10")
    st.markdown(f"**선택된 유형:** `{selected_mbti}`")
    
    top_10_chart = create_bar_chart(
        df, 
        selected_mbti, 
        title=f'{selected_mbti} 비율 TOP 10 국가', 
        ascending=False
    )
    st.plotly_chart(top_10_chart, use_container_width=True)
    
    st.markdown("---")
    
    # 5. 가장 적은 나라 10개 그래프
    st.header(f"📉 {selected_mbti} 비율이 **가장 낮은** 국가 10")
    
    bottom_10_chart = create_bar_chart(
        df, 
        selected_mbti, 
        title=f'{selected_mbti} 비율 BOTTOM 10 국가', 
        ascending=True
    )
    st.plotly_chart(bottom_10_chart, use_container_width=True)

if __name__ == "__main__":
    main()
