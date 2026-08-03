import streamlit as st
import requests
import json

# 1. DESIGN PROFESSIONNEL DU LOGICIEL
st.set_page_config(
    page_title="TravelTools Pro - Suite Interne",
    page_icon="🧳",
    layout="centered"
)

st.title("🧳 TravelTools Pro")
st.write("### La suite logicielle d'élite pour les salariés en agence de voyage.")
st.caption("Solution Décentralisée Premium — Hébergement Permanent 24h/24")

# Barre latérale pour la licence payante commune aux 4 onglets
st.sidebar.header("🔑 Espace Salarié")
code_licence = st.sidebar.text_input("Entrez le Code de Licence Interne :", type="password", value="AGENCE-ELITE-2026")
st.sidebar.markdown("---")
st.sidebar.markdown("💡 *Zéro erreur, commissions protégées. Vos 4 outils de terrain sur une seule page.*")

# 3. CRÉATION DES 4 ONGLETS MAGIQUES
onglet1, onglet2, onglet3, onglet4 = st.tabs([
    "🛂 1. Passeport & Visa", 
    "📊 2. Formatage Passagers", 
    "🔥 3. Contre-Attaque Devis", 
    "✈️ 4. Sécurité Escale"
])

# Vérification sécurisée du code d'accès de l'agence
if code_licence != "AGENCE-ELITE-2026" and code_licence != "TRAVEL-SAFE-VIP":
    st.error("❌ Code de licence invalide ou expiré dans la barre latérale.")
else:
    # SECRET : On récupère la clé OpenRouter cachée dans le serveur Streamlit
    try:
        cle_api_real = st.secrets["OPENROUTER_KEY"]
    except:
        st.warning("⚙️ En attente de la configuration de la clé de sécurité par l'administrateur...")
        cle_api_real = None

    if cle_api_real:
        # =====================================================================
        # CONTENU DE L'ONGLET 1 : VERIFICATION PASSEPORT & VISA
        # =====================================================================
        with onglet1:
            st.subheader("🛂 Vérification des Pièces d'Identité & Douanes")
            with st.form("form_passport"):
                nationalite = st.text_input("Nationalité des voyageurs :", value="Française")
                destination = st.text_input("Pays de destination :", value="Indonésie (Bali)")
                date_retour = st.text_input("Date de RETOUR prévue (AAAA-MM-JJ) :", value="2026-11-15")
                expire_passeport = st.text_input("Date d'EXPIRATION du passeport du client (AAAA-MM-JJ) :", value="2027-02-10")
                submit1 = st.form_submit_button("🔍 Lancer l'Audit Douanier")
                
                if submit1:
                    prompt = (
                        f"Calcule la validité pour un voyageer de nationalité {nationalite} se rendant en {destination}. "
                        f"Retour prévu le {date_retour}, expiration passeport le {expire_passeport}. "
                        "Dis si la règle de validité post-retour du pays est respectée ou violée et liste les formalités obligatoires (Visa/e-Visa)."
                    )
                    with st.spinner("Analyse des lois douanières..."):
                        try:
                            url = "https://openrouter.ai"
                            headers = {"Authorization": f"Bearer {cle_api_real}", "Content-Type": "application/json"}
                            data = {"model": "meta-llama/llama-3-8b-instruct:free", "messages": [{"role": "user", "content": prompt}]}
                            reponse = requests.post(url, headers=headers, data=json.dumps(data), timeout=20)
                            st.info("🤖 Rapport de Conformité Douanière :")
                            st.write(reponse.json()['choices']['message']['content'].strip())
                        except Exception as e: 
                            st.error(f"Erreur : {e}")

        # =====================================================================
        # CONTENU DE L'ONGLET 2 : FORMATAGE ET NETTOYAGE DES PASSAGERS
        # =====================================================================
        with onglet2:
            st.subheader("📊 Nettoyage et Formatage Clinique des Données Passagers")
            with st.form("form_data_stripper"):
                texte_vrac = st.text_area(
                    "Collez ici le mail ou le message en vrac reçu du client :",
                    value="Bonjour, voici les infos. Pour moi c'est Jean-Pierre Dupont né le 12 mars 1984. Ma femme c'est rachel dupont (nom de jeune fille martin) née le 04/05/1987 et notre fils léo...",
                    height=150
                )
                submit2 = st.form_submit_button("🚀 Extraire et Normaliser les Profils")
                
                if submit2:
                    prompt = (
                        f"Analyse ce texte en vrac : '{texte_vrac}'. Extrais les profils passagers de manière chirurgicale. "
                        "Structure ta réponse exactement ainsi : 1. PROFIL VOYAGEURS STANDARDISÉ (Liste avec : NOM EN MAJUSCULES, Prénom, "
                        "Date de Naissance au format JJ/MM/AAAA, et Type (Adulte/Enfant)). 2. ALERTES (Infos manquantes ou doutes). "
                        "3. CODE FORMAT GDS (Donne la ligne de texte au format universel Amadeus/Sabre, ex: NM1DUPONT/JEANPIERRE)."
                    )
                    with st.spinner("Nettoyage des fautes de frappe et extraction..."):
                        try:
                            url = "https://openrouter.ai"
                            headers = {"Authorization": f"Bearer {cle_api_real}", "Content-Type": "application/json"}
                            data = {"model": "meta-llama/llama-3-8b-instruct:free", "messages": [{"role": "user", "content": prompt}]}
                            reponse = requests.post(url, headers=headers, data=json.dumps(data), timeout=20)
                            st.success("🤖 Profils Passagers Sécurisés :")
                            st.write(reponse.json()['choices']['message']['content'].strip())
                        except Exception as e: 
                            st.error(f"Erreur : {e}")

        # =====================================================================
        # CONTENU DE l'ONGLET 3 : GHOSTBUSTER DE DEVIS CONCURRENTS
        # =====================================================================
        with onglet3:
            st.subheader("🔥 Le 'Ghostbuster' Commercial de Devis Concurrents")
            with st.form("form_deal_stealer"):
                devis_concurrent = st.text_area(
                    "Collez le texte brut ou la description du devis de l'agence concurrente :",
                    value="Vol Paris-Bangkok avec Qatar Airways. Hôtel Sunshine Resort 3 étoiles, chambre standard, transferts non inclus, taxes à régler sur place...",
                    height=150
                )
                submit3 = st.form_submit_button("⚡ Démonter le Devis Concurrent")
                
                if submit3:
                    prompt = (
                        f"Analyse ce devis concurrent : '{devis_concurrent}'. Trouve tous les pièges, inconforts ou frais cachés. "
                        "Structure ta réponse ainsi : 1. LES 3 PIÈGES DU CONCURRENT (frais masqués, mauvaises notes, escales de nuit...). "
                        "2. LE SCRIPT DE PAROLE MOT À MOT (Ce que l'agent doit dire au client pour lui faire peur légalement et casser l'offre concurrente). "
                        "3. L'ARGUMENT DE REVENTE (Comment justifier que notre offre est 10x plus sûre)."
                    )
                    with st.spinner("Recherche des failles du concurrent..."):
                        try:
                            url = "https://openrouter.ai"
                            headers = {"Authorization": f"Bearer {cle_api_real}", "Content-Type": "application/json"}
                            data = {"model": "meta-llama/llama-3-8b-instruct:free", "messages": [{"role": "user", "content": prompt}]}
                            reponse = requests.post(url, headers=headers, data=json.dumps(data), timeout=20)
                            st.warning("🤖 Contre-Attaque Commerciale Prête :")
                            st.write(reponse.json()['choices']['message']['content'].strip())
                        except Exception as e: 
                            st.error(f"Erreur : {e}")

        # =====================================================================
        # CONTENU DE L'ONGLET 4 : VERIFICATEUR D'ESCALE SÉCURISÉE
        # =====================================================================
        with onglet4:
            st.subheader("✈️ Assistant de Correspondances & Escales Securisées")
            with st.form("form_scale"):
                aeroport_escale = st.text_input("Aéroport d'escale (Nom ou code IATA) :", value="JFK (New York)")
                temps_escale = st.text_input("Temps de correspondance disponible :", value="1h20")
                details_vols = st.text_area("Détails des vols (Compagnies, terminaux, bagages) :", value="Arrivée de Paris avec Air France au Terminal 1, départ vers Miami avec Delta au Terminal 4. Bagages enregistrés de bout en bout.")
                submit4 = st.form_submit_button("🔍 Auditer la sécurité de l'escale")
                
                if submit4:
                    prompt = (
                        f"Tu es un expert en billetterie aérienne. Analyse cette escale à {aeroport_escale} pendant {temps_escale}. "
                        f"Détails : {details_vols}. Donne un verdict clair (Sûr / Trop Risqué), indique s'il faut un visa de transit "
                        "ou un réenregistrement de bagages, et liste 2 conseils indispensables pour que le passager ne rate pas son vol."
                    )
                    with st.spinner("Analyse des plans de l'aéroport..."):
                        try:
                            url = "https://openrouter.ai"
                            headers = {"Authorization": f"Bearer {cle_api_real}", "Content-Type": "application/json"}
