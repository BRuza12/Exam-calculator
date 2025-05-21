import streamlit as st

# Настройки страницы с тёмной темой
st.set_page_config(
    page_title="📊 Калькулятор экзамена",
    page_icon="📘",
    layout="wide"
)

# Настроим кастомный фон и стиль через Markdown + HTML
st.markdown("""
    <style>
        body {
            background-color: #1e1e2f;
            color: #f5f5f5;
        }
        .stApp {
            background-color: #1e1e2f;
        }
        .st-bb {
            background-color: #2e2e3e !important;
            border-radius: 10px;
            padding: 10px;
        }
        .css-1cpxqw2 edgvbvh3 {
            background-color: #222;
        }
    </style>
""", unsafe_allow_html=True)

# Заголовок
st.title("📘 Калькулятор финального экзамена")
st.markdown("Введите баллы за 4 промежуточных экзамена, чтобы узнать, какой балл нужен на финальном, чтобы пройти.")
st.divider()

# Ввод оценок в колонках
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

# Кнопка и логика
if st.button("📐 Рассчитать результат"):
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
        st.info(f"ℹ️ Нужно набрать минимум **{required_final:.2f}** на финальном экзамене.")
