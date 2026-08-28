\# RecoverX – Recovery Prediction \& Analytics System



RecoverX is a machine-learning-based recovery prediction system designed to predict the likelihood of successful recovery and provide useful recovery analytics.



\## Project Features



\- Machine learning recovery prediction

\- Recovery probability prediction

\- Recovery level classification

\- Recommended follow-up action

\- Interactive analytics dashboard

\- Django REST-style prediction API

\- Dashboard statistics API

\- 50,000-case recovery dataset

\- Responsive frontend



\## Project Structure



RecoverX\_FINAL\_SUBMISSION/



├── backend/

│   └── recoverx\_backend/

├── data/

│   └── recovery\_data.csv

├── frontend/

│   ├── dashboard.html

│   ├── index.html

│   └── script.js

├── ml/

│   ├── generate\_dataset.py

│   ├── predict.py

│   ├── recovery\_model.pkl

│   └── train\_model.py

├── notebooks/

└── requirements.txt



\## Requirements



\- Python 3.12 or compatible Python version

\- Django

\- Python virtual environment

\- Required Python packages listed in requirements.txt



\## Installation



Open PowerShell in the project directory.



Create a virtual environment:



&#x20;   python -m venv venv



Activate it:



&#x20;   .\\venv\\Scripts\\Activate.ps1



Install dependencies:



&#x20;   pip install -r requirements.txt



\## Start the Backend



Go to:



&#x20;   backend\\recoverx\_backend



Run:



&#x20;   python manage.py runserver



The backend will run at:



&#x20;   http://127.0.0.1:8000/



\## Start the Frontend



Open another PowerShell window.



Go to:



&#x20;   frontend



Run:



&#x20;   python -m http.server 5500 --bind 127.0.0.1



The frontend will run at:



&#x20;   http://127.0.0.1:5500/



\## Open RecoverX



Prediction page:



&#x20;   http://127.0.0.1:5500/index.html



Dashboard:



&#x20;   http://127.0.0.1:5500/dashboard.html



\## API Endpoints



Backend home:



&#x20;   GET http://127.0.0.1:8000/



Prediction API:



&#x20;   POST http://127.0.0.1:8000/api/predict/



Dashboard API:



&#x20;   GET http://127.0.0.1:8000/api/dashboard/



\## Dashboard Statistics



The current dataset contains:



\- Total Cases: 50,000

\- Recovered: 12,798

\- Not Recovered: 37,202

\- Recovery Rate: 25.6%

\- Average Amount Due: 4100.53

\- Average Days Overdue: 90.67

\- Average Recovery Days: 15.49



\## Machine Learning



The trained model is stored in:



&#x20;   ml/recovery\_model.pkl



The prediction logic is implemented in:



&#x20;   ml/predict.py



The training script is:



&#x20;   ml/train\_model.py



The dataset generation script is:



&#x20;   ml/generate\_dataset.py



\## Typical Prediction Output



A successful prediction returns information such as:



\- Recovery Probability

\- Prediction

\- Recovery Level

\- Recommended Action



Example:



&#x20;   Recovery Probability: 95.5%

&#x20;   Prediction: RECOVERY LIKELY

&#x20;   Recovery Level: HIGH

&#x20;   Recommended Action: High Priority Follow-up



\## Important



The Django server and frontend server must both be running when using the complete RecoverX application.



This project is intended for educational/project demonstration purposes.

