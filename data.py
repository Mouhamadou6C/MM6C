import streamlit as st
import pandas as pd

# Initialisation de la session pour stocker les données
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["x", "y", "z", "nom", "description"])

st.title("Application de collecte de données 3D")

# Formulaire de saisie
with st.form("data_form"):
    x = st.number_input("Coordonnée X", step=0.1)
    y = st.number_input("Coordonnée Y", step=0.1)
    z = st.number_input("Coordonnée Z", step=0.1)
    nom = st.text_input("Nom du point")
    description = st.text_area("Description")

    submitted = st.form_submit_button("Ajouter")

    if submitted:
        new_row = {"x": x, "y": y, "z": z, "nom": nom, "description": description}
        st.session_state.data = pd.concat([st.session_state.data, pd.DataFrame([new_row])], ignore_index=True)
        st.success("Point ajouté avec succès !")

# Affichage des données collectées
st.subheader("Données collectées")
st.dataframe(st.session_state.data)

# Option d’exportation
csv = st.session_state.data.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Télécharger les données en CSV",
    data=csv,
    file_name="donnees_points.csv",
    mime="text/csv",
)
