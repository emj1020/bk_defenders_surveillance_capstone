import streamlit as st

# Set page configuration
st.set_page_config(layout="wide")

# Define styles
main_title_style = """
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 20px;
"""
section_title_style = """
    font-size: 24px;
    font-weight: bold;
    margin-top: 40px;
    margin-bottom: 10px;
"""
subheader_style = """
    font-size: 20px;
    font-weight: bold;
    margin-top: 30px;
    margin-bottom: 10px;
"""

# Add NYU logo and title
nyu_logo = "https://media.licdn.com/dms/image/C4D0BAQFDeOVQn-KX0Q/company-logo_200_200/0/1559248562866?e=1696464000&v=beta&t=uRi7pw8Xk6wc2B_1GyCli1k72E-qIyqWXnlLrNY_2u0"
col1, col2 = st.columns([0.15, 0.85])
with col1:
    st.image(nyu_logo, use_column_width=True)
with col2:
    st.markdown(
        "<h1 style='text-align: center; background-color: violet; padding: 10px;'>NYU Center for Urban Science and Progress 2023 Capstone Project</h1>",
        unsafe_allow_html=True,
    )
st.markdown("---")


# Welcome section
st.markdown("<h2 style='text-align: center'>Brooklyn Surveillance Metric Dashboard</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center'>Welcome!</h2>", unsafe_allow_html=True)

# Project description
st.header("Project Description")
st.write("Brooklyn Defender Services is a public defense office whose mission is to provide outstanding representation and advocacy free of cost to people facing loss of freedom, family separation, and other serious legal harms by the government. Their Science and Surveillance Project focuses on investigating government and private entity use of new science, surveillance, and data analysis techniques to educate our staff, communities, and representatives, as well as advocate against unjust practices. The goal of this capstone project is to develop a methodology that quantifies the intensity of surveillance neighborhoods in Brooklyn are subjected to by the presence of surveillance cameras.")
st.markdown("---")

# Research question
st.header("Research Question")
st.write("How do we quantify the intensity of surveillance across Brooklyn? How do we develop a metric that can be used to reliably compare the intensity of surveillance? How can we identify which communities are disproportionately impacted by this surveillance load?")
st.markdown("---")

# Anticipated data requirements
st.header("Anticipated Data Requirements")
st.write("The project will require surveillance data, including datasets describing the locations of police-operated and private security cameras. Public-sector data such as the American Community Survey and NYC PLUTO data will also be used to identify key demographic information about the affected neighborhoods.")
st.markdown("---")

# Deliverables
st.header("Deliverables")
st.write("The expected deliverables of this capstone project include:")
st.markdown("- A metric that quantifies the intensity of surveillance to identify the most and least impacted communities across Brooklyn.")
st.markdown("- An interactive map of Brooklyn displaying the impact of surveillance on a neighborhood-by-neighborhood basis.")
st.markdown("- A general and iterable methodology that can be applied to other forms of surveillance technology in the future.")

# Project team
st.header("Project Team")
team_columns = st.columns(3)

with team_columns[0]:
    st.subheader("Project Manager: Rahnuma Tarannum")
    st.image("https://media.licdn.com/dms/image/D4E03AQHzh59NYBfwew/profile-displayphoto-shrink_400_400/0/1687961120146?e=1694044800&v=beta&t=cNzsc9nTTsD1Zao1svxi-Ve_7Al3l8bGETuXZcqBqLQ", use_column_width=True)

with team_columns[1]:
    st.subheader("Data Manager: Liz Johnson")
    st.image("https://media.licdn.com/dms/image/D4E03AQE2PkNbcqOmxA/profile-displayphoto-shrink_800_800/0/1682008231208?e=1694044800&v=beta&t=vOTKJ0wyF6NSJczCEpDXoUuu7MEf4aaTX8N0QWp21S8", use_column_width=True)

with team_columns[2]:
    st.subheader("Operations Manager: Rui Jiang")
    st.image("https://media.licdn.com/dms/image/C5603AQFTa5Mb9_IRRA/profile-displayphoto-shrink_800_800/0/1554355541265?e=1694044800&v=beta&t=nxryIQuaQvgxpHWGVSYHD7iPRZhgCU2Nu9aWD2BjPZg", use_column_width=True)

# Sponsor
st.header("Sponsor")
st.write("Brooklyn Defender Services")
st.image("data:image/png;base64,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", use_column_width=True)
st.write("Elizabeth Vasquez - Director of Science and Surveillance Project")
st.write("Andrew Foltz-Morrison - Data Scientist, Science & Surveillance Project")

# Mentor
st.header("Mentor")
st.write("Manny Patole")

# Links
st.header("Links")
st.write("[Our GitHub Repo](https://github.com/emj1020/bk_defenders_surveillance_capstone/)")
st.write("[LinkedIn - Rahnuma Tarannum](https://www.linkedin.com/in/rahnuma-tarannum/)")
st.write("[LinkedIn - Liz Johnson](https://www.linkedin.com/in/elizabeth-johnson-65835414a/)")
st.write("[LinkedIn - Rui Jiang](https://www.linkedin.com/in/ruijiang-wyf/)")

# Contact information
st.header("Contact Information")
st.write("NYU Center for Urban Science and Progress")
st.write("370 Jay Street, 13th Floor")
st.write("Brooklyn, NY 11201")

# Footer
st.markdown("---")
st.write("© 2023 Rahnuma, Liz, and Rui - Center for Urban Science + Progress")
