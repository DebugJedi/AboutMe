import streamlit as st

# Page Setup

about_page = st.Page(
    page="view/about_me.py",
    title="About Me",
    icon = ":material/account_circle:",
    default=True,
)
# project_1_page = st.Page(
#     page="view/dashboard.py",
#     title="Dashboard",
#     icon = ":material/bar_chart:"
# )
# project_2_page = st.Page(
#     page= "view/chatbot.py",
#     title="Chat Bot",
#     icon=":material/smart_toy:",
# )

# Navigation setup [WITHOUT SECTIONS]
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# Navigation setup [WITH SECTION]
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page]

    }
)

# Shared On all Pages

st.logo("Assets/Logo.png")
st.sidebar.text("By DebugJedi")

# Run Navigation
pg.run()
