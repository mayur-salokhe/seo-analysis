# **📌 SEO Performance Analysis Dashboard**  

🚀 **Track & Analyze Google Search Rankings using SerpAPI**  

---

## **📖 Overview**  
This project is an **SEO Performance Analysis Dashboard** that helps **track keyword rankings, analyze competitors, and monitor ranking trends** using **SerpAPI**. It is built with **Streamlit, SQLite, and Plotly** for interactive data visualization.  

---

## **✨ Features & Why They Were Added**  

### **1️⃣ Google SERP Scraping (SerpAPI)**
**📌 Feature:** Fetches **top search results** for a keyword from Google.  
**🤔 Why?** To **track keyword rankings** and analyze **which domains consistently rank high**.  

---

### **2️⃣ Monthly Search Quota Management (100 Searches/Month)**
**📌 Feature:** Keeps track of **remaining API searches per month**.  
**🤔 Why?** SerpAPI has a **100 searches/month limit**, so we **warn users** when they are about to run out.  

---

### **3️⃣ Keyword Ranking Trends**
**📌 Feature:** Displays ranking **fluctuations over time** with line charts.  
**🤔 Why?** Helps **monitor SEO performance** and see if rankings **improve or decline**.  

---

### **4️⃣ Competitor Analysis**
**📌 Feature:** Tracks **which domains appear most frequently** in top search results.  
**🤔 Why?** Allows users to **identify strong competitors** and analyze their SEO strategies.  

---

### **5️⃣ Featured Snippet Tracking**
**📌 Feature:** Detects if a result has a **featured snippet** (position 0 on Google).  
**🤔 Why?** Featured snippets get **higher click-through rates**, so tracking them helps **optimize content**.  

---

### **6️⃣ Rank Change Analysis**
**📌 Feature:** Compares **current vs. previous rankings** to see if a keyword **gained or lost** positions.  
**🤔 Why?** SEO is dynamic—this feature helps **track progress & adapt strategies**.  

---

### **7️⃣ Logging for API Errors**
**📌 Feature:** Logs API failures to a **logs/serpapi_errors.log** file.  
**🤔 Why?** Helps **debug issues** when API calls fail, ensuring **smooth operation**.  

---

## **🛠️ Tech Stack**
- **Python** 🐍 (Main Backend)
- **Streamlit** 📊 (Interactive Dashboard)
- **SerpAPI** 🔍 (Google Search Scraping)
- **SQLite** 🗄️ (Historical Data Storage)
- **Pandas** 📉 (Data Processing)
- **Plotly** 📈 (Data Visualization)
- **Logging** 📜 (Error Tracking)

---

## **📂 Project Structure**
```
📦 SEO_Analysis
│-- 📜 app.py                 # Streamlit dashboard
│-- 📜 serpapi_scraper.py      # Fetches SERP data using SerpAPI
│-- 📜 database.py             # Handles SQLite database
│-- 📜 config.py               # Stores API keys (loaded from .env)
│-- 📜 requirements.txt        # Python dependencies
│-- 📜 README.md               # Project documentation
│-- 📂 logs/                   # Stores error logs
│-- 📂 data/                   # (Optional) Stores exported data
```

---

## **🚀 Installation & Setup**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/your-repo/seo-analysis.git
cd seo-analysis
```

### **2️⃣ Create a Virtual Environment**  
```bash
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate     # Windows
```

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**  
Create a **.env** file in the root directory and add:  
```
SERPAPI_KEY=your_serpapi_key_here
SERPAPI_URL=https://serpapi.com/search
```

### **5️⃣ Run the Dashboard**  
```bash
streamlit run app.py
```

---

## **📌 How to Use**
1️⃣ **Enter a keyword** in the search box  
2️⃣ Click **"Fetch SERP Data"** to get rankings  
3️⃣ View **ranking trends, competitor insights, & snippets**  
4️⃣ Monitor **rank changes over time**  

---

## **💡 Future Improvements**
🔹 **Automated daily/weekly keyword tracking**  
🔹 **Backlink analysis & domain authority tracking**  
🔹 **Google Search Console integration**  

---

🎯 **This tool helps SEO analysts & marketers track keyword performance efficiently!** 🚀  
🙌 **Feel free to contribute or suggest improvements!**