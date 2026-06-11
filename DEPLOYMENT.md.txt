# Deployment Guide

## Local Development

\`\`\`bash
cp .env.example .env
docker-compose up -d
\`\`\`

## Cloud Storage (AWS S3)

\`\`\`bash
aws s3api create-bucket --bucket animate-pro --region us-east-1

# Update .env
STORAGE_TYPE=s3
AWS_ACCESS_KEY_ID=your_key
AWS_S3_BUCKET=animate-pro
\`\`\`

## Kubernetes

\`\`\`bash
kubectl apply -f kubernetes/namespace.yaml
\`\`\`