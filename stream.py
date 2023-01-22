import io
import streamlit as st
from PIL import Image
from transformers import pipeline

@st.cache(allow_output_mutation=True)
def load_pipe():
    return pipeline(model="sberbank-ai/rugpt3large_based_on_gpt2")



def get_text():
    
    """Создание формы для набора текста"""
    
    # Форма для загрузки изображения средствами Streamlit
    text_in = st.text_input(
        label='Наберите текст')
    if text_in:
        st.write("You entered: ", text_in)
        return text_in


pipe = load_pipe()

# Выводим заголовок страницы средствами Streamlit     
st.title('Продолжаем фразу')
# Вызываем функцию для набора текста
txt = get_text()

result = st.button('ЗАПУСК РАСЧЕТА ЭВМ')



def print_predictions(txt: str):
    return pipe(txt)[0]['generated_text']


if result:
    for_print = print_predictions(txt)
    st.write('результат: ','\n', for_print)