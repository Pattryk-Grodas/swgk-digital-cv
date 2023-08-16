from pathlib import Path

import streamlit as st
from PIL import Image

import sys
import os

# Path Settings

# Get the directory of the script
script_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
image_path = os.path.join(script_dir, "assets", "Foto.png")

# General Settings

PAGE_TITTLE = "Digital CV | Patryk Rąk"
PAGE_ICON = ":wave:"
NAME = "Patryk Rąk"
DESCRIPTION ="""
Transfer Pricing Manager | Business Analyst | Business Valuation Analyst
"""
DESCRIPTION2 ="""
Menedżer ds. cen transferowych | Analityk biznesowy | Analityk ds. wycen przedsiębiorstw
"""
EMAIL = "📑 patryk.rak111@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/patryk-r%C4%85k-3341939b/",
}

st.set_page_config(page_title=PAGE_TITTLE, page_icon=PAGE_ICON)

language = st.selectbox(':red[Wybierz język 👈]',
    ('Polski ✅', 'Angielski ✅'))

def display_polish():
    profile_pic = Image.open(image_path)
    link = "https://www.linkedin.com/in/patryk-r%C4%85k-3341939b"
    path_url = "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"
    col1, col2 = st. columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=340)

    with col2:
        st.write('#')
        st.write('#')
        st.title(NAME)
        st.write(DESCRIPTION2)
        st.markdown(f'<a href="{link}"><img src="{path_url}" width=35 height=35 /></a>', unsafe_allow_html=True)
        st.write("🌎 Poznań")
        st.write("☎️ 733 144 469")
        st.write(EMAIL)

    # Tech stack

    python_path = os.path.join(script_dir, "assets", "python.jpg")
    python_pic = Image.open(python_path)

    sql_path = os.path.join(script_dir, "assets", "sql.jpg")
    sql_pic = Image.open(sql_path)

    bpmn_path = os.path.join(script_dir, "assets", "bpmn.jpg")
    bpmn_pic = Image.open(bpmn_path)   
    
    col1, col2, col3 = st. columns(3, gap="small")

    with col1:
        st.write("#")
        st.write(":orange[★✰✰] :green[| Python - junior |]")
        with open(python_path, 'rb') as f:
            data = f.read()
            st.download_button(
                label="🕵🏽‍♂️ Certyfikat",
                data=data,
                file_name="python.jpg",
                mime="image/jpeg",
            )

    with col2:
        st.write("#")
        st.write(":orange[★★✰] :green[| SQL - regular |]")
        with open(sql_path, 'rb') as f:
            data = f.read()
            st.download_button(
                label="🕵🏽‍♂️ Certyfikat",
                data=data,
                file_name="sql.jpg",
                mime="image/jpeg",
            )
     
    with col3:
        st.write("#")
        st.write(":orange[★★✰] :green[| BPMN - regular |]")
        with open(bpmn_path, 'rb') as f:
            data = f.read()
            st.download_button(
                label="🕵🏽‍♂️ Certyfikat",
                data=data,
                file_name="bpmn.jpg",
                mime="image/jpeg",
            )      

    col1, col2, col3, col4 = st. columns(4, gap="small") 

    with col2:
        st.write("#")
        st.write(":orange[★★✰]")
        st.write(":green[| VBA - regular |]")

    with col3:
        st.write("#")
        st.write(":orange[★★★]")
        st.write(":green[| MS Excel - advanced |]")     

    # Experience & Qualifications

    st.write("#")
    st.subheader("Doświadczenie i kwalifikacje")
    st.write(
    """
    - ✅ 💻 5 lat doświadczenia jako Konsultant ds. cen transferowych
    - ✅ 📈 4 lata doświadczenia jako Inwestor giełdowy
    - ✅ 📥 Doświadczenie w projektowaniu i wdrażaniu narzędzi IT, które poprawiają efektywność pracy i usprawniają procesy, wykorzystując wiedzę techniczną i silne umiejętności rozwiązywania problemów.
    - ✅ 👊🏾 Doskonała umiejętność pracy w zespole i wykazywania inicjatywy w realizacji zadań.
    """
    )

    # Hard skills - Operation of programs
    st.write("#")
    st.subheader("Umiejętności w zakresie obsługi programów")
    st.write(
    """
    - ✅  👩‍💻  Obsługa programów: pakiet MS Office, Insert GT, Płatnik, GitLab, CRM, Transfer Pricing Manager, Company Value Radar
    - ✅  🗄️  Obsługa baz danych: Quick Analytics, Amadeus, Royalty Range, Legalis, LEX Informator Prawno-Ekonomiczny, EMIS Professional, Notoria Serwis
    - ✅  📊  Wizualizacja danych: MS Excel, Python - Matplotlib, Seaborn
    """
    )

    # Languages
    st.write("#")
    st.subheader("Języki")
    st.write(
    """
    - ✴️ Angielski :orange[|] :green[Średniozaawansowany]:orange[|] B2/C1
    - ✴️ Niemiecki :orange[|] :green[Podstawowy] :orange[|] A2
    """
    )


    st.write("---")

    # --- WORK HISTORY ---
    link_swgk = "https://www.linkedin.com/company/swgk/mycompany/?viewAsMember=true"
    link_cvr = "https://companyvalueradar.com/"

    st.subheader("👷 Doświadczenie zawodowe")

    # --- JOB 1
    st.write("🔛  10/2017 - obecnie :orange[|] :green[ Asystent➡️Menedżer] :orange[|] Dział Cen Transferowych")
    st.markdown(f'<a href="{link_swgk}">👉Grupa SWGK👈</a>', unsafe_allow_html=True)        
    st.write(
        """
    Jako Menedżer w Grupie SWGK odgrywam kluczową rolę w napędzaniu sukcesu projektów i zespołu zajmującego się cenami transferowymi. Do moich obowiązków należy nadzór nad realizacją projektów, wdrażanie procedur kontrolnych oraz projektowanie rozwiązań informatycznych odpowiadających potrzebom firmy w zakresie usług doradczych.

    W ramach codziennej pracy byłem zaangażowany m.in. w przygotowanie Local file i Master file, bieżące doradztwo, opracowanie modeli rozliczeń dla usług koncernowych oraz tworzenie polityk cen transferowych. Posiadam również doświadczenie w zakresie wykorzystania narzędzi informatycznych, które wspomagały mnie w przygotowaniu i zarządzaniu dokumentacją cen transferowych. 
    """
    )

    # --- JOB 2
    st.write("#")
    st.write("🔛  07/2019 - obecnie  :orange[|]:green[ Analityk biznesowy | Analityk ds. wycen przedsiębiorstw]")
    st.markdown(f'<a href="{link_cvr}">👉Company Value Radar👈</a>', unsafe_allow_html=True)        
    st.write(
        """
    Jako Analityk biznesowy/Analityk ds. wycen przedsiębiorstw współpracuję z działem IT nad rozwojem aplikacji internetowej do wycen spółek. Wykorzystuję moje doświadczenie w analizie danych i modelowaniu finansowym, aby zapewnić klientom dokładne i wnikliwe wyceny w sposób zautomatyzowany.
    """
    )
    st.write("---")

    # ---  EDUCATION ---

    st.subheader("🧑🏻‍🎓 Wykształcenie")

    # --- ED 1
    st.write("🔚10/2021 - 05/2022 :orange[|] :green[Uniwersytet Ekonomiczny w Poznaniu]")
    st.write("✅ Studia podyplomowe - CIMA Finance Leadership - Operational Level")
    st.write("🔚10/2019 - 07/2021 :orange[|] :green[Uniwersytet Ekonomiczny w Poznaniu]")
    st.write("✅ Magister - kierunek Rachunkowość i finanse biznesu - Specjalizacja Inwestycje kapitałowe i strategie finansowe przedsiębiorstwa")
    st.write("🔚10/2016 - 06/2019 :orange[|] :green[Uniwersytet Ekonomiczny w Poznaniu]")
    st.write("✅ Licencjat - kierunek Finanse i rachunkowość - Specjalizacja Finanse, Audyt i Podatki")
    st.write("---")

    # ---  Additional certificates  ---

    st.subheader("🕵🏻 Dodatkowe certyfikaty")
    st.write(
    """
- 🟢 CFA Institute Investment Foundations Program Certificate
- 🟢 Certyfikat Akademii Inwestowania nr Z/16/2019 – Program Orlen w Portfelu – poziom 
zaawansowany
- 🟢 The Complete Financial Analyst Course 2020
- 🟢 The Complete Investment Banking Course 2019
    """
    )  
    st.write("---")

    st.subheader("🕵🏻 Wyróżnienia")
    st.write(
    """
    - 🏆 Stypendysta Prezesa Rady Ministrów w roku szkolnym 2015/2016
    - 🏆 Stypendysta Prezydenta Miasta Zielonej Góry w roku szkolnym 2015/2016
    - 🏆 Stypendysta Marszałka Województwa Lubuskiego w roku szkolnym 2015/2016
    - 🏆 Stypendysta Ministra Edukacji Narodowej w roku szkolnym 2015/2016
    - 🏅 Laureat IV Olimpiady Przedsiębiorczości i Zarządzania
    - 🏅 Laureat XX Turnieju Wiedzy i Umiejętności Handlowo-Menedżerskich
    - 🏅 Finalista XXVIII Olimpiady Wiedzy Ekonomicznej
    - 🏅 Finalista XI Olimpiady Przedsiębiorczości
    - 🏅 Finalista IV Ogólnopolskiej Olimpiady Wiedzy o Bankach
    """
    )  
    st.write("---")


    # ---  Hobbies  ---
    analiza_path = os.path.join(script_dir, "assets", "analiza.jpg")
    analiza_pic = Image.open(analiza_path)

    sauna_path = os.path.join(script_dir, "assets", "sauna.jpg")
    sauna_pic = Image.open(sauna_path)

    st.subheader("🙈 Hobby")

    # Hero section

    col1, col2 = st. columns(2, gap="small")
    with col1:
        st.write("☀️  Saunowanie")
        st.image(sauna_pic, width=340)

    with col2:
        st.write("📊  Analiza danych")        
        st.image(analiza_pic, width=290)

    st.write("---")
    st.write(":green[Wyrażam zgodę na przetwarzanie moich danych osobowych dla potrzeb niezbędnych do realizacji procesu rekrutacji.]")

# --- LOAD CSS, PDF & PROFIL ---
def display_english_cv():
    profile_pic = Image.open(image_path)

    link = "https://www.linkedin.com/in/patryk-r%C4%85k-3341939b"
    path_url = "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"

    # Hero section

    col1, col2 = st. columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=340)

    with col2:
        st.write('#')
        st.write('#')
        st.title(NAME)
        st.write(DESCRIPTION)
        st.markdown(f'<a href="{link}"><img src="{path_url}" width=35 height=35 /></a>', unsafe_allow_html=True)
        st.write("🌎 Poznań")
        st.write("☎️ 733 144 469")
        st.write(EMAIL)

    # Tech stack


    python_path = os.path.join(script_dir, "assets", "python.jpg")
    python_pic = Image.open(python_path)

    sql_path = os.path.join(script_dir, "assets", "sql.jpg")
    sql_pic = Image.open(sql_path)

    bpmn_path = os.path.join(script_dir, "assets", "bpmn.jpg")
    bpmn_pic = Image.open(bpmn_path)   
    
    col1, col2, col3 = st. columns(3, gap="small")

    with col1:
        st.write("#")
        st.write(":orange[★✰✰] :green[| Python - junior |]")
        with open(python_path, 'rb') as f:
            data = f.read()
            st.download_button(
                label="🕵🏽‍♂️ Certyfikat",
                data=data,
                file_name="python.jpg",
                mime="image/jpeg",
            )

    with col2:
        st.write("#")
        st.write(":orange[★★✰] :green[| SQL - regular |]")
        with open(sql_path, 'rb') as f:
            data = f.read()
            st.download_button(
                label="🕵🏽‍♂️ Certyfikat",
                data=data,
                file_name="sql.jpg",
                mime="image/jpeg",
            )
     
    with col3:
        st.write("#")
        st.write(":orange[★★✰] :green[| BPMN - regular |]")
        with open(bpmn_path, 'rb') as f:
            data = f.read()
            st.download_button(
                label="🕵🏽‍♂️ Certyfikat",
                data=data,
                file_name="bpmn.jpg",
                mime="image/jpeg",
            )      

    col1, col2, col3, col4 = st. columns(4, gap="small") 

    with col2:
        st.write("#")
        st.write(":orange[★★✰]")
        st.write(":green[| VBA - regular |]")

    with col3:
        st.write("#")
        st.write(":orange[★★★]")
        st.write(":green[| MS Excel - advanced |]")   

    # Experience & Qualifications

    st.write("#")
    st.subheader("Experience & Qualifications")
    st.write(
    """
    - ✅  💻  5 Years experience as a Transfer Pricing Consultant
    - ✅  📈  4 Years experience as a Stock Market Investor
    - ✅  📥  Experienced in designing and implementing IT tools that improve workflow efficiency and streamline processes, leveraging technical knowledge and strong problem-solving skills
    - ✅  👊🏾  Excellent team-player and displaying strong sense of initiative on tasks
    """
    )

    # Hard skills - Operation of programs
    st.write("#")
    st.subheader("Hard skills - Operation of programs")
    st.write(
    """
    - ✅  👩‍💻  Programme operation: MS Office tools, Insert GT, Płatnik, GitLab, CRM, Transfer Pricing Manager, Company Value Radar
    - ✅  🗄️  Database operation: Quick Analytics, Amadeus, Royalty Range, Legalis, LEX Informator Legal and Economic, EMIS Professional, Notoria Serwis
    - ✅  📊  Data Visulization: MS Excel, Python - Matplotlib, Seaborn
    """
    )

    # Languages
    st.write("#")
    st.subheader("Languages")
    st.write(
    """
    - ✴️ English :orange[|] :green[Upper-intermediate]:orange[|] B2/C1
    - ✴️ German :orange[|] :green[Elementary] :orange[|] A2
    """
    )


    st.write("---")

    # --- WORK HISTORY ---
    link_swgk = "https://www.linkedin.com/company/swgk/mycompany/?viewAsMember=true"
    link_cvr = "https://companyvalueradar.com/"

    st.subheader("👷 Work History")

    # --- JOB 1
    st.write("🔛  10/2017 - Present :orange[|] :green[ Junior Assistant➡️Manager] :orange[|] Transfer Pricing Department")
    st.markdown(f'<a href="{link_swgk}">👉SWGK Group👈</a>', unsafe_allow_html=True)        
    st.write(
        """
    As a Manager at SWGK Group, I play a key role in driving the success of transfer pricing projects and team. My responsibilities include overseeing project delivery, implementing control procedures, and designing IT solutions that meet the needs of the company's advisory services.

    As part of my day-to-day work, I was involved in, among other things, the preparation of Local file and Master file, ongoing consultancy, the development of settlement models for group services and the creation of transfer pricing policies. I also have experience in the use of IT tools that assisted me in the preparation and management of transfer pricing documentation. 
    """
    )

    # --- JOB 2
    st.write("#")
    st.write("🔛  07/2019 - Present  :orange[|]:green[  Business and Valuation Analyst]")
    st.markdown(f'<a href="{link_cvr}">👉Company Value Radar👈</a>', unsafe_allow_html=True)        
    st.write(
        """
    As a Business and Valuation Analyst, I work with the IT department to develop a web application for company valuations. I utilize my expertise in data analysis and financial modeling to provide clients with accurate and insightful valuations.
    """
    )
    st.write("---")

    # ---  EDUCATION ---

    st.subheader("🧑🏻‍🎓 Education")

    # --- ED 1
    st.write("🔚10/2021 - 05/2022 :orange[|] :green[Poznań University of Economics and Business]")
    st.write("✅ Postgraduate studies - CIMA Finance Leadership - Operational Level")
    st.write("🔚10/2019 - 07/2021 :orange[|] :green[Poznań University of Economics and Business]")
    st.write("✅ Master's degree in Accounting and Business Finance - Specialization Capital investments and financial strategies")
    st.write("🔚10/2016 - 06/2019 :orange[|] :green[Poznań University of Economics and Business]")
    st.write("✅ Bachelor's degree in Finance and Accounting - Specialization Finance, Audit and Tax")
    st.write("---")

    # ---  Additional certificates  ---

    st.subheader("🕵🏻 Additional certificates")
    st.write(
    """
    - 🟢 CFA Institute Investment Foundations Program Certificate
    - 🟢 Investing Academy Certificate No. Z/16/2019 - Orlen Portfolio Programme - level advanced
    - 🟢 The Complete Financial Analyst Course 2020
    - 🟢 The Complete Investment Banking Course 2019
    """
    )  
    st.write("---")

    st.subheader("🕵🏻 Achievements")
    st.write(
    """
    - 🏆 Scholarship recipient from the Prime Minister's Council - 2015/2016
    - 🏆 Scholarship recipient from the Mayor of the City of Zielona Góra - 2015/2016
    - 🏆 Scholarship recipient from the Marshal of the Lubuskie Province - 2015/2016
    - 🏆 Scholarship recipient from the Minister of National Education - 2015/2016
    - 🏅 Laureate of the 4th Entrepreneurship and Management Olympiad
    - 🏅 Laureate of the 20th Tournament of Business and Management Knowledge and Skills
    - 🏅 Finalist of the 28th Economic Knowledge Olympiad
    - 🏅 Finalist of the 11th Entrepreneurship Olympiad
    - 🏅 Finalist of the 4th National Banking Knowledge Olympiad
    """
    )  
    st.write("---")


    # ---  Hobbies  ---

    analiza_path = os.path.join(script_dir, "assets", "analiza.jpg")
    analiza_pic = Image.open(analiza_path)

    sauna_path = os.path.join(script_dir, "assets", "sauna.jpg")
    sauna_pic = Image.open(sauna_path)


    st.subheader("🙈 Hobbies")

    # Hero section

    col1, col2 = st. columns(2, gap="small")
    with col1:
        st.write("☀️  Sauning")
        st.image(sauna_pic, width=340)

    with col2:
        st.write("📊  Data analysis")        
        st.image(analiza_pic, width=290)

    st.write("---")
    st.write(":green[I consent to the processing of my personal data for the purposes of the recruitment process.]")


if language == 'Angielski ✅':
    display_english_cv()
else:
    display_polish()

