\# 📰 News Pulse



An AI-powered News Aggregation and Clustering platform built using \*\*FastAPI, React, MongoDB Atlas, and Scikit-learn\*\*.



News Pulse automatically collects news from multiple RSS feeds, stores the articles in MongoDB, groups similar news using Machine Learning, and displays clustered results through a modern React interface.



\---



\## 🚀 Features



\- 📰 Fetch news from multiple RSS feeds

\- 💾 Store articles in MongoDB Atlas

\- 🤖 Cluster similar news using Machine Learning (K-Means)

\- ⚡ FastAPI REST API

\- 🎨 React.js frontend

\- 🔒 Secure configuration using Environment Variables (.env)

\- 📂 Clean project structure

\- ☁️ Ready for deployment



\---



\# 🛠 Tech Stack



\### Backend

\- Python

\- FastAPI

\- PyMongo

\- MongoDB Atlas



\### Machine Learning

\- Scikit-learn

\- Pandas

\- NumPy



\### Frontend

\- React.js

\- HTML5

\- CSS3

\- JavaScript



\### Tools

\- Git

\- GitHub

\- VS Code



\---



\# 📁 Project Structure



```

News-Pulse

│

├── backend

│   ├── main.py

│   └── .env

│

├── scraper

│   ├── ingest.py

│   ├── ingest\_multiple.py

│   ├── save\_articles.py

│   ├── cluster\_articles.py

│

├── frontend

│

├── requirements.txt

│

├── .gitignore

│

└── README.md

```



\---



\# ⚙️ Installation



\## 1. Clone Repository



```bash

git clone https://github.com/Harshitgarg-github/News---Pulse.git

cd News---Pulse

```



\---



\## 2. Install Python Dependencies



```bash

pip install -r requirements.txt

```



\---



\## 3. Configure Environment Variables



Create a file named \*\*.env\*\* inside the \*\*backend\*\* folder.



```

MONGO\_URI=your\_mongodb\_connection\_string

```



\---



\## 4. Start Backend



```bash

cd backend

python -m uvicorn main:app --reload

```



Backend will run on



```

http://127.0.0.1:8000

```



\---



\## 5. Start Frontend



```bash

cd frontend

npm install

npm start

```



Frontend will run on



```

http://localhost:3000

```



\---



\# 🔌 API Endpoints



\## Home



```

GET /

```



Returns



```json

{

&#x20; "message": "News Pulse API Running"

}

```



\---



\## Get News Clusters



```

GET /clusters

```



Example Response



```json

{

&#x20; "0": \[

&#x20;   {

&#x20;     "source": "BBC",

&#x20;     "title": "Sample News",

&#x20;     "cluster\_id": 0

&#x20;   }

&#x20; ]

}

```



\---



\# 🧠 Machine Learning Workflow



```

RSS Feeds

&#x20;     │

&#x20;     ▼

Fetch Articles

&#x20;     │

&#x20;     ▼

Store in MongoDB

&#x20;     │

&#x20;     ▼

Text Vectorization

(TF-IDF)

&#x20;     │

&#x20;     ▼

K-Means Clustering

&#x20;     │

&#x20;     ▼

FastAPI

&#x20;     │

&#x20;     ▼

React Frontend

```



\---



\# 📷 Screenshots



Add screenshots after deployment.



Example:



\- Home Page

\- Clustered News

\- MongoDB Atlas

\- API Response



\---



\# 🔮 Future Improvements



\- 🔍 Search functionality

\- 📰 Category-wise filtering

\- 🌙 Dark Mode

\- 🤖 AI News Summarization

\- ❤️ Bookmark Articles

\- 👤 User Authentication

\- 📱 Mobile Responsive UI

\- 📊 News Analytics Dashboard



\---



\# 📦 Requirements



Main Libraries



\- FastAPI

\- Uvicorn

\- MongoDB

\- Scikit-learn

\- Pandas

\- NumPy

\- Feedparser

\- Python-dotenv



\---



\# 👨‍💻 Author



\*\*Harshit Garg\*\*



BCA Graduate | Aspiring Software Developer | Python | React | FastAPI | MongoDB



GitHub



https://github.com/Harshitgarg-github



\---



\# ⭐ If you like this project



Give this repository a ⭐ on GitHub.



\---



\# 📄 License



This project is created for educational and internship evaluation purposes.

