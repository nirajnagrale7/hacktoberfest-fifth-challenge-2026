"""Streamlit interface for Echoes."""

from __future__ import annotations

import streamlit as st

from memory_writer import DEFAULT_MODEL, STYLES, write_memory

st.set_page_config(page_title="Echoes", page_icon="🕯️", layout="centered")

st.markdown(
    """
    <style>
    .stApp { background: #171923; color: #f5ead8; }
    .block-container { max-width: 820px; padding-top: 2.5rem; }
    .hero {
        padding: 2rem;
        border: 1px solid #554b58;
        border-radius: 22px;
        background: linear-gradient(135deg, #292637, #392934);
    }
    .hero h1 { color: #f5d9a8; margin: 0; font-size: 2.8rem; }
    .hero p { color: #e6d5c7; font-size: 1.08rem; margin-bottom: 0; }
    </style>
    <div class="hero">
      <h1>🕯️ Echoes</h1>
      <p>A little light for the stories we carry.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
st.caption(
    "Turn a memory into a remembrance or a gentle ghost story with a model "
    "running on your own computer. Your words are sent only to Ollama on "
    "localhost; Echoes does not save them."
)

with st.form("write_memory"):
    memory = st.text_area(
        "What would you like to remember?",
        placeholder=(
            "A small moment, a favorite song, something they always said, "
            "or a place you shared..."
        ),
        height=180,
        max_chars=6000,
    )
    style = st.selectbox("Shape this memory as", tuple(STYLES))
    model = st.text_input("Ollama model", value=DEFAULT_MODEL)
    submitted = st.form_submit_button("✨ Let the story take shape", type="primary")

if submitted:
    st.session_state.pop("written_memory", None)
    try:
        with st.spinner("Listening locally..."):
            result = write_memory(memory, style, model)
    except (OSError, RuntimeError, ValueError) as error:
        st.error(str(error))
    else:
        st.session_state["written_memory"] = (style, result)

written_memory = st.session_state.get("written_memory")
if written_memory:
    style, result = written_memory
    st.subheader(style)
    st.markdown(result)
    st.download_button(
        "Download this story",
        data=result,
        file_name="echoes.txt",
        mime="text/plain",
    )
    st.caption("The downloaded file is saved only when and where you choose.")

st.divider()
st.caption(
    "Echoes is a creative writing companion, not a way to contact or speak "
    "for someone who has died. Keep or change any words that feel right to you."
)
