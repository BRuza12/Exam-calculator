import streamlit as st
import os
import datetime

# Настройки страницы с тёмной темой
st.set_page_config(page_title="📊 Калькулятор экзамена", page_icon="📘", layout="wide")

# Настраиваем кастомный фон и стили (тёмная тема)
st.markdown("""
    <style>
        body {
            background-color: #1e1e2f;
            color: #f5f5f5;
        }
        .stApp {
            background-color: #1e1e2f;
        }
    </style>
""", unsafe_allow_html=True)

# Функция логирования аналитики — записывает каждое нажатие кнопки в файл analytics_log.txt
def log_event():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("analytics_log.txt", "a") as f:
        f.write(f"{now} - Рассчитано\n")

# Заголовок и описание
st.title("📘 Калькулятор финального экзамена")
st.markdown("Введите баллы за 4 промежуточных экзамена, чтобы узнать, какой балл нужен на финальном, чтобы пройти.")
st.divider()

# Ввод оценок – располагаем поля в 4 колонки
st.subheader("✏️ Введите баллы")
col1, col2, col3, col4 = st.columns(4)
with col1:
    e1 = st.number_input("Экзамен 1", min_value=0.0, max_value=100.0, value=0.0)
with col2:
    e2 = st.number_input("Экзамен 2", min_value=0.0, max_value=100.0, value=0.0)
with col3:
    e3 = st.number_input("Экзамен 3", min_value=0.0, max_value=100.0, value=0.0)
with col4:
    e4 = st.number_input("Экзамен 4", min_value=0.0, max_value=100.0, value=0.0)

st.divider()

# Расчёт результата и логирование события
if st.button("📐 Рассчитать результат"):
    log_event()  # Записываем событие в аналитический лог
    avg = (e1 + e2 + e3 + e4) / 4
    required_final = (70 - 0.4 * avg) / 0.6

    st.metric(label="Средний балл", value=f"{avg:.2f}")
    st.progress(min(avg, 100) / 100)

    if required_final > 100:
        st.error(f"❌ Даже 100 баллов не хватит. Нужно: **{required_final:.2f}**")
    elif required_final <= 0:
        st.success("✅ Поздравляем! Вы уже прошли.")
        st.balloons()
    else:
        st.info(f"ℹ️ Нужно набрать минимум **{required_final:.2f}** баллов на финальном экзамене.")

# Блок для просмотра аналитики (логов)
if st.checkbox("Показать аналитику"):
    password = st.text_input("Введите пароль для доступа к аналитике", type="password")
    if password == "qweasd123":  # Замените "мойсекрет" на свой собственный пароль
        if os.path.exists("analytics_log.txt"):
            with open("analytics_log.txt", "r") as f:
                logs = f.readlines()
            st.text(f"Всего расчетов: {len(logs)}")
            st.text_area("Логи аналитики", "".join(logs), height=200)
        else:
            st.info("Аналитика пока отсутствует.")
    elif password:
        st.warning("Неверный пароль")
