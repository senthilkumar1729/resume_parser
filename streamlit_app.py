import streamlit as st
import textract
import spacy
import tempfile
from utils import get_skills, clean_resume, plot_pie, get_matching_skills


@st.experimental_singleton
def get_model():
    nlp = spacy.load("en_core_web_sm")
    entity_pattern = "temp.jsonl"
    ruler = nlp.add_pipe("entity_ruler")
    ruler.from_disk(entity_pattern)
    return nlp


st.write("Hello world")
model = get_model()
#required_skills = st.text_input(
 #   "Enter skills seperated by a commma").lower().split(',')


uploaded_file = st.file_uploader("Upload pdf")
text = ''
if st.button("Parse resume and get skills"):
    st.write('Parsing')
    context = None

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
        temp.write(uploaded_file.getvalue())

        temp.flush()
        context = textract.process(temp.name)

        text = context.decode("UTF-8")


clean_text = clean_resume(text)
skills = list(get_skills(model, clean_text))
print(skills)
#matching, missing = get_matching_skills(required_skills, skills)
#print(matching)

st.write(skills)
#sk_miss = st.checkbox("Show only missing skills")



'''
if sk_miss:
    sk_found = st.checkbox('Show all skills found', disabled=True)
    sk_match = st.checkbox("Show matching skills", disabled=True)
    st.write("Missing skills")
    st.write(missing)
else:
    sk_found = st.checkbox('Show all skills found', disabled=False)
    sk_match = st.checkbox("Show matching skills", disabled=False)

    if sk_match and sk_found:
        full = matching+missing
        st.write(full)
    else:
        if sk_match:
            st.write(matching)

'''
#fig = plot_pie(required_skills, skills)
# st.pyplot(fig)
# st.write(count/len(required_skills))
