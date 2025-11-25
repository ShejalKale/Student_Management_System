
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text

app = FastAPI()

# Enable CORS for Angular frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your Angular app URL for security
    allow_methods=["*"],
    allow_headers=["*"],
)

connection_string = "mssql+pyodbc://shejal:Pass@123@18557sqlserver1.database.windows.net:1433/SqlDatabasedriver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(connection_string)

# Example query

@app.post("/submit")
def submit_data(name: str = Form(...), email: str = Form(...)):
    try:
        with engine.connect() as conn:
            query = text("INSERT INTO Users (Name, Email) VALUES (:name, :email)")
            conn.execute(query, {"name": name, "email": email})
        return {"status": "success", "message": "Data inserted successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/")
def home():
    return {"message": "API is running"}

