import streamlit as st

st.set_page_config(page_title="Калькулятор экзамена", page_icon="📊")

st.title("Сколько нужно набрать на финальном экзамене?")
st.markdown("Вводите баллы за 4 промежуточных экзамена — и узнаете, сколько нужно на финальном, чтобы пройти!")

st.divider()

st.subheader("Промежуточные экзамены")
e1 = st.number_input("Экзамен 1", min_value=0.0, max_value=100.0, value=0.0)
e2 = st.number_input("Экзамен 2", min_value=0.0, max_value=100.0, value=0.0)
e3 = st.number_input("Экзамен 3", min_value=0.0, max_value=100.0, value=0.0)
e4 = st.number_input("Экзамен 4", min_value=0.0, max_value=100.0, value=0.0)

if st.button("Рассчитать"):
    avg = (e1 + e2 + e3 + e4) / 4
    required_final = (70 - 0.4 * avg) / 0.6

    st.markdown(f"**Средний балл за промежуточные:** {avg:.2f}")
    if required_final > 100:
        st.error(f"Даже 100 баллов не хватит — нужно {required_final:.2f}.")
    elif required_final <= 0:
        st.success("Вы уже прошли! Финал можно не сдавать.")
    else:
        st.info(f"Нужно набрать как минимум **{required_final:.2f}** на финальном экзамене.")
