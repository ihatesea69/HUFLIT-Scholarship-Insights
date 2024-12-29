Đây là đoạn văn bản đã được viết lại:

---

**Student Reward Prediction System**

This is an end-to-end solution designed to analyze student performance data and predict reward categories using machine learning. The system automates decision-making processes to ensure fairness in the distribution of rewards.

---

**Problem Statement**

This project focuses on solving the following challenges:
- **Efficient Data Analysis**: Identifying trends and patterns from large-scale student performance data.
- **Automated Reward Prediction**: Minimizing manual errors while enhancing the decision-making process.
- **Fair Distribution**: Ensuring an unbiased allocation of scholarships and recognitions.

---

**Features**

- **Data Processing**
  - **PDF to CSV Conversion**: Utilizes `pdfplumber` to extract structured data from PDF documents.
  - **Data Cleaning and Normalization**: Ensures the data is consistent and ready for analysis.

- **Exploratory Data Analysis (EDA)**
  - **Visualizations**: Uses `matplotlib` and `seaborn` to visualize trends and distributions.
  - **Insights**: 
    - Distribution of reward categories.
    - Correlations between academic scores (GPA) and behavioral scores (ĐRL).

- **Machine Learning Model**
  - **Model**: Implements a Random Forest Classifier to predict reward categories.
  - **Performance**: Achieves an accuracy of **86%** during testing.

- **Interactive Application**
  - **User Interface**: Built with `Streamlit` to provide an intuitive experience.
  - **Functionality**: Users can input their academic and behavioral scores to predict reward categories.

---

**How to Run**

1. **Clone the Repository**
   - `git clone https://github.com/your-repo/student-reward-prediction.git`
   - `cd student-reward-prediction`

2. **Install Dependencies**
   - `pip install -r requirements.txt`

3. **Start the Application**
   - `streamlit run app.py`

4. **Use the App**
   - Input the necessary performance scores to get the predicted reward category.

---

**Technologies**

- **Languages**: Python
- **Libraries**: Streamlit, pdfplumber, pandas, matplotlib, seaborn, scikit-learn
- **Machine Learning Model**: Random Forest Classifier
