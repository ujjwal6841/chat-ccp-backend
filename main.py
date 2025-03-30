from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Chat-CCP Backend is Live!"}

@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    return {"filename": file.filename, "status": "Uploaded successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
