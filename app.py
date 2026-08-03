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
st.caption("Disponible 24h/24 — Version Sécurisée Pro")

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

# Fonction universelle et sécurisée pour appeler OpenRouter
def appeler_openrouter_secure(prompt_text, api_key):
    url = "https://openrouter.ai"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://streamlit.io",
        "X-Title": "TravelTools Pro suite"
    }
    
    # CHANGEMENT DE MODÈLE : Utilisation de Google Gemini (Gratuit, stable et ultra-rapide)
    data = {
        "model": "google/gemini-2.5-flash:free",
        "messages": [{"role": "user", "content": prompt_text}]
    }
    
    try:
        reponse = requests.post(url, headers=headers, data=json.dumps(data), timeout=20)
        
        if reponse.status_code != 200:
            return f"❌ Erreur du serveur OpenRouter (Code {reponse.status_code}). Le serveur est saturé, réessayez dans 3 secondes."
            
        json_data = reponse.json()
        if 'choices' in json_data and len(json_data['choices']) > 0:
            return json_data['choices']['message']['content'].strip()
        else:
            return "⚠️ Le serveur d'IA est momentanément indisponible, veuillez recliquer sur le bouton."
            
    except requests.exceptions.Timeout:
        return "⏱️ Le serveur d'IA a mis trop de temps à répondre. Veuillez réessayer."
    except Exception as e:
        return f"🚨 Erreur technique : {e}"

# Vérification du mot de passe
if code_licence != "AGENCE-ELITE-2026" and code_licence != "TRAVEL-SAFE-VIP":
    st.error("❌ Code de licence invalide ou expiré.")
else:
    # Récupération de la clé OpenRouter cachée dans les Secrets Streamlit
        cle_api = "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"

    if cle_api:
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
                    prompt = f"Agis en expert douanier. Dis si un voyageur de nationalité {nationalite} peut aller en {destination} avec un retour le {date_retour} et un passeport expirant le {expire_passeport}. Réponds de manière courte en français."
                    with st.spinner("Analyse douanière en cours..."):
                        resultat = appeler_openrouter_secure(prompt, cle_api)
                        st.info("🤖 Rapport Douane :")
                        st.write(resultat)

        # =====================================================================
        # CONTENU DE L'ONGLET 2 : FORMATAGE DES PASSAGERS
        # =====================================================================
        with onglet2:
            st.subheader("📊 Normalisation des Données Passagers")
            with st.form("form_data"):
                texte_vrac = st.text_area("Collez le mail fouillis du client ici :", value="Jean-Pierre Dupont né le 12 mars 1984, sa femme rachel dupont née le 04/05/1987")
                submit2 = st.form_submit_button("🚀 Nettoyer le profil")
                
                if submit2:
                    prompt = f"Agis en secrétaire de billetterie. Extrais les noms, prénoms et dates de naissance de ce texte de manière propre : {texte_vrac}."
                    with st.spinner("Nettoyage en cours..."):
                        resultat = appeler_openrouter_secure(prompt, cle_api)
                        st.success("🤖 Données Propres :")
                        st.write(resultat)

        # =====================================================================
        # CONTENU DE L'ONGLET 3 : GHOSTBUSTER DE DEVIS
        # =====================================================================
        with onglet3:
            st.subheader("🔥 Démonter le Devis du Concurrent")
            with st.form("form_devis"):
                devis_concurrent = st.text_area("Collez le devis de l'autre agence :", value="Vol avec escale de 14h, hôtel 3 étoiles excentré...")
                submit3 = st.form_submit_button("⚡ Trouver les pièges")
                
                if submit3:
                    prompt = f"Agis en directeur commercial. Trouve les points faibles cachés de ce devis de voyage et donne un court script commercial pour convaincre le client : {devis_concurrent}."
                    with st.spinner("Analyse commerciale en cours..."):
                        resultat = appeler_openrouter_secure(prompt, cle_api)
                        st.warning("🤖 Contre-Attaque Commerciale :")
                        st.write(resultat)

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
                    prompt = f"Agis en expert de vol. Dis si une escale de {temps_escale} à l'aéroport de {aeroport_escale} est risquée et s'il faut un visa de transit pour un français."
                    with st.spinner("Vérification de l'escale..."):
                        resultat = appeler_openrouter_secure(prompt, cle_api)
                        st.error("🤖 Alerte Logistique Escale :")
                        st.write(resultat)
