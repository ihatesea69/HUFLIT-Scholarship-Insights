### **Introduction**

The project "HUFLIT Scholarship Analysis and Prediction" is a comprehensive data science and data analytics solution designed to analyze and predict student rewards based on academic and behavioral performance. The primary objective is to streamline the scholarship allocation process by leveraging machine learning to provide data-driven insights and automate predictions.

This is the user's first project using ChatGPT's assistance, demonstrating the integration of advanced AI technologies into real-world applications. The project utilizes Python for data preprocessing, visualization, and model training, and integrates Streamlit to provide an interactive web-based prediction tool.

---

### **Project Details**

#### **1. Problem Statement**
The project addresses the challenge of analyzing large-scale student performance data to identify patterns and predict the appropriate reward category for students based on their performance metrics. This automates decision-making, reduces human errors, and ensures fair distribution of scholarships and recognitions.

---

#### **2. Key Features**
1. **Data Extraction and Preprocessing:**
   - Converts PDF data into a structured CSV format using `pdfplumber`.
   - Cleans and normalizes data to ensure consistency and readiness for analysis.

2. **Exploratory Data Analysis (EDA):**
   - Visualizes trends and distributions using `matplotlib` and `seaborn`.
   - Insights include:
     - The distribution of students across reward categories.
     - Relationships between academic scores (GPA) and behavioral scores (ĐRL).

3. **Machine Learning Model:**
   - Implements a Random Forest Classifier to predict reward categories based on performance metrics.
   - Achieves an accuracy of 86% during testing, indicating a robust predictive capability.

4. **Interactive Prediction Application:**
   - Developed using Streamlit for an intuitive user interface.
   - Allows users to input performance metrics (academic and behavioral scores) to predict the scholarship or reward category.

---

#### **3. Technical Workflow**
1. **Data Pipeline:**
   - Extract performance data from PDF files.
   - Clean and preprocess the data into numerical formats suitable for analysis and modeling.

2. **Visualization and Reporting:**
   - Generate detailed visualizations to understand patterns in student performance.
   - Save summarized insights into markdown reports for easy sharing.

3. **Model Development:**
   - Prepare the data by splitting it into training and testing sets.
   - Train a Random Forest model and evaluate its performance using precision, recall, and F1-score metrics.

4. **Deployment:**
   - Package the trained model using `joblib`.
   - Deploy the model via a Streamlit application for real-time predictions.

---

#### **4. Tools and Libraries**
- **Python Libraries:** `pandas`, `matplotlib`, `seaborn`, `sklearn`, `pdfplumber`, `streamlit`, `numpy`, `joblib`.
- **Development Environment:** Jupyter Notebook for experimentation and VSCode for production scripts.
- **Web Deployment:** Streamlit for a simple and accessible user interface.

---

#### **5. Applications**
- Automating scholarship evaluations in educational institutions.
- Enhancing transparency and fairness in reward allocation.
- Providing insights for institutional performance improvement.

---

This project highlights the practical application of data science and analytics in solving real-world problems, serving as a foundation for more advanced AI-driven solutions in education.
