# Personal_project


개인 프로젝트 소개 
---

KeywordVisualizerApp


import sys
sys.path.append("D:\_DeepNLP\mylib\KeywordVisualizerApp\lib")

from konlpy.tag import Okt #한국어 품사태깅 
import lib.STVisualizer as stv # 자체적인 라이브러리 사용
import lib.myTextmining as tm # 자체적인 라이브러리 사용
import numpy as np #넘파이 수학 함수
import pandas as pd #판다스 데이터 프레임 함수
import streamlit as st #스트림릿 사용함수
import matplotlib.pyplot as plt # 파이썬 데이터 시각화 함수
import os #파이썬 운영처리 접속 함수

if "user_input"  not in st.session_state:
    st.session_state.user_input = None
if "option_1"  not in st.session_state:
    st.session_state.option_1 = False
if "option_2"  not in st.session_state:
    st.session_state.option_2 = False
if "number1"  not in st.session_state:
    st.session_state.number1 = None
if "number2" not in st.session_state:
    st.session_state.number2 = None
if "loaded_df" not in st.session_state:
    st.session_state.loaded_df = None
#스트림릿 내부에서 사용할 사용자 인풋 데이터 정의
  
st.title(" 데이터 확인 대시보드")
save_path= "D:/_DeepNLP/mylib/KeywordVisualizerApp/uploaded_file.csv"
# 파일 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file,encoding="utf-8")  #  업로드된 파일을 pandas DataFrame으로 변환
        
        df.to_csv(save_path, index=False, encoding="utf-8")
        st.write("업로드한 데이터 미리보기:")
        st.success(f"파일이 {save_path} 에 저장되었습니다.")
        st.write(" 데이터 미리보기:")
        st.dataframe(df)  #  DataFrame을 Streamlit에 출력
    except Exception as e:
        st.error(f" 파일을 읽는 중 오류 발생: {e}")
else:
    st.warning(" CSV 파일을 업로드하세요.") 
if uploaded_file :
    # CSV 파일 읽기
    # 데이터 미리보기
    st.subheader(" 데이터 미리보기")
    st.write(df.head())
    # 특정 컬럼 선택
    
    columns = df.columns.tolist()
    selected_columns = st.multiselect("확인할 컬럼 선택", columns, default=columns[:2])
    if selected_columns: # 컬럼을 선택해 사용자가 칼럼에 뭐 들어갔는지 확인하기 위한 칼럼목록
        st.subheader(" 선택한 컬럼 데이터")
        st.write(df[selected_columns])

font_path = "c:/Windows/fonts/malgun.ttf"  


user_input = st.text_input("파일의 속성을 입력하세요:")
if user_input:
    st.success(f"입력한 파일의 속성: {user_input}")

option_1 = st.checkbox("수평선 그래프",key = "option_1")
number1 = st.slider("값을 선택하세요", min_value=10, max_value=50, value=20)#,key = "number1"

option_2 = st.checkbox("산점도",key = "option_2")
number2 = st.slider("값을 선택하세요", min_value=20, max_value=500, value=50)#,key = "number2"


#plt 데이터를 fig로 바꾸어 넘겨서 명시적으로 fig를 사용하는걸 권장함 
if st.button("분석시작"):
    if os.path.exists(save_path):
            fig = stv.bchart(save_path,st.session_state.option_1,st.session_state.number1) 
            fig1 = stv.wordc(save_path,st.session_state.option_2,st.session_state.number2)

            if fig:
             st.pyplot(fig)
            else:
                print("이거 아님 ?")

            if fig1:
                st.pyplot(fig1)         
         
![이미지](https://github.com/siwon456/Personal_project/blob/main/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202025-04-09%20173602.png)
