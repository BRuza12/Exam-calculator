import streamlit as st
import os
import datetime

# Настройки страницы
st.set_page_config(page_title="Калькулятор экзамена", page_icon="📊")

# Простая аналитика — логгируем в файл
def log_event():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("analytics_log.txt", "a") as f:
        f.write(f"{now} - Рассчитано\n")

# Заголовок
st.title("Сколько нужно набрать на финальном экзамене?")
st.markdown("Введите баллы за 4 промежуточных экзамена, чтобы узнать, какой балл нужен на финальном, чтобы пройти.")

st.divider()

# Ввод промежуточных оценок
st.subheader("Промежуточные экзамены")
e1 = st.number_input("Экзамен 1", min_value=0.0, max_value=100.0, value=0.0)
e2 = st.number_input("Экзамен 2", min_value=0.0, max_value=100.0, value=0.0)
e3 = st.number_input("Экзамен 3", min_value=0.0, max_value=100.0, value=0.0)
e4 = st.number_input("Экзамен 4", min_value=0.0, max_value=100.0, value=0.0)

# Расчёт
if st.button("Рассчитать"):
    log_event()  # логируем нажатие

    avg = (e1 + e2 + e3 + e4) / 4
    required_final = (70 - 0.4 * avg) / 0.6

    st.markdown(f"**Средний балл за промежуточные экзамены:** `{avg:.2f}`")

    if required_final > 100:
        st.error(f"К сожалению, даже 100 баллов не хватит. Нужно: **{required_final:.2f}**")
    elif required_final <= 0:
        st.success("Поздравляем! Вы уже прошли. Финальный экзамен можно не сдавать.")
    else:
        st.info(f"Чтобы пройти, нужно набрать на финальном экзамене минимум **{required_final:.2f}** баллов.")
