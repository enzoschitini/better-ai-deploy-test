import streamlit as st

st.set_page_config(
    page_title="BetterAI",
    page_icon="✦",
    layout="wide",
)

# --- Routing ---
params = st.query_params
page = params.get("page", "home")

# --- Navigation ---
def nav_link(label: str, target: str):
    is_active = page == target
    style = "font-weight: 700; text-decoration: underline;" if is_active else "text-decoration: none; color: inherit;"
    st.markdown(
        f'<a href="?page={target}" style="{style}">{label}</a>',
        unsafe_allow_html=True,
    )

with st.sidebar:
    st.markdown("## ✦ BetterAI")
    st.markdown("---")
    nav_link("🏠 Home", "home")
    nav_link("📖 Sobre", "about")
    nav_link("🔌 API", "api")
    nav_link("📬 Contato", "contact")

# --- Pages ---
if page == "home":
    st.title("Bem-vindo ao BetterAI ✦")
    st.markdown(
        """
        **Where intelligence finds purpose.**

        Esta é a interface web da plataforma BetterAI.
        Use o menu lateral para navegar entre as seções.
        """
    )

elif page == "about":
    st.title("Sobre")
    st.markdown(
        """
        O **BetterAI** é uma plataforma de serviços de inteligência artificial
        desenvolvida para oferecer soluções práticas e escaláveis.

        - Versão: `1.0.0`
        - Backend: FastAPI + uv
        - Frontend: Streamlit
        """
    )

elif page == "api":
    st.title("API")
    st.markdown(
        """
        A API REST do BetterAI está disponível publicamente.

        | Endpoint | Método | Descrição |
        |----------|--------|-----------|
        | `/health` | GET | Status do serviço |
        | `/docs`   | GET | Documentação interativa |

        **Base URL:**
        ```
        https://better-ai-deploy-test.onrender.com
        ```
        """
    )

elif page == "contact":
    st.title("Contato")
    st.markdown(
        """
        Entre em contato para dúvidas, sugestões ou parcerias.

        - 💼 [LinkedIn](https://www.linkedin.com/in/enzoschitini/)
        - 🐙 [GitHub](https://github.com/enzoschitini)
        """
    )

else:
    st.error(f'Página `{page}` não encontrada.')
    st.markdown('[← Voltar para Home](?page=home)')