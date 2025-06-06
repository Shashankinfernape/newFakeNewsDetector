
📰 Fake News Detection Using Machine Learning
🚀 Live Demo: https://selvagangleaderxx.streamlit.app/

This project aims to detect fake news articles using supervised machine learning algorithms. It classifies news articles as either "Fake" or "True" based on the textual content, using natural language processing techniques and popular ML models. This solution can help combat misinformation by automatically identifying untrustworthy news sources.

📁 Project Structure
1. Data Loading
The dataset includes:

Fake.csv: Contains fake news articles.

True.csv: Contains true news articles.

These files are used for model training and evaluation.

2. Data Preprocessing
Text data is cleaned and normalized through:

Conversion to lowercase

Removal of punctuation, special characters, and URLs

(Optional) Tokenization and stopword removal

3. Feature Extraction
Text data is converted to numeric format using:

TF-IDF (Term Frequency-Inverse Document Frequency): Measures the importance of words in the document context.

4. Model Training
The following models are trained and tested:

Logistic Regression

Decision Tree Classifier

Gradient Boosting Classifier

Random Forest Classifier

5. Evaluation Metrics
Models are evaluated based on:

Accuracy

Precision

Recall

F1-score

📊 Results:
Logistic Regression: 95.56% accuracy

Decision Tree Classifier: 93.86% accuracy

Gradient Boosting Classifier: 93.90% accuracy

Random Forest Classifier: Performed competitively

🛠 How to Use
1. Clone the Repository
bash https://github.com/Shashankinfernape/newFakeNewsDetector.git
cd Fake-News-Detection

2. Install Dependencies
bash
pip install pandas numpy scikit-learn matplotlib seaborn

3. Run the Jupyter Notebook
Open Fake News Detection using machine learning.ipynb in Jupyter Notebook or Google Colab, and execute the cells sequentially to:

Preprocess the data

Train ML models

Evaluate model performance

📦 Dataset
Ensure these files are present inside the data/ directory:

Fake.csv

True.csv

manual_testing.csv (optional for manual input testing)

Note: Dataset files are not included in the repository due to size restrictions.

🤝 Contributors
Sarathy 

Shashank 

Suresh 

Selvaganapathy 

🔮 Future Work
✅ Deep Learning Integration: Explore LSTM or BERT for improved results.

✅ Web Deployment: Model already deployed on Streamlit.

⏳ Dataset Expansion: Add more languages and diversified sources.

📜 License
This project is open-source and licensed under the MIT License.
Feel free to use, modify, and share the code.
