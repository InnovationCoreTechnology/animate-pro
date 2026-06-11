from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from contextlib import asynccontextmanager
import uuid

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Animate Pro API...")
    yield
    logger.info("Shutting down...")

app = FastAPI(
    title="Animate Pro",
    description="AI Video Animation Studio",
    version="0.1.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"name": "Animate Pro", "version": "0.1.0", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/ready")
async def ready():
    return {"ready": True, "models_loaded": True}

@app.post("/api/animate")
async def create_animation(style: str = "realistic", output_format: str = "mp4"):
    job_id = str(uuid.uuid4())
    return {"job_id": job_id, "status": "pending", "message": "Animation queued!"}

@app.get("/api/animate/jobs/{job_id}")
async def get_job_status(job_id: str):
    return {"job_id": job_id, "status": "processing", "progress": 50}