import streamlit as st
import pandas as pd

@st.cache_data
def load_data(data_url="/content/drive/MyDrive/groupeDeTravail-BDAenergie/eco2mix-regional-cons-defcopiecopy.csv"):
    # Charger les données
    data = pd.read_csv(data_url, sep=";")
    return data

def main():
    # Chargement des données
    data_url = "/content/drive/MyDrive/groupeDeTravail-BDAenergie/eco2mix-regional-cons-defcopiecopy.csv"
    data = load_data(data_url)

    # Pages disponibles
    pages = ["Accueil", "Présentation", "Préprocessing", "Graphiques", "Modélisations", "Conclusion"]
    selected_page = st.sidebar.selectbox("Navigation", pages)

    # Page d'Accueil
    if selected_page == "Accueil":
        st.title("RAPPORT SUR LA CONSOMMATION ET LA PRODUCTION D'ÉNERGIE EN FRANCE")
        st.markdown("<h2 style='font-size: 28px; font-weight: bold;'>Étude sur la production et la consommation d'électricité</h2>", unsafe_allow_html=True)
        st.write("en France métropolitaine de janvier 2013 à septembre 2024")
        st.image("https://storage.letudiant.fr/mediatheque/letudiant/7/8/2635278-differentes-sources-energie-766x438.jpeg", use_container_width=True)

        st.markdown("<h2 style='font-size: 28px; font-weight: bold;'>Membres du Projet :</h2>", unsafe_allow_html=True)
        st.write("JALILI Amine")
        st.write("HOUDOUIN Jean-Raphaël")
        st.write("TOURE Mariama Mountaga")
        st.write("YEBGAR Lucien")

        st.markdown("<h2 style='font-size: 28px; font-weight: bold;'>Mentor :</h2>", unsafe_allow_html=True)
        st.write("Alain Ferlac")

    # Page de Présentation
    elif selected_page == "Présentation":
        st.header("📄 Contexte")
        st.write(
            """
            La plateforme **Open Data Réseaux Énergies (ODRÉ)** propose un jeu de données régional consolidé
            sur la consommation et la production d’électricité en France. Ces données, couvrant la période
            de **janvier 2013 à janvier 2023**, sont :
            - **Actualisées quotidiennement**
            - **Vérifiées et complétées** pour assurer leur fiabilité
            - Détaillées par région
            """
        )

        # Section : Objectifs
        st.header("🎯 Objectifs")
        st.write(
            """
            Ce jeu de données permet de fournir des informations complètes et fiables sur :
            """
        )
        st.markdown("""
        - **Consommation d’électricité** réalisée par région.
        - **Production d’électricité** par filière énergétique, avec une précision à la demi-heure.
        - **Consommation des Stations de Transfert d'Énergie par Pompage (STEP)** pour le stockage et la régulation de l’énergie.
        - **Solde des échanges interrégionaux** pour évaluer l’autosuffisance énergétique et les flux d’électricité.
        """)

        # Section : Finalités
        st.header("📊 Finalités")
        st.markdown("""
        Grâce à ces données, il est possible de :
        - Suivre l'évolution de la **consommation et de la production d’électricité** dans le temps et par région.
        - Analyser la **couverture énergétique** régionale par filière (**TCO**) et la performance des installations (**TCH**).
        - Effectuer des **analyses comparatives** entre régions pour comprendre les dynamiques énergétiques.
        """)

    # Page de Préprocessing
    elif selected_page == "Préprocessing":
        st.title("Préprocessing")
        st.subheader("Aperçu des données")

        # Sélectionner les colonnes à afficher
        columns_to_show = st.multiselect("Choisir les colonnes à afficher", data.columns.tolist(), default=data.columns.tolist())
        st.dataframe(data[columns_to_show].head(50))

        # Afficher des statistiques descriptives
        if st.checkbox("Afficher les statistiques descriptives"):
            st.subheader("Statistiques Descriptives")
            st.write(data.describe())

        # Afficher les valeurs manquantes
        if st.checkbox("Afficher les valeurs manquantes"):
            st.subheader("Valeurs Manquantes")
            st.write(data.isnull().sum())

        # Ajouter un bouton pour recharger les données
        if st.button("Recharger les données"):
            data = load_data()
            st.success("Les données ont été rechargées avec succès !")

    # Page de Graphiques
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

        image_paths = {
            "Production d'électricité par Région": "/content/drive/MyDrive/groupeDeTravail-BDAenergie/Dossier sans titre/Production d'Electricité par Région.png",
            "Production et Consommation d'électricité au fil du temps": "/content/drive/MyDrive/groupeDeTravail-BDAenergie/Dossier sans titre/Production et Consommation d'électricité au fil du temps (1).png",
            "Impact de la COVID-19 sur la production": "/content/drive/MyDrive/groupeDeTravail-BDAenergie/Dossier sans titre/Production et Consommation d'électricité pendant la période de la COVID-19 et la reprise.png",
            "Histogramme de la Production et Consommation bimensuelle": "/content/drive/MyDrive/groupeDeTravail-BDAenergie/Dossier sans titre/Histogramme de la Production et Consommation d'Électricité tous les 2 mois.png",
            "Répartition globale du TCH": "/content/drive/MyDrive/groupeDeTravail-BDAenergie/Dossier sans titre/Répartition du taux de charge (TCH) par sources d'énergie en France Métropolitaine.png",
            "Répartition globale du TCO": "/content/drive/MyDrive/groupeDeTravail-BDAenergie/Dossier sans titre/Répartition du taux de couverture (TCO) par sources d'énergie en France Métropolitaine.png",
            "Consommation d'Électricité par Région": "/content/drive/MyDrive/groupeDeTravail-BDAenergie/Dossier sans titre/Consommation d'Electricité par Région.png"
        }

        choix_graphique = st.selectbox("Choisissez un graphique", graphiques)

        if choix_graphique in image_paths:
            st.image(image_paths[choix_graphique], caption=choix_graphique, use_container_width=True)

    # Page de Modélisations
    elif selected_page == "Modélisations":
        st.title("Modélisations")
        st.write("Section de prédictions basée sur des modèles de machine learning.")

        # Liste déroulante pour les visualisations
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

        # Dictionnaire des liens vers les images
        images = {
            'Boxplot': "/content/drive/MyDrive/groupeDeTravail-BDAenergie/Boxplot de consomation.png",
            'Performance des modèles': "/content/drive/MyDrive/groupeDeTravail-BDAenergie/Perforamance des modèles.png",
            'Graphique de corrélation': "/content/drive/MyDrive/groupeDeTravail-BDAenergie/Graphique de corrélation.png",
            'Régression Linéaire': "/content/drive/MyDrive/groupeDeTravail-BDAenergie/Régresionn liéaire.png",
            'Régression Ridge': "/content/drive/MyDrive/groupeDeTravail-BDAenergie/Régression de Ridge.png",
            'Régression Lasso': "/content/drive/MyDrive/groupeDeTravail-BDAenergie/Régression Lasso.png",
            'Arbre de Décision': "/content/drive/MyDrive/groupeDeTravail-BDAenergie/Arbre de décision.png",
            'Forêt Aléatoire': "/content/drive/MyDrive/groupeDeTravail-BDAenergie/Modèle foret aléatoire.png",
            'Régression : Île-de-France': "/content/drive/MyDrive/groupeDeTravail-BDAenergie/Régression ile de France.png",
        }

        # Affichage de l'image correspondant à l'option sélectionnée
        if selected_option in images:
            st.image(images[selected_option], caption=f"Visualisation : {selected_option}", use_container_width=True)
        else:
            st.warning("Aucune image disponible pour cette sélection.")

    # Page de Conclusion
    elif selected_page == "Conclusion":
        st.title("Conclusion")
        st.markdown("""
        - 🔍 L'étude a permis d'analyser la consommation et la production d'énergie en France.
        - 🌳 Les énergies renouvelables représentent une part significative mais variable selon les régions.
        - 🔮 Perspectives futures : renforcer l'indépendance énergétique et investir dans les infrastructures.
        """)

# Point d'entrée de l'application
if __name__ == "__main__":
    main()
