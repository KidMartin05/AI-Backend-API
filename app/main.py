from fastapi import FastAPI, UploadFile, File, HTTPException

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".txt")):
        raise HTTPException(status_code=400, detail="Only PDF and TXT files are allowed")

    contents = await file.read()

    return {
        "filename": file.filename,
        "size": len(contents),
        "message": "File received successfully"
    }