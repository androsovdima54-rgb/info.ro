import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# Настройка стиля "Киберпанк"
st.set_page_config(page_title="Command Hub", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b0d14; color: #00ff41; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: #161b22; border-radius: 10px 10px 0 0; color: #00ff41; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ COMMAND CENTER v3.0")

# Вкладки для разного контента
tab1, tab2, tab3 = st.tabs(["📊 Аналитика", "📝 Заметки", "🎮 Интерактив"])

with tab1:
    st.subheader("Системные показатели")
    col1, col2, col3 = st.columns(3)
    
    # Индикаторы загрузки (выглядят очень "программистски")
    with col1:
        cpu = st.slider("Загрузка CPU", 0, 100, 45)
        st.progress(cpu)
    with col2:
        ram = st.slider("Использование RAM", 0, 100, 72)
        st.progress(ram)
    with col3:
        st.metric("Активные процессы", "128", "+12")

    st.write("### График нейросети (Симуляция)")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Alpha', 'Beta', 'Gamma'])
    st.area_chart(chart_data)

with tab2:
    st.subheader("Секретный архив данных")
    msg = st.text_area("Добавить запись в зашифрованный лог:")
    if st.button("ЗАШИФРОВАТЬ И СОХРАНИТЬ"):
        with st.spinner('Шифрование по протоколу AES-256...'):
            time.sleep(2)
            st.success("Данные успешно упакованы в блокчейн!")
            st.info(f"Запись: {msg}")

with tab3:
    st.subheader("Визуальная лаборатория")
    color = st.color_picker("Выбери цвет интерфейса", "#00ff41")
    st.write(f"Выбранный HEX-код: `{color}`")
    
    # Маленькая "рисовалка" или график
    st.write("Рисуй данные прямо здесь:")
    map_data = pd.DataFrame(
        np.random.randn(5, 2) / [50, 50] + [44.43, 26.10],
        columns=['lat', 'lon']
    )
    st.map(map_data)

st.sidebar.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXZueXJueXJueXJueXJueXJueXJueXJueXJueXJueXJueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKSjPXYphOGpnyo/giphy.gif")
st.sidebar.write("---")
st.sidebar.write("**Статус:** Защищено")
if st.sidebar.button("САМОУНИЧТОЖЕНИЕ"):
    st.warning("Запуск протокола через 3... 2... 1...")
    st.snow() # Вместо взрыва пойдет снег, это их расслабит :)