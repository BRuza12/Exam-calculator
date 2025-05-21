import streamlit as st
import streamlit.components.v1 as components

# Настройки страницы
st.set_page_config(page_title="Калькулятор экзамена", page_icon="📊")

# Встраиваем Google Analytics через HTML компонент с sandbox
components.html(
    """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-DFMK70428K"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-DFMK70428K');
    </script>
    """,
    height=0,
    scrolling=False,
    # sandbox режим отключён, чтобы скрипты работали
    # можно добавить, если будет ошибка: sandbox="allow-scripts allow-same-origin"
)

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
    avg = (e1 + e2 + e3 + e4) / 4
    required_final = (70 - 0.4 * avg) / 0.6

    st.markdown(f"**Средний балл за промежуточные экзамены:** `{avg:.2f}`")

    if required_final > 100:
        st.error(f"К сожалению, даже 100 баллов не хватит. Нужно: **{required_final:.2f}**")
    elif required_final <= 0:
        st.success("Поздравляем! Вы уже прошли. Финальный экзамен можно не сдавать.")
    else:
        st.info(f"Чтобы пройти, нужно набрать на финальном экзамене минимум **{required_final:.2f}** баллов.")
