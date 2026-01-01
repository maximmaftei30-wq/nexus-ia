import streamlit as st
from openai import OpenAI
import datetime

# --- CONFIGURARE ---
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="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" 
)

st.set_page_config(page_title="NexusIA 2026", layout="wide")

# Timp real (Data + Ora)
acum = datetime.datetime.now()
import pytz
from datetime import datetime

# Această linie îi spune site-ului să folosească ora de la Paris
timezone_fr = pytz.timezone('Europe/Paris')
ora_actuala = datetime.now(timezone_fr).strftime("%H:%M:%S")

# Acum, oriunde folosești ora în site (st.write sau st.sidebar), 
# folosește variabila "ora_actuala"

# --- MENIU LATERAL ---
with st.sidebar:
    st.title("🛰️ NexusIA")
    st.write(f"🕒 **Ora actuală:** {ora_ro}")
    st.write(f"📅 **Data:** {data_ro}")
    st.markdown("---")
    # Numele de aici trebuie să fie identic cu cel din IF-ul de mai jos
    optiune = st.selectbox("Mod de operare:", ["NexusIA (Universal)", "Inginer", "Chef", "Evoluție"])
    st.markdown("---")
    st.success("Sistem activat de Maxim")

# --- 1. MODUL: NexusIA (UNIVERSAL) ---
if optiune == "NexusIA (Universal)":
    st.title(f"🧠 Nucleul NexusIA")
    st.subheader(f"Status: Online | Timp sistem: {ora_ro}")
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Afișare istoric chat
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # AICI ESTE REZOLVAREA ERORII: definim 'prompt'
    prompt = st.chat_input("Introdu comanda pentru NexusIA...")

    if prompt:
        # Salvăm întrebarea
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Sincronizare cu baza de date..."):
                sys_prompt = f"Ești NexusIA. Azi e {data_ro}, ora {ora_ro}. Ești un sistem creat de Maxim."
                res = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "system", "content": sys_prompt}] + st.session_state.chat_history,
                    temperature=0.2
                )
                txt = res.choices[0].message.content
                st.write(txt)
                st.session_state.chat_history.append({"role": "assistant", "content": txt})
            
            # Unelte externe
            st.markdown("---")
            c1, c2, c3 = st.columns(3)
            # Folosim prompt-ul salvat pentru butoane
            query = prompt.replace(' ', '+')
            c1.link_button("🔍 Google", f"https://www.google.com/search?q={query}")
            c2.link_button("📍 Maps", f"https://www.google.com/maps/search/{query}")
            c3.link_button("📺 YouTube", f"https://www.youtube.com/results?search_query={query}")

# --- 2. MODUL: INGINER ---
elif optiune == "Inginer":
    st.title("🏗️ Modul Inginer - Construcții")
    q = st.text_input("Ce vrei să verificăm pe șantier?")
    if st.button("Analizează"):
        res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": f"Răspunde ca un inginer expert: {q}"}]
        )
        st.info(res.choices[0].message.content)

# --- 3. MODUL: CHEF ---
elif optiune == "Chef":
    st.title("🍳 Modul Chef - Gătit")
    ing = st.text_input("Ce ingrediente ai?")
    if st.button("Creează Rețetă"):
        res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": f"Fă o rețetă cu: {ing}"}]
        )
        st.success(res.choices[0].message.content)

# --- 4. MODUL LIFESYTLE ---
elif optiune == "Evoluție":
    st.title("📈 Modul Evoluție - Succes")
    st.write("Maxim, urmărește-ți progresul!")
    c1, c2 = st.columns(2)
    with c1:
        st.checkbox("Cod scris")
        st.checkbox("Plan realizat")
    with c2:
        st.select_slider("Stare:", ["Stabil", "Focus", "Geniu"])
    if st.button("Sfat din spatiu"):
        st.balloons()
        st.write("Succesul este suma micilor eforturi repetate zi de zi.")

