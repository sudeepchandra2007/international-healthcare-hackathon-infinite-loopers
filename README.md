# international-healthcare-hackathon-infinite-loopers
### **🚀 README for Cancer Detection AI Web App**  
This **README** will guide you through setting up, running, and understanding the **Cancer Detection AI Web App**.  

---

## **📌 Project Overview**
**Cancer Detection AI** is a **deep learning-powered web application** designed to assist radiologists and pathologists in detecting **potential cancerous anomalies** in medical images.  
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Flask (Python)  
- **AI Model:** Google Gemini API  
- **Functionality:**
  - Upload & analyze medical images  
  - Drag & Drop support  
  - Display AI-generated results  
  - Track past analyses with timestamps  
  - Downloadable reports (coming soon)  

---

## **📦 File Structure**
```
infinite loopers cancer detection
│── api/
│   ├── gemini_api.py           # Handles AI model requests
│── webapp/
│   ├── app.py                  # Main Flask application
│   ├        # Loads and configures the AI model
│   |── static/
│      ├── styles.css              # Styling for UI
│      ├── script.js               # JavaScript for interactivity
│   |── templates/
│      ├── index.html              # Main web UI
│── .env                        # API Key storage (not committed)
│── requirements.txt            # Dependencies
│── README.md                   # Project documentation
```

---

## **🚀 Installation & Setup**
### **🔹 1. Clone the Repository**
```bash
git clone https://github.com/your-username/cancer-detection-ai.git
cd cancer-detection-ai
```

### **🔹 2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### **🔹 3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **🔹 4. Configure the API Key**
- **Create a `.env` file** inside the project folder.
- Add your **Gemini API key**:
  ```
  GEMINI_API_KEY=your-api-key-here
  ```

---

## **🚦 Running the App**
### **🔹 Run the Flask Server**
```bash
python -m webapp.app
```
The app will be available at:  
➡️ **http://127.0.0.1:5000/**  

---

## **🎯 Features**
✅ **Drag & Drop Image Upload**  
✅ **AI-Powered Cancer Analysis (Google Gemini API)**  
✅ **Cancer Probability & Type Detection**  
✅ **Past Analysis Tracking with Timestamp**  
✅ **Modern Dashboard UI**  

---

## **📌 Future Enhancements**
🔹 **Download Reports (PDF)**  
🔹 **Multi-Image Upload & Batch Processing**  
🔹 **User Authentication for Doctors**  
🔹 **Dark Mode Toggle**  

---

## **📜 License**
This project is **open-source** under the **MIT License**.  

---

## **🤝 Contributing**
Pull requests are welcome! Feel free to **fork** the project and improve it.  

---

## **💡 Credits**
**Developed by:** [Infinite Loopers] 
🚀 Powered by **Flask** & **Google Gemini API**  

---

Now, commit this **README.md** to GitHub with:  
```bash
git add README.md
git commit -m "Added README file"
git push origin main
```
Let me know if you need any **modifications or improvements**! 🚀🔥
