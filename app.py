import streamlit as st
from some_module import parse_pdf, generate_vectors, store_vectors, query_engine

def main():
    st.title('Content Engine')
    query = st.text_input('Enter your query:')
    
    if st.button('Submit'):
        vectors, texts = parse_pdf()
        collection = store_vectors(vectors, texts)
        results = query_engine(query, collection)
        
        st.write("Search Results:")
        for result in results:
            st.write(result)
        
if __name__ == '__main__':
    main()
