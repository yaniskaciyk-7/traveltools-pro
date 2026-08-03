import streamlit as st
import requests
import json

# 1. PARAMÈTRES DU SITE INTERNET
st.set_page_config(
    page_title="TravelTools Pro",
    page_icon="🧳",
    layout="centered"
)

st.title("🧳 TravelTools Pro")
st.write("### La suite logicielle d'élite pour les agences de voyage.")
st.caption("Disponible 24h/24 — Version Sécurisée")

# Barre latérale pour le mot de passe client
st.sidebar.header("🔑 Clé de Licence")
code_licence = st.sidebar.text_input("Entrez votre code d'accès :", type="password", value="AGENCE-ELITE-2026")

# 2. CRÉATION DES 4 ONGLETS DU LOGICIEL
onglet1, onglet2, onglet3, onglet4 = st.tabs([
    "🛂 1. Passeport & Visa", 
    "📊 2. Formatage Passagers", 
    "🔥 3. Contre-Attaque Devis", 
    "✈️ 4. Sécurité Escale"
])

# Vérification du mot de passe
if code_licence != "AGENCE-ELITE-2026" and code_licence != "TRAVEL-SAFE-VIP":
    st.error("❌ Code de licence invalide ou expiré.")
else:
    # Récupération de la clé OpenRouter cachée en sécurité
    try:
        cle_api = st.secrets["OPENROUTER_KEY"]
    except:
        st.warning("⚙️ Clé de sécurité en cours de configuration par le serveur...")
        cle_api = None

    if cle_api:
        # En-tête obligatoire exigé par OpenRouter en 2026 pour les modèles gratuits
        headers_openrouter = {
            "Authorization": f"Bearer {cle_api}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://streamlit.io", # Obligatoire pour OpenRouter
            "X-Title": "TravelTools Pro App"       # Obligatoire pour OpenRouter
        }

        # =====================================================================
        # CONTENU DE L'ONGLET 1 : VERIFICATION PASSEPORT & VISA
        # =====================================================================
        with onglet1:
            st.subheader("🛂 Vérification des Pièces d'Identité")
            with st.form("form_passport"):
                nationalite = st.text_input("Nationalité :", value="Française")
                destination = st.text_input("Pays de destination :", value="Indonésie (Bali)")
                date_retour = st.text_input("Date de RETOUR (AAAA-MM-JJ) :", value="2026-11-15")
                expire_passeport = st.text_input("Expiration du passeport (AAAA-MM-JJ) :", value="2027-02-10")
                submit1 = st.form_submit_button("🔍 Lancer l'Audit Douanier")
                
                if submit1:
                    prompt = f"Vérifie si un voyageur de nationalité {nationalite} peut aller en {destination} avec un retour le {date_retour} et un passeport expirant le {expire_passeport}. Réponds de manière courte en français."
                    with st.spinner("Analyse..."):
                        try:
                            url = "https://openrouter.ai"
                            data = {"model": "meta-llama/llama-3-8b-instruct:free", "messages": [{"role": "user", "content": prompt}]}
                            reponse = requests.post(url, headers=headers_openrouter, data=json.dumps(data), timeout=15)
                            st.info("🤖 Rapport Douane :")
                            st.write(reponse.json()['choices']['message']['content'].strip())
                        except Exception as e: st.error(f"Erreur : {e}")

        # =====================================================================
        # CONTENU DE L'ONGLET 2 : FORMATAGE DES PASSAGERS
        # =====================================================================
        with onglet2:
            st.subheader("📊 Normalisation des Données Passagers")
            with st.form("form_data"):
                texte_vrac = st.text_area("Collez le mail fouillis du client ici :", value="Jean-Pierre Dupont né le 12 mars 1984, sa femme rachel dupont née le 04/05/1987")
                submit2 = st.form_submit_button("🚀 Nettoyer le profil")
                
                if submit2:
                    prompt = f"Extrais les noms, prénoms et dates de naissance de ce texte de manière propre : {texte_vrac}."
                    with st.spinner("Nettoyage..."):
                        try:
                            url = "https://openrouter.ai"
                            data = {"model": "meta-llama/llama-3-8b-instruct:free", "messages": [{"role": "user", "content": prompt}]}
                            reponse = requests.post(url, headers=headers_openrouter, data=json.dumps(data), timeout=15)
                            st.success("🤖 Données Propres :")
                            st.write(reponse.json()['choices']['message']['content'].strip())
                        except Exception as e: st.error(f"Erreur : {e}")

        # =====================================================================
        # CONTENU DE L'ONGLET 3 : GHOSTBUSTER DE DEVIS
        # =====================================================================
        with onglet3:
            st.subheader("🔥 Démonter le Devis du Concurrent")
            with st.form("form_devis"):
                devis_concurrent = st.text_area("Collez le devis de l'autre agence :", value="Vol avec escale de 14h, hôtel 3 étoiles excentré...")
                submit3 = st.form_submit_button("⚡ Trouver les pièges")
                
                if submit3:
                    prompt = f"Trouve les points faibles cachés de ce devis de voyage et donne un court script commercial pour convaincre le client : {devis_concurrent}."
                    with st.spinner("Analyse commerciale..."):
                        try:
                            url = "https://openrouter.ai"
                            data = {"model": "meta-llama/llama-3-8b-instruct:free", "messages": [{"role": "user", "content": prompt}]}
                            reponse = requests.post(url, headers=headers_openrouter, data=json.dumps(data), timeout=15)
                            st.warning("🤖 Contre-Attaque Commerciale :")
                            st.write(reponse.json()['choices']['message']['content'].strip())
                        except Exception as e: st.error(f"Erreur : {e}")

        # =====================================================================
        # CONTENU DE L'ONGLET 4 : SECURITE ESCALE
        # =====================================================================
        with onglet4:
            st.subheader("✈️ Agent de Sécurisation des Escales")
            with st.form("form_scale"):
                aeroport_escale = st.text_input("Aéroport d'escale :", value="JFK (New York)")
                temps_escale = st.text_input("Temps de correspondance :", value="1h20")
                submit4 = st.form_submit_button("🔍 Auditer l'escale")
                
                if submit4:
                    prompt = f"Dis si une escale de {temps_escale} à l'aéroport de {aeroport_escale} est risquée et s'il faut un visa de transit pour un français."
                    with st.spinner("Vérification..."):
                        try:
                            url = "https://openrouter.ai"
                            data = {"model": "meta-llama/llama-3-8b-instruct:free", "messages": [{"role": "user", "content": prompt}]}
                            reponse = requests.post(url, headers=headers_openrouter, data=json.dumps(data), timeout=15)
                            st.error("🤖 Alerte Logistique Escale :")
                            st.write(reponse.json()['choices']['message']['content'].strip())
                        except Exception as e: st.error(f"Erreur : {e}")
