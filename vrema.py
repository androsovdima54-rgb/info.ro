import streamlit as st
from datetime import datetime
import pytz
import random
import pandas as pd

# Настройка страницы
st.set_page_config(page_title="Romania Portal", page_icon="🇷🇴", layout="wide")

# Данные для карты (центр Бухареста)
bucharest_coords = pd.DataFrame(
    [[44.43225, 26.10626]],
    columns=['lat', 'lon']
)

# --- ГЛАВНЫЙ ИНТЕРФЕЙС ---
st.title("🇷🇴 Romania Info Portal")

# Время и дата
romania_tz = pytz.timezone('Europe/Bucharest')
now = datetime.now(romania_tz)

col_time, col_date = st.columns(2)
with col_time:
    st.metric("⌚ Время в Бухаресте", now.strftime("%H:%M:%S"))
with col_date:
    st.metric("📅 Сегодняшняя дата", now.strftime("%d.%m.%Y"))

st.divider()

# --- ОСНОВНОЙ КОНТЕНТ ---
left_col, right_col = st.columns([1, 2])

with left_col:
    st.subheader("🇷🇴 Учим румынский")
    phrases = [
        {"ro": "Bună ziua!", "ru": "Добрый день!"},
        {"ro": "Cât costă?", "ru": "Сколько это стоит?"},
        {"ro": "Nu înțeleg.", "ru": "Я не понимаю."},
        {"ro": "O zi bună!", "ru": "Хорошего дня!"},
        {"ro": "Noroc!", "ru": "Удачи!"}
    ]
    
    if 'phrase' not in st.session_state:
        st.session_state.phrase = random.choice(phrases)
    
    st.info(f"**{st.session_state.phrase['ro']}** \n\n — {st.session_state.phrase['ru']}")
    
    if st.button("🎲 Сменить фразу"):
        st.session_state.phrase = random.choice(phrases)
        st.rerun()

    st.write("---")
    st.subheader("💵 Курсы валют")
    st.write("1 EUR ≈ 4.97 RON")
    st.write("1 USD ≈ 4.62 RON")

with right_col:
    st.subheader("📍 Ты здесь (Бухарест)")
    # Рисуем карту
    st.map(bucharest_coords, zoom=12)

# --- НИЖНЯЯ ПАНЕЛЬ ---
st.divider()
if st.button("🚀 ЗАПУСТИТЬ ПРАЗДНИК"):
    st.balloons()
    st.snow()
    st.toast("Праздник к нам приходит!")

st.caption(f"Сайт запущен из файла: vrema.py | Последнее обновление: {now.strftime('%H:%M')}")