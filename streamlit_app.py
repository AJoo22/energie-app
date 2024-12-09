import streamlit as st
import pandas as pd
import gdown
import os

# Function to download and load the dataset
@st.cache_data
def load_data():
    # Define the file path and Google Drive file ID
    file_path = "data/eco2mix-regional-cons-defcopiecopy.csv"
    file_id = "1gZ1dkFXOBfK6gk9LBanu1qYCQkcLTQKp"  # Extracted from your Google Drive link
    download_url = f"https://drive.google.com/uc?id={file_id}"

    # Check if the file exists locally
    if not os.path.exists(file_path):
        st.info("Downloading dataset from Google Drive...")
        os.makedirs("data", exist_ok=True)  # Ensure the 'data' directory exists
        gdown.download(download_url, file_path, quiet=False)
        st.success("Download complete!")

    # Load the dataset
    data = pd.read_csv(file_path, sep=";")
    return data

# Main application logic
def main():
    # Load the data
    data = load_data()

    # Pages available in the app
    pages = ["Accueil", "Présentation", "Préprocessing", "Graphiques", "Modélisations", "Conclusion"]
    selected_page = st.sidebar.selectbox("Navigation", pages)

    # Page: Accueil
    if selected_page == "Accueil":
        st.title("RAPPORT SUR LA CONSOMMATION ET LA PRODUCTION D'ÉNERGIE EN FRANCE")
        st.markdown("<h2 style='font-size: 28px; font-weight: bold;'>Étude sur la production et la consommation d'électricité</h2>", unsafe_allow_html=True)
        st.write("En France métropolitaine de janvier 2013 à septembre 2024")
        st.image("https://storage.letudiant.fr/mediatheque/letudiant/7/8/2635278-differentes-sources-energie-766x438.jpeg", use_container_width=True)
        st.markdown("<h2 style='font-size: 28px; font-weight: bold;'>Membres du Projet :</h2>", unsafe_allow_html=True)
        st.write("JALILI Amine")
        st.write("HOUDOUIN Jean-Raphaël")
        st.write("TOURE Mariama Mountaga")
        st.write("YEBGAR Lucien")
        st.markdown("<h2 style='font-size: 28px; font-weight: bold;'>Mentor :</h2>", unsafe_allow_html=True)
        st.write("Alain Ferlac")

    # Page: Présentation
    elif selected_page == "Présentation":
        st.header("📄 Contexte")
        st.write("""
            La plateforme **Open Data Réseaux Énergies (ODRÉ)** propose un jeu de données régional consolidé
            sur la consommation et la production d’électricité en France.
        """)
        st.header("🎯 Objectifs")
        st.markdown("""
            - **Consommation d’électricité** réalisée par région.
            - **Production d’électricité** par filière énergétique, avec une précision à la demi-heure.
            - **Consommation des Stations de Transfert d'Énergie par Pompage (STEP)**.
            - **Solde des échanges interrégionaux**.
        """)

    # Page: Préprocessing
    elif selected_page == "Préprocessing":
        st.title("Préprocessing")
        st.subheader("Aperçu des données")
        columns_to_show = st.multiselect("Choisir les colonnes à afficher", data.columns.tolist(), default=data.columns.tolist())
        st.dataframe(data[columns_to_show].head(50))
        if st.checkbox("Afficher les statistiques descriptives"):
            st.subheader("Statistiques Descriptives")
            st.write(data.describe())
        if st.checkbox("Afficher les valeurs manquantes"):
            st.subheader("Valeurs Manquantes")
            st.write(data.isnull().sum())

    # Page: Graphiques
    elif selected_page == "Graphiques":
        st.title("Graphiques")
        graphiques = [
            "Production d'électricité par Région",
            "Production et Consommation d'électricité au fil du temps",
            "Impact de la COVID-19 sur la production",
            "Histogramme de la Production et Consommation bimensuelle",
            "Répartition globale du TCH",
            "Répartition globale du TCO",
            "Consommation d'Électricité par Région"
        ]
        choix_graphique = st.selectbox("Choisissez un graphique", graphiques)
        st.warning(f"Le graphique '{choix_graphique}' n'est pas encore implémenté.")

    # Page: Modélisations
    elif selected_page == "Modélisations":
        st.title("Modélisations")
        options = [
            'Boxplot',
            'Performance des modèles',
            'Graphique de corrélation',
            'Régression Linéaire',
            'Régression Ridge',
            'Régression Lasso',
            'Arbre de Décision',
            'Forêt Aléatoire',
            'Régression : Île-de-France'
        ]
        selected_option = st.selectbox("Choisissez une visualisation :", options)
        st.warning(f"Le modèle '{selected_option}' n'est pas encore implémenté.")

    # Page: Conclusion
    elif selected_page == "Conclusion":
        st.title("Conclusion")
        st.markdown("""
        - 🔍 L'étude a permis d'analyser la consommation et la production d'énergie en France.
        - 🌳 Les énergies renouvelables représentent une part significative mais variable selon les régions.
        - 🔮 Perspectives futures : renforcer l'indépendance énergétique et investir dans les infrastructures.
        """)

# Entry point for the application
if __name__ == "__main__":
    main()
