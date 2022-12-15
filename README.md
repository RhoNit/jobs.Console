# Jobs.Console: a job API
A job posting console built in FastAPI


## Technology Stack:
* FastAPI
* Uvicorn (server)
* SQLAlchemy
* sqlite


## 🛠 Installation

### Clone this repo
```
git clone "https://github.com/RhoNit/jobs.Console.git"
```

<hr>

### Navigate to the ```/backend``` sub-directory
```
cd jobs.Console/
python -m venv new-env         #create a virtual environment
.\new-env\Scripts\activate     #activate your virtual environment (for Windows)
cd backend/

<hr>

### Install all dependencies mentioned inside ```requirements.txt``` file
```
pip install -r requirements.txt
```

<hr>

### Run the application
```
uvicorn main:app --reload
```

<hr> 

### Visit ```localhost:8000```
```
http://127.0.0.1:8000
```
<hr>

### API Documentation and test APIs on
```
http://127.0.0.1:8000/docs
```


