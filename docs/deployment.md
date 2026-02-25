# Deployment Guide (Docker + VPS)

## Provision VPS
- Ubuntu 22.04+
- 2+ vCPU, 4-8 GB RAM (CPU embedding baseline)
- Open ports: `22`, `80`, `443`

## Install runtime
```bash
sudo apt update
sudo apt install -y docker.io docker-compose-plugin nginx certbot python3-certbot-nginx
sudo usermod -aG docker $USER
```

## Deploy app
```bash
git clone <repo-url>
cd AI-Career-Assistant-for-Freshers_MVP
cp backend/.env.example backend/.env
cp frontend/.env.local.example frontend/.env.local
docker compose -f infra/docker-compose.yml up -d --build
```

## Reverse proxy
- Route `api.yourdomain.com` -> `localhost:8000`
- Route `app.yourdomain.com` -> `localhost:3000`
- Enable TLS with certbot:
```bash
sudo certbot --nginx -d api.yourdomain.com -d app.yourdomain.com
```

## Production hardening
- Move secrets to secure secret manager.
- Add DB backups and healthchecks.
- Add observability (Prometheus + Grafana + OpenTelemetry).
- Pin model files in container image for cold-start reliability.
