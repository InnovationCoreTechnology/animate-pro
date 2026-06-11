# Animate Pro - AI Video Animation Studio

Transform images & audio into animated videos with AI

## MVP Features

✅ Image-to-Video Animation
✅ Voice Lip-Sync  
✅ Dance Motion Transfer
✅ Cartoon & Realistic Modes
✅ Fast MP4 Export
✅ AWS S3 Cloud Storage
✅ Mobile Ready PWA

## Quick Start

\`\`\`bash
git clone https://github.com/YOUR_USERNAME/animate-pro.git
cd animate-pro
cp .env.example .env
docker-compose up -d
\`\`\`

Access: http://localhost:3000 | API: http://localhost:8000

## Tech Stack

- **Frontend**: Next.js 14 + TailwindCSS
- **Backend**: FastAPI + Python
- **AI/ML**: MediaPipe, Wav2Lip, OpenCV, FFmpeg
- **Infrastructure**: Docker, Kubernetes, AWS S3
- **Queue**: Redis

## Deployment

**Docker**: `docker-compose up -d`

See `DEPLOYMENT.md` for Kubernetes setup.

## License

MIT