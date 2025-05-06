## 1. Personal Finance Dashboard

Creating a web application that tracks expenses, visualizes spending habits, and offers financial insights.

# Personal Finance App

Full‑stack application consisting of a **Next.js 15** frontend, **FastAPI** backend and **MongoDB** database – all containerised with **Docker Compose**.

---

## ✨ What’s new?

| Date       | Change                                                                                                               |
| ---------- | -------------------------------------------------------------------------------------------------------------------- |
| 2025‑05‑06 | **Docker Compose stack** – added `docker-compose.yml` orchestrating `frontend`, `backend` and `mongo` services.      |
| 2025‑05‑06 | **Tailwind CSS** integrated into the Next.js app for modern styling (see `tailwind.config.js`, `postcss.config.js`). |
| 2025‑05‑06 | **Register page** (`pages/register.tsx`) and updated **Login → Index** routing.                                      |
| 2025‑05‑06 | Environment‑driven ports – backend reads `BACKEND_PORT`, frontend reads `PORT`, all set in Compose.                  |

---

## 📁 Project structure

```
.
├── docker-compose.yml              # Orchestrates all services
├── backend/                        # FastAPI service
│   ├── Dockerfile
│   ├── main.py
│   ├── config.py
│   └── …
├── frontend/                       # Next.js 15 + Tailwind
│   ├── Dockerfile
│   ├── pages/
│   │   ├── index.tsx   # Login (front page)
│   │   └── register.tsx
│   └── styles/globals.css
└── README.md                       # This file
```

---

## 🚀 Quick start (Docker Compose)

1. **Clone & cd** into the repo.

2. Build and start everything:

   ```bash
   docker-compose up --build
   ```

   _First run may take a few minutes while images build and npm/pip packages install._

3. Open the services:

   | Service            | URL (host)                                               | Container port |
   | ------------------ | -------------------------------------------------------- | -------------- |
   | Frontend (Next.js) | [http://localhost:3010](http://localhost:3010)           | `3010`         |
   | Backend (FastAPI)  | [http://localhost:8000/docs](http://localhost:8000/docs) | `8000`         |
   | MongoDB            | localhost:27017                                          | `27017`        |

4. Stop everything:

   ```bash
   docker-compose down -v
   ```

---

## 🛠️ Environment variables

Docker Compose passes these to the containers; change them in **`docker-compose.yml`** or a `.env` file:

```yaml
services:
  backend:
    environment:
      DB_URL: mongodb://mongo:27017
      DB_NAME: mydatabase
      BACKEND_PORT: 8000
  frontend:
    environment:
      PORT: 3010
      NEXT_PUBLIC_API_URL: http://backend:8000
```

---

## 🖥️ Local development (without Docker)

```bash
# Frontend
cd frontend
npm install
npm run dev       # listens on PORT (default 3000)

# Backend
cd ../backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

If you’re on **Node ≥ 22** and see `npx tailwindcss init` errors, install Tailwind first:

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

---

## 🤝 Contributing

- Fork & clone
- Create a feature branch
- Open a PR – be sure `docker-compose up` passes and linting (`npm run lint`) is clean.

---

## 📜 License

MIT
