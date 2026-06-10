# 🎮 Hindi Land - Quick Setup Guide

## Prerequisites

Ensure you have installed:
- **Node.js** (v16+) - [Download](https://nodejs.org/)
- **Python** (v3.9+) - [Download](https://www.python.org/)
- **Git** - [Download](https://git-scm.com/)
- **Docker** (optional, for containerized setup) - [Download](https://www.docker.com/)

---

## 🚀 Local Development Setup (Non-Docker)

### Step 1: Clone Repository
```bash
cd d:\CODING
git clone https://github.com/INDIPS/hindi-land-game.git
cd hindi-land-game
```

### Step 2: Setup Backend

```bash
# Navigate to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cat > .env << EOF
DEBUG=True
SECRET_KEY=dev-key-change-in-production
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:8080
EOF

# Run migrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser
# Username: admin
# Email: admin@example.com
# Password: (enter a secure password)

# Start backend server
python manage.py runserver
```

Backend runs at: `http://localhost:8000`
Admin panel: `http://localhost:8000/admin`

---

### Step 3: Setup Frontend (in a new terminal)

```bash
# From project root
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend runs at: `http://localhost:8080`

---

## 🐳 Docker Setup (Optional - All-in-One)

```bash
# From project root
docker-compose up -d

# Wait for services to start (~30 seconds)
# Check logs
docker-compose logs -f

# Create superuser (in another terminal)
docker-compose exec django python manage.py createsuperuser

# Stop services
docker-compose down
```

**Access URLs**:
- Frontend: `http://localhost:8080`
- Backend: `http://localhost:8000`
- API Docs: `http://localhost:8000/api/docs/`
- Admin: `http://localhost:8000/admin`

---

## 🎮 Playing the Game

1. Visit `http://localhost:8080` in your browser
2. Click **"PLAY"** button
3. Use **WASD** or **Arrow Keys** to move
4. Click to aim/shoot
5. Collect loot to survive
6. Stay in the safe zone (green circle)
7. Last player alive wins!

---

## 📊 API Testing

### Using cURL

```bash
# Health check
curl http://localhost:8000/api/health/

# Get admin token
curl -X POST http://localhost:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"your_password"}'

# Using the token
curl -H "Authorization: Bearer <token>" http://localhost:8000/api/players/me/
```

### Using Postman
Import the Postman collection from: `docs/postman_collection.json` (to be created)

---

## 🛠️ Development Commands

### Frontend
```bash
cd frontend

# Development server
npm run dev

# Build for production
npm run build

# Linting
npm run lint

# Type checking
npm run type-check
```

### Backend
```bash
cd backend

# Run server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Run tests
python manage.py test

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run Pylint
pylint api
```

---

## 📝 Environment Variables

### Backend (.env)
```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:8080
JWT_LIFETIME=3600
```

### Frontend (.env)
```env
REACT_APP_API_URL=http://localhost:8000/api
REACT_APP_ENV=development
```

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Find process using port 8000
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill process
kill -9 <PID>  # macOS/Linux
taskkill /PID <PID> /F  # Windows
```

### CORS Errors
- Ensure `CORS_ALLOWED_ORIGINS` in backend .env includes frontend URL
- Restart backend after changing .env

### Module Not Found
```bash
# Backend
pip install -r requirements.txt

# Frontend
npm install
npm install -D @types/phaser phaser
```

### Database Issues
```bash
# Backend
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

---

## 📚 Documentation

- [Game Design Document](docs/DESIGN.md)
- [API Specification](docs/API_SPEC.md)
- [Asset Requirements](docs/ASSETS.md)
- [Development Roadmap](docs/ROADMAP.md)

---

## 🤝 Contributing

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Commit changes: `git commit -am 'Add feature'`
3. Push to branch: `git push origin feature/your-feature`
4. Open a pull request

---

## 📞 Support

For issues or questions:
- 📧 Email: support@hindiland.com
- 💬 Discord: [Join our community](https://discord.gg/hindiland)
- 🐛 Issues: [GitHub Issues](https://github.com/INDIPS/hindi-land-game/issues)

---

**Happy Gaming! 🎮🎉**
