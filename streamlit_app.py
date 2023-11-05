import streamlit as st
import pandas as pd

# Function to filter data based on user input
def filter_data(df, name, status, capital, type_company, city, province):
    if name:
        df = df[df['Company Name'].str.contains(name, case=False)]
    if status:
        df = df[df['Business Status'] == status]
    if capital:
        df = df[df['Registered Capital'] == capital]
    if type_company:
        df = df[df['Type of Company'] == type_company]
    if city:
        df = df[df['City'] == city]
    if province:
        df = df[df['Provice'] == province]
    return df

# Streamlit app layout
def main():
    # Load the data
    df = pd.read_excel('Printing company Short.xlsx')

    # Unique values for dropdowns
    status_options = df['Business Status'].unique().tolist()
    capital_options = df['Registered Capital'].unique().tolist()
    type_company_options = df['Type of Company'].unique().tolist()
    city_options = df['City'].unique().tolist()
    province_options = df['Provice'].unique().tolist()

    # App initialization
    st.set_page_config(page_title="Asia Pilots", layout="wide")

    # Sidebar
    with st.sidebar:
        st.header('Asia Pilots')
        st.header('Search & Filter')
        name_input = st.text_input('Company Name')

        # Dropdown filters
        status_input = st.selectbox('Business Status', options=[''] + status_options)
        capital_input = st.selectbox('Registered Capital', options=[''] + capital_options)
        type_company_input = st.selectbox('Type of Company', options=[''] + type_company_options)
        city_input = st.selectbox('City', options=[''] + city_options)
        province_input = st.selectbox('Province', options=[''] + province_options)

        # Filter button
        filter_button = st.button('Apply Filter')

    # Main Page
    st.title('List of Chinese Companies')

    # Displaying the filtered dataframe
    if filter_button:
        df_filtered = filter_data(df, name_input, status_input, capital_input, type_company_input, city_input, province_input)
    else:
        df_filtered = df.copy()

    # Display the dataframe in the main page
    st.dataframe(df_filtered)

    # Select a company to view details
    if not df_filtered.empty:
        company_names = df_filtered['Company Name'].tolist()
        selected_company_name = st.selectbox('Select a company to view details', company_names)
        selected_company = df_filtered[df_filtered['Company Name'] == selected_company_name].iloc[0]

        # Display the selected company profile
        with st.container():
            st.header('Company Profile')
            st.write(f"**Company Name**: {selected_company['Company Name']}")
            st.write(f"**Legal Representative**: {selected_company['Legal Representative']}")
            st.write(f"**Registered Capital**: {selected_company['Registered Capital']}")
            st.write(f"**Establishment Date**: {selected_company['Establishment Date']}")
            st.write(f"**Unified Social Credit**: {selected_company['Unified Social Credit']}")
            st.write(f"**Insured Persons**: {selected_company['Insured Persons']}")
            st.write(f"**Type of Company**: {selected_company['Type of Company']}")
            st.write(f"**Website**: {selected_company['Website']}")
            st.write(f"**Telephone**: {selected_company['Telephone']}")
            st.write(f"**E-Mail**: {selected_company['E-Mail']}")
            st.write(f"**International Offices**: {selected_company['International Offices']}")
            st.write(f"**Offices in China**: {selected_company['Offices in China']}")
            st.write(f"**Company Description**: {selected_company['Company Description']}")
            st.write(f"**Management Team**: {selected_company['Management Team']}")
            st.write(f"**Products and Product Categories**: {selected_company['Products and Product Categories']}")
            st.write(f"**Customer Information**: {selected_company['Customer Information']}")
            st.write(f"**Contact Information**: {selected_company['Contact Information']}")
            # You can add more details as needed here.

if __name__ == "__main__":
    main()


