```markdown
# 🎓 Student Reward Prediction System  

An end-to-end solution for analyzing student performance data and predicting reward categories using machine learning. The system automates decision-making and ensures fairness in reward distribution.  

---

## 📋 Problem Statement  

The project tackles:  
- **Efficient Data Analysis:** Identifying trends and patterns from large-scale student performance data.  
- **Automated Reward Prediction:** Reducing manual errors and enhancing decision-making.  
- **Fair Distribution:** Ensuring unbiased allocation of scholarships and recognitions.  

---

## ✨ Features  

### 🛠 Data Processing  
- **PDF to CSV Conversion:**  
  - Uses `pdfplumber` to extract structured data from PDFs.  
- **Data Cleaning and Normalization:**  
  - Ensures consistency and prepares data for analysis.  

### 📊 Exploratory Data Analysis (EDA)  
- **Visualizations:**  
  - Leverages `matplotlib` and `seaborn` to showcase trends and distributions.  
- **Insights:**  
  - Reward category distribution.  
  - Correlation between academic scores (GPA) and behavioral scores (ĐRL).  

### 🤖 Machine Learning Model  
- **Model:**  
  - Implements a Random Forest Classifier for predicting reward categories.  
- **Performance:**  
  - Achieves an accuracy of **86%** during testing.  

### 🌐 Interactive Application  
- **User Interface:**  
  - Built with `Streamlit` for an intuitive experience.  
- **Functionality:**  
  - Users input performance metrics (academic and behavioral scores) to predict rewards.  

---

## 🚀 How to Run  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-repo/student-reward-prediction.git  
   cd student-reward-prediction  
   ```  

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt  
   ```  

3. **Start the Application**  
   ```bash
   streamlit run app.py  
   ```  

4. **Use the App**  
   - Input scores to get reward predictions.  

---

## 🛠 Technologies  

- **Languages:** Python  
- **Libraries:** Streamlit, pdfplumber, pandas, matplotlib, seaborn, scikit-learn  
- **Machine Learning Model:** Random Forest Classifier  
```  
