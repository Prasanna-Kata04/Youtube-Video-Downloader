
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware, # type: ignore
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

import os
import yt_dlp

cur_dir = os.getcwd()

@app.post("/download")
def download_video(link: str = Form(...)):
    # Your download logic using yt-dlp
    youtube_dl_options = {
        "format": "best",
        "outmpl": os.path.join(cur_dir, f"video{link[-11:]}.mp4")
    }
    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        ydl.download([link])
    return {"status": "Download started"}

