# 🌤 Smart Weather Forecast App

A simple and interactive Weather Forecast Web Application built using **Streamlit** and **Python**.  
This app allows users to enter a city name and get real-time weather information.

---

## 🚀 Features

- 🌍 Search weather by city name
- 🌡 Displays temperature
- 💧 Shows humidity
- 🌬 Wind speed details
- 🌥 Weather condition description
- 🔐 Secure API key using `.env` file
- 🎨 Clean and simple UI using Streamlit

---

## 🛠 Tech Stack

- Python
- Streamlit
- Requests
- python-dotenv
- OpenWeatherMap API

---

## 📂 Project Structure

```
smart-weather-forecast-app/
│
├── app.py
├── weather_service.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Yogesh-23-08-2007/smart-weather-forecast-app.git
cd smart-weather-forecast-app
```

### 2️⃣ Create virtual environment (Optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add API Key

Create a `.env` file and add:

```
OPENWEATHER_API_KEY=your_api_key_here
```

You can get your API key from:
https://openweathermap.org/api

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Then open:
```
http://localhost:8501
```

---

## 📸 Screenshot

Home page
<img width="1919" height="1014" alt="Screenshot 2026-02-22 162950" src="https://github.com/user-attachments/assets/fa1879d6-0032-4036-87e2-74a4df0d9b01" />

Weather Forecasting

<img width="1920" height="1017" alt="Screenshot 2026-02-15 141136" src="https://github.com/user-attachments/assets/57f09b04-77e4-4e92-920f-0243192115b5" />
<img width="1919" height="1014" alt="Screenshot 2026-02-22 163205" src="https://github.com/user-attachments/assets/0ecf7166-c074-4d8c-9e92-3e440194bf84" />
<img width="1919" height="1014" alt="Screenshot 2026-02-22 165550" src="https://github.com/user-attachments/assets/deb2571a-ffab-4b20-bc3f-3d1364fc241f" />

---

## 🎯 Future Improvements

- 5-day forecast feature
- Weather icons
- Location auto-detection
- Deployment on Streamlit Cloud

---

## 👨‍💻 Author

**Yogesh S**  
2nd Year CSE (AIML) Student  
Passionate about Python, AI & Full Stack Development 🚀

---

⭐ If you like this project, give it a star!
