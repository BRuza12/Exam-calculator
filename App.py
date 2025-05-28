import streamlit as st
import datetime
import pytz
import os

# --- Настройки страницы ---
st.set_page_config(page_title="Exam Calculator", page_icon="📘", layout="wide")

# --- Переводы ---
translations = {
    "ru": {
        "title": "📘 Калькулятор финального экзамена",
        "desc": "Введите баллы за 4 промежуточных экзамена, чтобы узнать, какой балл нужен на финальном, чтобы пройти.",
        "exam": "Экзамен",
        "button": "📐 Рассчитать результат",
        "avg": "Средний балл",
        "error": "❌ Даже 100 баллов не хватит. Нужно:",
        "success": "✅ Поздравляем! Вы уже прошли.",
        "info": "ℹ️ Нужно набрать минимум",
        "analytics": "Показать аналитику",
        "password": "Введите пароль для доступа к аналитике",
        "wrong_password": "Неверный пароль",
        "empty_log": "Лог пустой.",
        "total": "Всего расчётов"
    },
    "en": {
        "title": "📘 Final Exam Calculator",
        "desc": "Enter scores from 4 midterms to find out what you need on the final to pass.",
        "exam": "Exam",
        "button": "📐 Calculate Result",
        "avg": "Average Score",
        "error": "❌ Even 100 points won't be enough. Required:",
        "success": "✅ Congrats! You've already passed.",
        "info": "ℹ️ You need at least",
        "analytics": "Show Analytics",
        "password": "Enter password to access analytics",
        "wrong_password": "Wrong password",
        "empty_log": "Log is empty.",
        "total": "Total calculations"
    },
    "kg": {
        "title": "📘 Финалдык экзамен калькулятору",
        "desc": "Акыркы экзаменден өтүү үчүн эмне алуу керек экенин билүү үчүн 4 аралык баллды киргизиңиз.",
        "exam": "Экзамен",
        "button": "📐 Натыйжаны эсепте",
        "avg": "Орточо балл",
        "error": "❌ Атүгүл 100 балл жетпейт. Керек:",
        "success": "✅ Куттуктайм! Сиз өттүңүз.",
        "info": "ℹ️ Акыркы экзаменде алуу керек:",
        "analytics": "Аналитиканы көрсөтүү",
        "password": "Аналитикага кирүү үчүн сырсөздү киргизиңиз",
        "wrong_password": "Сырсөз туура эмес",
        "empty_log": "Лог бош.",
        "total": "Бардык эсептөөлөр"
    },
    "tr": {
        "title": "📘 Final Sınav Hesaplayıcı",
        "desc": "Finalden geçmek için kaç puan almanız gerektiğini öğrenmek için 4 ara sınav notunuzu girin.",
        "exam": "Sınav",
        "button": "📐 Sonucu Hesapla",
        "avg": "Ortalama Puan",
        "error": "❌ 100 puan bile yetmez. Gerekli:",
        "success": "✅ Tebrikler! Zaten geçtiniz.",
        "info": "ℹ️ Finalde en az",
        "analytics": "Analitiği Göster",
        "password": "Analitiğe erişmek için şifre girin",
        "wrong_password": "Yanlış şifre",
        "empty_log": "Kayıt boş.",
        "total": "Toplam hesaplama"
    }
}

# --- Язык ---
lang = st.selectbox("🌐 Язык / Language / Тил / Dil", ["ru", "en", "kg", "tr"], format_func=lambda x: {
    "ru": "Русский 🇷🇺", "en": "English 🇬🇧", "kg": "Кыргызча 🇰🇬", "tr": "Türkçe 🇹🇷"
}[x])
t = translations[lang]

# --- Интерфейс ---
st.title(t["title"])
st.markdown(t["desc"])
st.divider()

col1, col2, col3, col4 = st.columns(4)
with col1: e1 = st.number_input(f"{t['exam']} 1", 0.0, 100.0, 0.0)
with col2: e2 = st.number_input(f"{t['exam']} 2", 0.0, 100.0, 0.0)
with col3: e3 = st.number_input(f"{t['exam']} 3", 0.0, 100.0, 0.0)
with col4: e4 = st.number_input(f"{t['exam']} 4", 0.0, 100.0, 0.0)

if st.button(t["button"]):
    avg = (e1 + e2 + e3 + e4) / 4
    required_final = (70 - 0.4 * avg) / 0.6
    st.metric(t["avg"], f"{avg:.2f}")

    if required_final > 100:
        st.error(f"{t['error']} **{required_final:.2f}**")
    elif required_final <= 0:
        st.success(t["success"])
        st.balloons()
    else:
        st.info(f"{t['info']} **{required_final:.2f}**")

    # --- Логирование в файл ---
    tz = pytz.timezone("Asia/Bishkek")
    now = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"{now} — avg: {avg:.2f}, required: {required_final:.2f}\n")

# --- Просмотр аналитики (по паролю) ---
st.divider()
with st.expander(t["analytics"]):
    pw = st.text_input(t["password"], type="password")
    if pw == "analiz123":  # 🔐 Измени по желанию
        if os.path.exists("log.txt"):
            with open("log.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
                st.metric(t["total"], len(lines))
                st.code("".join(lines[-10:]), language="text")
        else:
            st.warning(t["empty_log"])
    elif pw:
        st.error(t["wrong_password"])
