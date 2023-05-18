import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.image as img
import seaborn as sns
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
from folium.plugins import MiniMap
from folium.plugins import MarkerCluster
import folium
import json
from data_loader import data_loader
from visualization import main_image
import base64
from pathlib import Path

plt.rc('font', family='NanumGothic') # For Windows
print(plt.rcParams['font.family'])

matplotlib.get_cachedir()

# '기준년월','주문시간','주문명','광역시도명','주소명','결제종류'

# background image to streamlit

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


with st.sidebar:
    choose = option_menu("Menu", ["Main", "구별", "시간별"],
                         icons=['house', 'camera fill', 'kanban'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

if choose == 'Main':
    st.title('배달 앱 소비 분석')

    data1 = data_loader()
    
    st.subheader(
        '서울시 지역구별 배달 건수 데이터를 바탕으로 지역구별 주문건수 통계량 및 시간대별 주문건수 통계량을 분석'
    )

    st.subheader('Raw data')
    st.write(data1)
    

    st.header('서울시 세부지역별 주문상품건수')
    main_image = img.imread('./seoul_image.PNG')
    st.image(main_image)
    st.write('구로구 > 영등포구 > 금천구 ... 순으로 배달 빈도가 높음')


    st.header('서울시 세대구성별 배달건수')
    sub_image = img.imread('./세대구성별_배달.PNG')
    st.image(sub_image)
    st.write('다세대 가구보다 1인, 2인 가구의 배달 주문 건수가 많음')
    st.write('')
    st.write('')
    st.write('')

    st.subheader('folium 를 사용한 서울시 구별 주문건수.....')
    geojson = json.load( open('./seoulsigungu.geojson',encoding='utf-8') )
    geojson['features'][0]['properties']
    df_order = data1['주소명'].value_counts()
    df_order = pd.DataFrame(df_order)
    
    #print(df_order)
    
    map = folium.Map( location = [37.5536067,126.9674308], zoom_start=11, tiles="CartoDB dark_matter" )

    folium.Choropleth(
    geo_data = geojson,
    columns = [df_order.index, '주소명'],   
    fill_color='YlOrRd',
    # fill_opacity = 0.7,
    # line_opacity=0.5,
    key_on = 'properties.SIG_KOR_NM'
    ).add_to(map)

    map

# 구별 배달건수
if choose == '구별':
     with st.sidebar:
        goo_list = ['구로구','금천구','도봉구','영등포구','서초구','은평구','강남구','동작구','양천구','서대문구','관악구','강동구','노원구','강서구']
        goo_select = st.selectbox('', goo_list)

if choose =='구별' and goo_select =='구로구':
    st.subheader('구로구 주문 상품 비율')
    gu_image = img.imread('./guro_image.PNG')
    st.image(gu_image)

if choose =='구별' and goo_select =='금천구':
    st.subheader('금천구 주문 상품 비율')
    gu_image = img.imread('./금천구.PNG')
    st.image(gu_image)

if choose =='구별' and goo_select =='도봉구':
    st.subheader('도봉구 주문 상품 비율')
    gu_image = img.imread('./도봉구.PNG')
    st.image(gu_image)

if choose =='구별' and goo_select =='영등포구':
    st.subheader('영등포구 주문 상품 비율')
    gu_image = img.imread('./영등포구.PNG')
    st.image(gu_image)

if choose == '시간별':
    st.subheader('시간대별 주문상품별 배달건수')
    time_image = img.imread('./시간대별_주문상품별_배달건수.PNG')
    st.image(time_image)

    st.subheader('24시간 동안 운영하는 배달 전문 업체의 주문건수는 점심/저녁 시간대를 중심으로 분포해 있음')
    st.subheader('')
    st.subheader('치킨, 분식, 패스트푸드가 공통적으로 많은 비중을 차지하고 있음')
