import streamlit as st
import sqlite3
import pandas as pd

# Funkcja do wyszukiwania danych w bazie SQLite
def search_by_year(year):
    conn = sqlite3.connect('test.db')  # połącz z bazą danych SQLite
    query = "SELECT id, title, author, year, abstract, doi, entry_type, keywords FROM Bibliografia WHERE year = ?"
    df = pd.read_sql_query(query, conn, params=(year,))
    conn.close()
    return df

# Interfejs aplikacji
st.title("Wyszukiwarka Bibliografii")

# Pole do wpisania roku
year = st.text_input("Podaj rok publikacji:", "")

# Przycisk do uruchomienia wyszukiwania
if st.button("Szukaj"):
    if year:
        # Pobieranie wyników z bazy danych
        results = search_by_year(year)

        if not results.empty:
            # Wyświetlanie wyników
            for index, row in results.iterrows():
                st.write(f"### Publikacja {index + 1}")
                st.write(f"**ID:** {row['id']}")
                st.write(f"**Autorzy:** {row['author']}")
                st.write(f"**Tytuł:** {row['title']}")
                st.write(f"**Keywords:** {row['keywords']}")
                st.write(f"**Rok:** {row['year']}")
                st.write(f"**Abstrakt:** {row['abstract']}")
                st.write(f"**DOI:** {row['doi'] if row['doi'] else 'Brak'}")
                st.write("---")  # Dodaje linię oddzielającą wyniki
        else:
            st.write("Brak wyników dla podanego roku.")
    else:
        st.write("Proszę podać rok publikacji.")
