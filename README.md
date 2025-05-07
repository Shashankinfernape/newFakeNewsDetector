Fake News Detection Using Machine Learning
Overview
This project aims to detect fake news articles using machine learning techniques. The primary objective is to classify news articles as either "fake" or "true" based on their textual content. This project involves data preprocessing, feature extraction, and training multiple machine learning models to achieve high accuracy in classification.

<<<<<<< HEAD
Project Structure
1. Data Loading
The dataset consists of two CSV files:

Fake.csv: Contains fake news articles.
=======
>>>>>>> b8d91aff4a3f984086bdfe3843970e3356aa9ea6

True.csv: Contains true news articles.

These files are used to train and test the model.

2. Data Preprocessing
The text data is cleaned by performing the following operations:

Converting the text to lowercase.

Removing special characters, URLs, and punctuation.

Tokenization and stopword removal (optional).

3. Feature Extraction
The textual data is transformed into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency), which is a statistical method used to evaluate the importance of a word in a document relative to all other documents in the dataset.

4. Model Training
The following machine learning models are trained and evaluated:

Logistic Regression

Decision Tree Classifier

Gradient Boosting Classifier

Random Forest Classifier

5. Evaluation
Each model is evaluated using accuracy and classification metrics, including:

Precision

Recall

F1-score

Results
Logistic Regression: Achieved an accuracy of 95.56%.

Decision Tree Classifier: Achieved an accuracy of 93.86%.

Gradient Boosting Classifier: Achieved an accuracy of 93.90%.

Random Forest Classifier: Performed comparably to other models.

How to Use
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/Shashankinfernape/Fake-News-Detection.git
cd Fake-News-Detection
2. Install Dependencies
bash
Copy
Edit
pip install pandas numpy scikit-learn matplotlib seaborn
3. Run the Jupyter Notebook
Open Fake News Detection using machine learning.ipynb in Jupyter Notebook or any compatible environment.

Execute the cells sequentially to preprocess data, train models, and evaluate performance.

Dataset
The dataset is located in the data directory (not included in the repository). Ensure that you have the following files:

Fake.csv

True.csv

manual_testing.csv (optional for additional testing)

Author
Shashank
GitHub: Shashankinfernape

License
This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as needed.

Future Work
Deep Learning Models: Experiment with advanced deep learning models like LSTM or BERT for improved accuracy.

Web Application Deployment: Deploy the model as a real-time fake news detection web application.

Dataset Expansion: Expand the dataset to include more diverse sources, languages, and topics.

