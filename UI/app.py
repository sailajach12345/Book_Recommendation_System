import streamlit as st
import requests

st.title("📚 Book Recommendation System")

title = st.text_input("Enter a book title:")

if st.button("Get Recommendations"):
    if title:
        try:
            response = requests.get(f"http://127.0.0.1:5000/recommend?title={title}")
            data = response.json()
            recommendations = data.get("recommendations", [])

            if isinstance(recommendations, list) and len(recommendations) > 0:
                st.subheader("Recommendations:")
                for book in recommendations:
                    if isinstance(book, list) and len(book) == 3:
                        book_title, author, image_url = book
                        st.markdown(f"**{book_title}**  \n*by {author}*")
                        st.image(image_url, width=150)
                        st.markdown("---")
                    else:
                        st.warning(f"Unexpected book format: {book}")
            else:
                st.info("No recommendations found.")
        except Exception as e:
            st.error(f"Failed to fetch recommendations: {e}")
    else:
        st.warning("Please enter a book title.")
