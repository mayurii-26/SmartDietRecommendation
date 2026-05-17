# SmartDietRecommendation
A Machine Learning Smart Diet Recommendation web application developed using ML Algorithms and Streamlit.  The system predicts the most suitable diet plan based on user health details, lifestyle habits, BMI, calorie intake, diseases, allergies, and nutritional preferences.

# 🚀 Features

✅ Personalized Diet Recommendation  
✅ BMI Calculation  
✅ Interactive Modern UI  
✅ Machine Learning Prediction  
✅ Health Tips & Lifestyle Suggestions  
✅ Multiple ML Algorithms Comparison  
✅ Streamlit Web Application

---

# 🧠 Machine Learning Algorithms Used

- Random Forest
- KNN (K-Nearest Neighbors)
- SVM (Support Vector Machine)
- Naive Bayes
- K-Means Clustering

The project uses multiple Machine Learning algorithms for training and accuracy comparison:

| Algorithm | Purpose |
|---|---|
| Random Forest | Final prediction model |
| K-Nearest Neighbors (KNN) | Accuracy comparison |
| Support Vector Machine (SVM) | Accuracy comparison |
| Naive Bayes | Accuracy comparison |
| K-Means Clustering | Data analysis and experimentation |

Final deployed prediction model:
✅ Random Forest Classifier

Reason:
- Highest accuracy
- Better performance
- Handles multiple features efficiently
- Stable predictions
  
---

# 📊 Input Parameters

The system takes the following health parameters:

- Age
- Gender
- Weight
- Height
- BMI
- Disease Type
- Severity Level
- Physical Activity
- Daily Calories
- Cholesterol
- Blood Pressure
- Glucose Level
- Dietary Restrictions
- Allergies
- Preferred Cuisine
- Weekly Exercise Hours
- Diet Adherence
- Nutrient Deficiency

Based on these inputs, the system predicts the most suitable diet category using trained Machine Learning models.
---

# 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-Learn
- Pandas
- NumPy
- Joblib
- PIL

---

# 📁 Project Structure

```bash
SmartDietRecommendation/
│
├── app.py
├── model.ipynb
├── rf_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
│
├── images/
│   ├── banner.png
│   ├── diet.png
```

---

# ▶️ Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# 🌐 Deployment

This project is deployed using Streamlit Community Cloud.

---

# 📌 Future Improvements

- AI chatbot integration
- Real-time nutrition tracking
- Meal planning
- Fitness recommendation system
- User authentication
