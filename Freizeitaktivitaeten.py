import streamlit as st
import pandas as pd
import altair as alt

st.header("Häufige Freizeitaktivitäten von Jungen")
st.subheader("Was machst Du häufig in Deiner Freizeit?")

source = pd.DataFrame({
        'Prozent(%)': [82, 68, 58, 50, 33, 32, 25, 24, 23, 23],
        'Aktivitäten': ['Freunde treffen', 'Rad fahren', 'Fußball spielen', 'Musik hören', 'Computer nutzen', 'Mit Handspielgeräten spielen', 'Computerspiele spielen', 'Schwimmen', 'Mit Spielkästen spielen', 'Mit Konsolen spielen']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Prozent(%):Q',
        x='Aktivitäten:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    6-13 Jahre; Jungen
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Ehapa Verlag")