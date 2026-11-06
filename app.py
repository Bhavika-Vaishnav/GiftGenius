
import streamlit as st
import html
import pandas as pd

from modules.recommender import recommend_gifts
from modules.database import (
    create_database,
    add_favorite,
    get_favorites,
    add_search_history,
    get_search_history,
    delete_search_history
)


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="GiftGenius | AI Gift Finder",
    page_icon="🎁",
    layout="wide",
    initial_sidebar_state="collapsed"
)

create_database()


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #f8f7fc;
    color: #29243a;
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

#MainMenu, footer, header {
    visibility: hidden;
}

/* HERO SECTION - KEEP CURRENT DESIGN */

.hero {
    background: linear-gradient(120deg, #31205f, #7146a8, #bd78b8);
    padding: 65px 30px;
    border-radius: 28px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 15px 40px rgba(65, 39, 105, 0.18);
}

.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 52px;
    font-weight: 700;
    letter-spacing: -1px;
    margin-bottom: 12px;
    color: white;
}

.hero p {
    font-size: 16px;
    color: #f5eaff;
    line-height: 1.8;
    margin-bottom: 5px;
}

/* INTRO CARD */

.intro-card {
    background: white;
    border: 1px solid #eee8f7;
    padding: 22px 26px;
    border-radius: 18px;
    margin-bottom: 30px;
    box-shadow: 0 5px 20px rgba(49, 32, 95, 0.04);
}

.intro-card p {
    color: #696176;
    font-size: 14px;
    line-height: 1.9;
    margin: 0;
}

/* SECTION HEADINGS */

.section-heading {
    color: #49316f;
    font-size: 25px;
    font-weight: 800;
    margin-top: 28px;
    margin-bottom: 18px;
}

/* SEARCH FORM */

[data-testid="stForm"] {
    background: white;
    border: 1px solid #eee8f7;
    border-radius: 22px;
    padding: 28px;
    box-shadow: 0 8px 28px rgba(49, 32, 95, 0.05);
}

/* INPUT LABELS */

[data-testid="stWidgetLabel"] p {
    color: #49316f !important;
    font-weight: 600;
    font-size: 14px;
}

/* SELECT BOX AND MULTISELECT */

div[data-baseweb="select"] > div {
    border-radius: 12px;
    border-color: #e5d9f2;
    background: #fdfcff;
}

div[data-baseweb="select"] > div:hover {
    border-color: #a78bca;
}

/* PURPLE MULTISELECT TAGS */

[data-baseweb="tag"] {
    background: #7650a3 !important;
    border: none !important;
    border-radius: 8px !important;
}

[data-baseweb="tag"] span,
[data-baseweb="tag"] svg {
    color: white !important;
    fill: white !important;
}

/* PURPLE SLIDER */

div[data-testid="stSlider"] [data-baseweb="slider"] {
    --slider-color: #7650a3;
}

div[data-testid="stSlider"] [data-baseweb="slider"] [role="slider"] {
    background-color: #7650a3 !important;
    border: 2px solid #7650a3 !important;
}

div[data-testid="stSlider"] [data-baseweb="slider"] [role="progressbar"] {
    background-color: #7650a3 !important;
}

/* Slider labels and values */

div[data-testid="stSlider"] {
    color: #7650a3 !important;
}

div[data-testid="stSlider"] [data-testid="stThumbValue"] {
    color: #7650a3 !important;
}

/* FORM SUBMIT BUTTON */

div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(100deg, #65418f, #a15ba9) !important;
    color: white !important;
    border: none !important;
    border-radius: 14px !important;
    min-height: 48px !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    box-shadow: 0 5px 15px rgba(101, 65, 143, 0.2) !important;
}

div[data-testid="stFormSubmitButton"] button:hover {
    background: #49316f !important;
    color: white !important;
    transform: translateY(-2px);
}

/* OTHER BUTTONS */

.stButton > button {
    border-radius: 12px;
    border: 1px solid #7650a3;
    background: linear-gradient(100deg, #65418f, #a15ba9);
    color: white;
    font-weight: 700;
    padding: 10px 16px;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    border-color: #49316f;
    background: #49316f;
    color: white;
    transform: translateY(-1px);
}

/* GIFT CARDS */

.gift-card {
    background: white;
    border: 1px solid #eee8f7;
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 10px;
    min-height: 245px;
    box-shadow: 0 6px 22px rgba(49, 32, 95, 0.05);
}

.gift-card h3 {
    color: #49316f;
    font-size: 20px;
    font-weight: 800;
    margin: 12px 0;
}

.gift-category {
    display: inline-block;
    background: #f2eafa;
    color: #7545a0;
    padding: 6px 13px;
    border-radius: 30px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.4px;
}

.gift-description {
    color: #777083;
    font-size: 13px;
    line-height: 1.7;
    min-height: 42px;
}

.gift-price {
    color: #8b4db0;
    font-size: 24px;
    font-weight: 800;
    margin-top: 12px;
}

.match-label {
    color: #7650a3;
    font-size: 13px;
    font-weight: 700;
}

/* PROGRESS BAR */

div[data-testid="stProgress"] > div > div > div {
    background-color: #7650a3 !important;
}

/* PURPLE INFORMATION MESSAGES */

div[data-testid="stAlert"] {
    background: #f2eafa !important;
    border: 1px solid #e1d1f0 !important;
    border-radius: 12px !important;
}

div[data-testid="stAlert"] p {
    color: #65418f !important;
}

div[data-testid="stAlert"] svg {
    color: #7650a3 !important;
}

/* CUSTOM TABLES */

.custom-table-wrapper {
    background: white;
    border: 1px solid #e9e1f1;
    border-radius: 16px;
    overflow: hidden;
    margin: 12px 0 20px 0;
}

.custom-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
}

.custom-table th {
    background: #f2eafa;
    color: #49316f;
    text-align: left;
    padding: 15px;
    font-weight: 700;
}

.custom-table td {
    padding: 14px 15px;
    color: #514961;
    border-top: 1px solid #eee8f7;
}

.custom-table tr:hover td {
    background: #faf7fd;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #88749f;
    font-size: 13px;
    padding: 25px 0 10px;
}

hr {
    border-color: #e9e1f1;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HELPER FUNCTION FOR TABLES
# --------------------------------------------------

def display_custom_table(headers, rows):

    header_html = "".join(
        f"<th>{html.escape(str(header))}</th>"
        for header in headers
    )

    row_html = ""

    for row in rows:
        cells = "".join(
            f"<td>{html.escape(str(value))}</td>"
            for value in row
        )

        row_html += f"<tr>{cells}</tr>"

    table_html = f"""
    <div class="custom-table-wrapper">
        <table class="custom-table">
            <thead>
                <tr>{header_html}</tr>
            </thead>
            <tbody>
                {row_html}
            </tbody>
        </table>
    </div>
    """

    st.html(table_html)


# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.html("""
<div class="hero">
    <h1>🎁 GiftGenius</h1>
    <p>Thoughtful gifting, made effortless.</p>
    <p>Discover meaningful gifts tailored to every person, interest and occasion.</p>
</div>
""")

st.html("""
<div class="intro-card">
    <p>
        Finding the perfect gift doesn't have to be difficult!
        Tell us about the recipient, their interests, the occasion,
        and your budget. GiftGenius will recommend gifts that match
        your preferences using an AI-powered recommendation system.
    </p>
</div>
""")


# --------------------------------------------------
# GIFT SEARCH FORM
# --------------------------------------------------

st.markdown(
    '<div class="section-heading">✨ Find the Perfect Gift</div>',
    unsafe_allow_html=True
)

with st.form("gift_search_form"):

    col1, col2 = st.columns(2)

    with col1:

        recipient = st.selectbox(
            "Who are you shopping for?",
            [
                "Friend",
                "Mother",
                "Father",
                "Brother",
                "Sister",
                "Partner"
            ]
        )

        interests = st.multiselect(
            "What are their interests?",
            [
                "Art",
                "Sketching",
                "Music",
                "Technology",
                "Travel",
                "Photography",
                "Sports",
                "Fashion",
                "Reading",
                "Cooking"
            ],
            default=["Art"]
        )

    with col2:

        occasion = st.selectbox(
            "What's the occasion?",
            [
                "Birthday",
                "Anniversary",
                "Graduation",
                "Wedding",
                "Festival",
                "Thank You",
                "Just Because"
            ]
        )

        budget = st.slider(
            "Your budget (₹)",
            min_value=100,
            max_value=10000,
            value=2000,
            step=100
        )

    submitted = st.form_submit_button(
        "✨ Find Perfect Gifts",
        use_container_width=True,
        type="primary"
    )


# --------------------------------------------------
# RECOMMENDATIONS
# --------------------------------------------------

if submitted:

    if not interests:

        st.warning("Please select at least one interest.")

    else:

        recommendations = recommend_gifts(
            recipient,
            interests,
            occasion,
            budget
        )

        add_search_history(
            recipient,
            interests,
            occasion,
            budget
        )

        st.session_state["recommendations"] = recommendations

        st.rerun()


# --------------------------------------------------
# DISPLAY RECOMMENDATIONS
# --------------------------------------------------

if "recommendations" in st.session_state:

    recommendations = st.session_state["recommendations"]

    st.markdown("---")

    st.markdown(
        '<div class="section-heading">💜 Recommended Gifts for You</div>',
        unsafe_allow_html=True
    )

    if recommendations.empty:

        st.info(
            "No gifts found within your budget. Try increasing your budget."
        )

    else:

        st.success(
            f"We found {len(recommendations)} gift ideas for you!"
        )

        for start in range(0, len(recommendations), 2):

            columns = st.columns(2)

            for offset, column in enumerate(columns):

                index = start + offset

                if index >= len(recommendations):
                    break

                gift = recommendations.iloc[index]

                gift_name = str(gift["gift_name"])
                category = str(gift["category"])
                description = str(gift["description"])
                price = float(gift["price"])
                match = float(gift["match_percentage"])

                safe_name = html.escape(gift_name)
                safe_category = html.escape(category)
                safe_description = html.escape(description)

                with column:

                    st.html(f"""
                    <div class="gift-card">
                        <span class="gift-category">
                            {safe_category}
                        </span>

                        <h3>🎁 {safe_name}</h3>

                        <p class="gift-description">
                            {safe_description}
                        </p>

                        <div class="gift-price">
                            ₹{price:,.0f}
                        </div>

                        <p class="match-label">
                            ✨ {match:.2f}% Match
                        </p>
                    </div>
                    """)

                    st.progress(
                        min(max(match / 100, 0.0), 1.0)
                    )

                    if st.button(
                        "💜 Save to Favourites",
                        key=f"favorite_{gift['gift_id']}",
                        use_container_width=True
                    ):

                        saved = add_favorite(
                            gift_name,
                            price
                        )

                        if saved:
                            st.success("Gift saved to favourites!")
                        else:
                            st.info(
                                "This gift is already in your favourites."
                            )


# --------------------------------------------------
# FAVOURITE GIFTS
# --------------------------------------------------

st.markdown("---")

st.markdown(
    '<div class="section-heading">💖 Your Favourite Gifts</div>',
    unsafe_allow_html=True
)

favorites = get_favorites()

if favorites:

    favorite_rows = []

    for favorite in favorites:

        favorite_rows.append([
            favorite[1],
            f"₹{favorite[2]:,.0f}"
        ])

    display_custom_table(
        ["Gift Name", "Price"],
        favorite_rows
    )

else:

    st.html("""
    <div style="
        background:#f2eafa;
        border:1px solid #e1d1f0;
        padding:16px 20px;
        border-radius:12px;
        color:#65418f;
        margin:12px 0;
    ">
        💜 You haven't saved any favourite gifts yet.
        Save a gift from your recommendations!
    </div>
    """)


# --------------------------------------------------
# SEARCH HISTORY
# --------------------------------------------------

st.markdown("---")

st.markdown(
    '<div class="section-heading">📜 Search History</div>',
    unsafe_allow_html=True
)

history = get_search_history()

if history:

    history_rows = []

    for item in history:

        history_rows.append([
            item[0],
            item[1].replace(";", ", "),
            item[2],
            f"₹{item[3]:,.0f}",
            item[4]
        ])

    display_custom_table(
        [
            "Recipient",
            "Interests",
            "Occasion",
            "Budget",
            "Search Date"
        ],
        history_rows
    )

    if "confirm_delete_history" not in st.session_state:
        st.session_state.confirm_delete_history = False

    if st.button(
        "🗑️ Delete Search History",
        key="delete_history_button"
    ):

        st.session_state.confirm_delete_history = True

    if st.session_state.confirm_delete_history:

        st.warning(
            "Are you sure you want to delete all your search history?"
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "Yes, Delete All",
                key="confirm_delete"
            ):

                delete_search_history()

                st.session_state.confirm_delete_history = False

                st.success("Search history deleted successfully!")

                st.rerun()

        with col2:

            if st.button(
                "Cancel",
                key="cancel_delete"
            ):

                st.session_state.confirm_delete_history = False

                st.rerun()

else:

    st.html("""
    <div style="
        background:#f2eafa;
        border:1px solid #e1d1f0;
        padding:16px 20px;
        border-radius:12px;
        color:#65418f;
        margin:12px 0;
    ">
        📜 Your search history will appear here.
    </div>
    """)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.html("""
<div class="footer">
    <p>Made with 💜 using Python, Streamlit and Machine Learning</p>
    <p>Created with ❤️ by Bhavika</p>
</div>
""")
