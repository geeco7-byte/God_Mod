import streamlit as st
import random
import time
from datetime import datetime, timedelta

st.set_page_config(page_title="Germany GodMode", page_icon="🦈", layout="wide")

st.title("🦈 DEUTSCHLAND GOD-MODE KONTROLLZENTRUM")
st.markdown(f"**Imperator:** @SharkX89 | {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")

if "start" not in st.session_state:
    st.session_state.start = datetime.now() - timedelta(hours=2, minutes=27)

laufzeit = datetime.now() - st.session_state.start
h, rem = divmod(laufzeit.total_seconds(), 3600)
m, s = divmod(rem, 60)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Macarena läuft", f"{int(h):02d}:{int(m):02d}:{int(s):02d}")
col2.metric("Tanzende", f"{random.randint(83200000,83499999):,}".replace(",","."))
col3.metric("Sync-Rate", f"{random.uniform(99.94,99.99):.4f}%")
col4.metric("DB Verspätung", f"-{random.uniform(2.1,7.8):.1f} min", "Rekord!")

with st.sidebar:
    st.header("GOD-BEFEHLE")
    cmd = st.text_input("Befehl eingeben")
    if st.button("EXECUTE", type="primary"):
        if any(x in cmd.lower() for x in ["stop","ende","aus"]):
            st.success("MACARENA GESTOPPT! Deutschland atmet auf!")
            st.balloons()
        else:
            st.success(f"Befehl '{cmd}' ausgeführt!")
            st.confetti()

time.sleep(1)
st.rerun()