import streamlit as st

st.set_page_config(page_title="Калькулятор экзамена", page_icon="📊")

st.title("Калькулятор для перехода на следующий курс")
st.markdown("Вводите баллы за 4 промежуточных экзамена — и узнаете, сколько нужно на финальном!")

e1 = st.number_input("Баллы за экзамен 1", min_value=0.0, max_value=100.0, value=0.0)
e2 = st.number_input("Баллы за экзамен 2", min_value=0.0, max_value=100.0, value=0.0)
e3 = st.number_input("Баллы за экзамен 3", min_value=0.0, max_value=100.0, value=0.0)
e4 = st.number_input("Баллы за экзамен 4", min_value=0.0, max_value=100.0, value=0.0)

if st.button("Рассчитать"):
    avg = (e1 + e2 + e3 + e4) / 4
    required_final = (70 - 0.4 * avg) / 0.6

    if required_final > 100:
        st.error(f"Увы, даже 100 баллов не хватит — нужно {required_final:.2f}.")
    elif required_final <= 0:
        st.success("Поздравляем! Вы уже прошли без финального экзамена!")
    else:
        st.success(f"Вам нужно набрать минимум {required_final:.2f} баллов на финальном экзамене.")
