# Jobs.Console: a job API
A job posting console built in FastAPI


## Technology Stack:
* FastAPI
* Uvicorn (server)
* SQLAlchemy
* sqlite


## How to start the app ?
```
git clone "https://github.com/RhoNit/jobs.Console.git"
cd jobs.Console/
python -m venv new-env         #create a virtual environment
.\new-env\Scripts\activate     #activate your virtual environment (for Windows)
cd backend/
pip install -r requirements.txt
uvicorn main:app --reload      #start server
visit  localhost:8000/
```
