import streamlit as st
import random

# Dette sætter titlen og ikonet oppe i browserens fane!
st.set_page_config(page_title="Land, By, Flod", page_icon="🌍")

# Overskriften på selve hjemmesiden
st.title("🌍 Land, By og Flod Generator")
st.write("Tryk på knappen for at trække et nyt bogstav og 5 tilfældige kategorier!")

# Vores store pulje af kategorier
alle_kategorier = [
    "Land", "By", "Flod / Vand", "Dyr", "Drenge-navn", "Pige-navn",
    "Filminstruktør", "Rock- eller metalband", "Historisk begivenhed",
    "Noget fra Formel 1", "Et videospil", "Profession",
    "Frugt / Grøntsag", "Noget man finder i en taske", "Sportsgren"
]

bogstaver = "ABCDEFGHIJKLMNOPRSTUVYZÆØÅ"

# Her laver vi en stor, klikbar knap på hjemmesiden
if st.button("🎯 START EN NY RUNDE", use_container_width=True):
    # Koden herunder kører KUN, når man trykker på knappen
    trukket_bogstav = random.choice(bogstaver)
    rundens_kategorier = random.sample(alle_kategorier, 5)

    st.divider() # Laver en flot adskillelseslinje
    
    st.header(f"Rundens bogstav: **{trukket_bogstav}**")
    
    st.write("### Kategorier:")
    # Vi udskriver kategorierne med et nummer foran
    tal = 1
    for kategori in rundens_kategorier:
        st.write(f"**{tal}.** {kategori}")
        tal += 1
        
    st.divider()
    st.success("Tid til at skrive! Hvem bliver først færdig?")