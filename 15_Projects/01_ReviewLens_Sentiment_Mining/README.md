# 📊 ReviewLens: Sentiment Mining from Restaurant Feedback  

> 🔎 *"Turning customer voices into data-driven insights with NLP"*  

---

## 📌 Project Overview
Customer reviews hold valuable information about **satisfaction, complaints, and expectations**.  
However, manually reading thousands of reviews is impossible.  

**ReviewLens** is an **NLP-powered sentiment analysis system** that classifies restaurant reviews as **Positive 😊 or Negative 😠**.  
This helps businesses **automatically monitor customer satisfaction** and take **data-driven decisions**.

---

## 🎯 Objectives
- Clean and preprocess raw text reviews  
- Extract features using **Bag of Words (BoW)** and **TF-IDF**  
- Train multiple ML models for classification  
- Evaluate performance and identify the **best performing model**  
- Provide business insights from the results  

---

## 📂 Project Structure
```
01_ReviewLens_Sentiment_Mining/
├─ data/
│  └─ Restaurant_Reviews.tsv
└─ ReviewLens_Final_Pipeline.ipynb
```

- `data/` → contains the dataset (`Restaurant_Reviews.tsv`)  
- `ReviewLens_Final_Pipeline.ipynb` → complete end-to-end pipeline notebook  

---

## 🗂️ Dataset
- Source: Restaurant review dataset (TSV format, 1000 reviews)  
- Columns:  
  - `Review` → customer text review  
  - `Liked` → sentiment label (1 = Positive, 0 = Negative)  
- Balanced dataset → ~50% positive, ~50% negative reviews  

---

## ⚙️ Methodology
1. **Text Preprocessing**
   - Remove special characters & numbers  
   - Convert to lowercase  
   - Remove stopwords  
   - Apply stemming (PorterStemmer)  

2. **Feature Extraction**
   - Bag of Words (BoW)  
   - Term Frequency-Inverse Document Frequency (TF-IDF)  

3. **Model Training**
   - Logistic Regression  
   - Naive Bayes  
   - Support Vector Machine (SVM)  
   - Decision Tree  
   - Random Forest  
   - XGBoost  
   - LightGBM  

4. **Evaluation Metrics**
   - Accuracy  
   - Precision, Recall, F1-score  
   - ROC-AUC  
   - Confusion Matrix  

---

## 📊 Results

| Model               | Accuracy | ROC-AUC |
|----------------------|----------|---------|
| **Naive Bayes**      | **0.77** | **0.77** ✅ |
| Logistic Regression  | 0.73     | 0.74    |
| SVM                  | 0.75     | 0.75    |
| Decision Tree        | 0.71     | 0.72    |
| Random Forest        | 0.72     | 0.72    |
| XGBoost              | 0.67     | 0.67    |
| LightGBM             | 0.62     | 0.63    |

🔹 **Best Performing Model → Naive Bayes with TF-IDF (Accuracy: 77%)**  
🔹 Linear models (Naive Bayes, Logistic Regression, SVM) work best on sparse TF-IDF features.  
🔹 Tree-based models underperformed without tuning.  

---

## 💡 Business Insights
- Restaurants can **track sentiment trends** in customer reviews automatically.  
- Managers can quickly identify **negative reviews** to improve service.  
- Saves hours of manual review-reading → more **efficient operations**.  
- Extensible to other domains (e-commerce, hotel reviews, app feedback).  

---

## 🚀 Next Steps
- Hyperparameter tuning for better performance  
- Try **n-grams (bi/tri-grams)** and larger feature sets  
- Use **word embeddings (Word2Vec, GloVe, FastText)**  
- Explore **Deep Learning models (LSTM, BERT, Transformers)**  
- Build a **dashboard/streamlit app** for real-time sentiment monitoring  

---

## 🛠️ Tech Stack
- **Python** 🐍  
- **NLTK, spaCy** → preprocessing  
- **Scikit-learn, XGBoost, LightGBM** → ML models  
- **Matplotlib, Seaborn** → visualization  
- **Pandas, NumPy** → data handling  

---

## ✨ Tagline
> *"ReviewLens helps restaurants listen better by converting customer feedback into actionable insights."*  

---

## 📌 Author
👤 **Mubasshir Ahmed**  
📧 [https://www.linkedin.com/in/mubasshir3712/]  
🔗 GitHub: [mubasshirahmed-3712](https://github.com/mubasshirahmed-3712)  

---
