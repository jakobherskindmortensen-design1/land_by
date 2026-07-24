import streamlit as st
import random

st.set_page_config(page_title="Land, By, Flod", page_icon="🌍")

st.title("🌍 Land, By og Flod Generator")

# ==========================================
# 1. HUKOMMELSEN (SESSION STATE)
# ==========================================
if "kategorier" not in st.session_state:
    st.session_state.kategorier = [
        "Land", "By", "Flod / Vand", "Dyr", "Drenge-navn", "Pige-navn",
        "Filminstruktør", "Rock- eller metalband", "Historisk begivenhed",
        "Noget fra Formel 1", "Et videospil", "Profession",
        "Frugt / Grøntsag", "Noget man finder i en taske", "Sportsgren"
    ]

# ==========================================
# 2. TILFØJ NY KATEGORI (BRUGERFLADEN)
# ==========================================
st.write("### ➕ Tilføj en ekstra kategori til puljen")

col1, col2 = st.columns([3, 1])

with col1:
    ny_kat = st.text_input("Ny kategori", placeholder="F.eks. Skurk fra en film...", label_visibility="collapsed")
    
with col2:
    if st.button("Tilføj", use_container_width=True):
        if ny_kat:
            st.session_state.kategorier.append(ny_kat)
            st.success(f'"{ny_kat}" tilføjet!')

st.write(f"*Der er lige nu {len(st.session_state.kategorier)} kategorier i puljen.*")
st.divider()

# ==========================================
# 3. SELVE SPILLET
# ==========================================
st.write("Tryk på knappen for at trække et nyt bogstav og 5 tilfældige kategorier!")
bogstaver = "ABCDEFGHIJKLMNOPRSTUVYZÆØÅ"

if st.button("🎯 START EN NY RUNDE", use_container_width=True):
    trukket_bogstav = random.choice(bogstaver)
    
    rundens_kategorier = random.sample(st.session_state.kategorier, 5)

    st.divider() 
    st.header(f"Rundens bogstav: **{trukket_bogstav}**")
    
    st.write("### Kategorier:")
    tal = 1
    for kategori in rundens_kategorier:
        st.write(f"**{tal}.** {kategori}")
        tal += 1
        
    st.divider()
    st.success("Tid til at skrive! Hvem bliver først færdig?")
