# 👗 StyleSync Inventory Intelligence

## 🚀 Overview

StyleSync Inventory Intelligence is an AI-driven solution designed specifically for fashion retailers and inventory management systems. Leveraging Crew AI, this project analyzes inventory data to provide real-time insights, demand forecasting, and actionable recommendations to optimize stock levels and boost sales performance while minimizing deadstock.

The system retrieves data from **Google Trends** and **Google Events** using **SerpAPI**, enhancing trend analysis and enabling better forecasting of customer demand. It uses Custom Tools to do the same.

## ✨ Features

- 📊 **Inventory Analysis**: Monitor inventory levels and track product performance.
- 🔥 **Actionable Insights**: Receive recommendations for restocking, promotions, and markdowns.
- 📈 **Trend Analysis**: Understand evolving trends in product styles and consumer preferences.
- 🔍 **Google Trends & Events Integration**: Uses SerpAPI to fetch relevant fashion trends and event data.
- 🤖 **Crew AI Integration**: Utilizes Crew AI for advanced data processing and analytics.
- ♻️ **Deadstock Minimization**: Helps identify slow-moving stock and suggest strategies to reduce deadstock.

## 🛠 Tech Stack

- **Backend**: Python
- **AI Orchestration**: Crew AI
- **Data Processing**: Pandas, NumPy
- **LLM Model**: Groq's DeepSeek Distilled
- **APIs Used**: SerpAPI, Groq API, Serper API, Weather API

## 🔧 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/krishshah9944/StyleSync-Inventory-Intelligence.git
cd StyleSync-Inventory-Intelligence
```

### 2️⃣ Create a Virtual Environment

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables

Create a `.env` file in the root directory and add your API keys:

```bash
GROQ_API_KEY=your_groq_api_key_here
SERP_API_KEY=your_serp_api_key_here
SERPER_API_KEY=your_serper_api_key_here
WEATHER_API_KEY=your_weather_api_key_here
```

### 5️⃣ Navigate to the `inv` Directory

```bash
cd inv
```

### 6️⃣ Export Path and Run the Application

Before running the application, export the correct path:

```bash
export PYTHONPATH=$(pwd)/src
```

Then, execute the main script:

```bash
python main.py
```

## 📌 Usage

- 📥 **Provide Inventory Data**: Upload your inventory data via a CSV file.
- 🛠 **Run Analysis**: The system processes data and provides insights using Crew AI.
- 📊 **Review Recommendations**: Get actionable recommendations for inventory management and deadstock reduction.

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests for improvements and bug fixes.

## 📧 Contact

For inquiries, please reach out via:

- **LinkedIn**: [Krish Shah](https://www.linkedin.com/in/krishshah9944/)
- **Email**: [krishshah9944@gmail.com](mailto\:krishshah9944@gmail.com)

