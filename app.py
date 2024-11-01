import streamlit as st
import sqlite3
import pandas as pd

# Funkcja do wyszukiwania danych w bazie SQLite
def search_by_year(year):
    conn = sqlite3.connect('test2.db')  # połącz z bazą danych SQLite
    query = "SELECT id, title, author, year, abstract, doi, entry_type, keywords FROM Bibliografia WHERE year = ?"
    df = pd.read_sql_query(query, conn, params=(year,))
    conn.close()
    return df

# Interfejs aplikacji
st.title("Search publications by year")

# Pole do wpisania roku
year = st.text_input("Year of publication:", "")

# Przycisk do uruchomienia wyszukiwania
if st.button("Search"):
    if year:
        # Pobieranie wyników z bazy danych
        results = search_by_year(year)
        # Nowe okno
        with st.expander("Wyniki wyszukiwania", expanded=True):
            if not results.empty:
                # Wyświetlanie wyników
                st.write("<div style='max-height: 300px; overflow-y: auto;'>", unsafe_allow_html=True)  # Kontener do przewijania
                for index, row in results.iterrows():
                    st.write(f"### Publication {index + 1}")
                    st.write(f"**ID:** {row['id']}")
                    st.write(f"**Authors:** {row['author']}")
                    st.write(f"**Title:** {row['title']}")
                    st.write(f"**Keywords:** {row['keywords']}")
                    st.write(f"**Year:** {row['year']}")
                    st.write(f"**Abstract:** {row['abstract']}")
                    st.write(f"**DOI:** {row['doi'] if row['doi'] else 'Brak'}")
                    st.write("---")  # Dodaje linię oddzielającą wyniki
                st.write("</div>", unsafe_allow_html=True)
            else:
                st.write("No results for the year specified.")
    else:
        st.write("Please indicate the year of publication.")
