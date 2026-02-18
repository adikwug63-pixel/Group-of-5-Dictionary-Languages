import streamlit as st

# Dictionary
hausa_dictionary = {
    "water": "ruwa",
    "food": "abinci",
    "house": "gida",
    "man": "namiji",
    "woman": "mace",
    "child": "yaro",
    "school": "makaranta",
    "book": "littafi",
    "sun": "rana",
    "moon": "wata",
    "dog": "kare",
    "cat": "kuliya",
    "money": "kudi",
    "road": "hanya",
    "market": "kasuwa",
    "friend": "aboki",
    "teacher": "malami",
    "student": "dalibi",
    "love": "so",
    "work": "aiki"
}

idoma_dictionary = {
    "water": "ankpor",
    "food": "ogira",
    "house": "ole",
    "person": "oche",
    "man": "ochigbo",
    "woman": "onya",
    "child": "oyi",
    "sun": "oleno",
    "moon": "owia",
    "fire": "inya",
    "road": "okpokwu",
    "market": "ogwu",
    "friend": "okpakun",
    "love": "ihotu",
    "work": "ukro",
    "money": "eja",
    "tree": "ochi",
    "book": "okpa",
    "school": "enokpa",
    "king": "oche"
}

yoruba_dictionary = {
    "water":"omi",
    "food":"ounje",
    "house":"ile",
    "man":"okunrin",
    "woman":"obirin",
    "child":"omo",
    "school":"ile-iwe",
    "book":"iwe",
    "sun":"orun",
    "moon":"osupa",
    "dog":"aja",
    "cat":"oko",
    "money":"owo",
    "road":"ona",
    "market":"oja",
    "friend":"ore",
    "teacher":"olko",
    "student":"akewi",
    "love":"ife",
    "work":"aiki"
}


# App title
st.title("Language dictionary")
st.write("English to Language  translator")

# Input
word = st.text_input("Enter an English word:").lower()

# Language selection
st.subheader("Select Target Language")
languages = st.multiselect(
    "Choose which languages to translate to:",
    ["Hausa", "Yoruba", "Idoma"],
    default=["Hausa", "Yoruba", "Idoma"]
)

# Translate button
if st.button("Translate"):
    if not word:
        st.warning("Please enter a word to translate")
    else:
        found = False
        
        if "Hausa" in languages and word in hausa_dictionary:
            st.success(f"🇳🇬 **Hausa**: {hausa_dictionary[word]}")
            found = True
        
        if "Yoruba" in languages and word in yoruba_dictionary:
            st.success(f"🇳🇬 **Yoruba**: {yoruba_dictionary[word]}")
            found = True
            
        if "Idoma" in languages and word in idoma_dictionary:
            st.success(f"🇳🇬 **Idoma**: {idoma_dictionary[word]}")
            found = True
        
        if not found:
            st.error("Word not found in selected language(s)")

# Display options
st.subheader("Dictionary Viewer")
col1, col2, col3 = st.columns(3)

with col1:
    if st.checkbox("Show Hausa Dictionary"):
        st.write("**Hausa Words:**")
        for eng, hau in hausa_dictionary.items():
            st.write(f"**{eng}** → {hau}")

with col2:
    if st.checkbox("Show Yoruba Dictionary"):
        st.write("**Yoruba Words:**")
        for eng, yor in yoruba_dictionary.items():
            st.write(f"**{eng}** → {yor}")

with col3:
    if st.checkbox("Show Idoma Dictionary"):
        st.write("**Idoma Words:**")
        for eng, ido in idoma_dictionary.items():
            st.write(f"**{eng}** → {ido}")