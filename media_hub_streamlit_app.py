
import streamlit as st

st.set_page_config(page_title="Media Hub", layout="wide")

st.title("🎵 Media Hub - روابط أشهر منصات الموسيقى")

services = {
    "Spotify": "https://open.spotify.com/",
    "YouTube Music": "https://music.youtube.com/",
    "Anghami": "https://play.anghami.com/",
    "SoundCloud": "https://soundcloud.com/",
    "Apple Music": "https://music.apple.com/",
    "Deezer": "https://www.deezer.com/",
    "Tidal": "https://tidal.com/",
    "Mixcloud": "https://www.mixcloud.com/",
}

cols = st.columns(4)
for index, (name, url) in enumerate(services.items()):
    with cols[index % 4]:
        st.markdown(f"### [{name}]({url})")
        st.image(f"https://logo.clearbit.com/{url.replace('https://','').replace('/','')}", width=80)
        st.markdown("---")
