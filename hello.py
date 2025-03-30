import time
import streamlit as st

from lib.chatgpt_util import get_book_recommendation

def main():
    def check_easter_eggs():
        if "harry potter" in [b.lower() for b in books]:
            st.balloons()
            st.info("🧙‍♂️ Harry Potter? Ah, a fellow wizard.")

    st.title("📚 Book Recommender 📚")
    st.markdown("> _“A reader lives a thousand lives before he dies.”_ — George R.R. Martin")
    st.markdown("---")

    st.markdown("### 👋 Hey there, bookworm!")
    st.markdown("Tell me a few books you **loved**, and I'll divine your next literary soulmate.")

    col1, col2, col3 = st.columns(3)
    with col1:
        book1 = st.text_input("1st Book You Loved", placeholder="e.g. 1984")
    with col2:
        book2 = st.text_input("2nd Book", placeholder="e.g. Dune")
    with col3:
        book3 = st.text_input("3rd Book", placeholder="e.g. The Alchemist")

    books = [book for book in (book1, book2, book3) if book.strip()]

    if st.button("Dear reader, click here for your next read"):
        if not books:
            st.warning("Sorry bud! No books = no recommendations :(")
        
        with st.spinner("Consulting the great library spirits..."):
            check_easter_eggs()
            time.sleep(0.5)

            st.info("🧙 Whispering through parchment... 📜")
            
            book_recommendation = get_book_recommendation(books=books)
            time.sleep(1)
            
            st.success("Your recommendation is ready. Enjoy!")

            if book_recommendation:
                st.warning(book_recommendation)
                st.subheader(f"📖 {book_recommendation['title']}")
                st.markdown(f"**Why this book?** {book_recommendation['reason']}")


if __name__ == "__main__":
    main()