# 🎁 GiftGenius – AI-Powered Personalized Gift Finder

GiftGenius is an AI-powered gift recommendation web application that helps users discover thoughtful and personalized gifts based on the recipient, their interests, the occasion, and their budget.

The application uses **Machine Learning and content-based recommendation techniques** to suggest relevant gift options through a simple and interactive interface.

## ✨ Features

- **Personalized Recommendations:** Find gifts based on recipient preferences and interests.
- **Budget-Based Filtering:** Get gift suggestions within your selected budget.
- **Machine Learning:** Uses TF-IDF vectorization and cosine similarity to calculate gift relevance.
- **Match Percentage:** Displays how closely each gift matches the user's preferences.
- **Favourite Gifts:** Save your preferred gifts using SQLite.
- **Duplicate Prevention:** Prevents saving the same favourite gift multiple times.
- **Search History:** Stores previous searches for future reference.
- **Interactive Interface:** Clean and user-friendly interface built with Streamlit.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Pandas | Data handling and processing |
| Scikit-learn | Machine Learning and similarity calculations |
| TF-IDF | Text feature extraction |
| Cosine Similarity | Recommendation scoring |
| SQLite | Database management |

## ⚙️ How It Works

1. The user selects the gift recipient.
2. The user chooses their interests and the occasion.
3. The user sets a preferred budget.
4. The system filters gifts according to the budget.
5. TF-IDF converts gift information and user preferences into numerical vectors.
6. Cosine similarity calculates the relevance score.
7. Gifts are sorted by their match percentage.
8. Users can save favourite gifts and view their search history.

## 📁 Project Structure

```text
GiftGenius/
│
├── .streamlit/
│   └── config.toml
│
├── assets/
│
├── data/
│   └── gifts.csv
│
├── modules/
│   ├── database.py
│   └── recommender.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/GiftGenius.git
```

### 2. Navigate to the project directory

```bash
cd GiftGenius
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧠 Recommendation Algorithm

GiftGenius uses a content-based recommendation approach.

- **TF-IDF Vectorization:** Converts gift attributes and user preferences into numerical representations.
- **Cosine Similarity:** Measures similarity between the user's preferences and available gifts.
- **Budget Filtering:** Excludes gifts that exceed the selected budget.
- **Ranking:** Sorts the recommended gifts according to their calculated match percentage.

## 💾 Database

SQLite is used to store:

- Favourite gifts
- Search history

The database is created automatically when the application starts.

## 👩‍💻 Author

**Bhavika Vaishnav**

B.E. Electronics & Telecommunication Engineering  
Specialization: Artificial Intelligence & Machine Learning

---

⭐ If you find this project interesting, consider giving the repository a star!