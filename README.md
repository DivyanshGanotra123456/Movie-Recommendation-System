# 🎬 Netflix-Style Movie Recommendation System

## 📌 About the Project

This project is a Netflix-inspired movie recommendation system built using Flask and machine learning.

The goal was simple:  
👉 Build something that actually feels like a real product, not just a notebook model.

So instead of stopping at just ML, this project includes:

- A working backend (Flask)  
- A clean Netflix-style UI  
- Real-time recommendations  
- Movie posters using an external API  

---

## 🚀 What It Does

You can get recommendations in three ways:

### 1️⃣ Movie-based (Cosine Similarity)
Type a movie → get similar movies  

### 2️⃣ User-based (SVD)
Enter a user ID → get personalized recommendations  

### 3️⃣ Hybrid (Best One 🔥)
Combines both approaches to give better results  

---

## 🧠 How It Works (Simple Explanation)

The system first creates a **user–movie matrix**.

Then it uses:

- Cosine similarity → to find similar movies  
- SVD → to learn hidden user preferences  

Finally, both are combined using a weighted approach.

---

## 💡 Why This Works Well

This approach helps in:

- Handling sparse data  
- Improving personalization  
- Giving more realistic recommendations  

---

## 🎯 Summary

This project is not just about building a model —  
it focuses on turning machine learning into a **real usable product**.
