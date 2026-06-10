# 🎮 Hindi Land - Battle Royale Game

A fast-paced battle royale game inspired by Garena Free Fire, set on an India-inspired map with Indian characters, weapons, and culture.

## 📋 Project Structure

```
hindi-land-game/
├── frontend/                 # Phaser 3 game client
│   ├── src/
│   │   ├── scenes/          # Game scenes (Menu, Gameplay, GameOver, etc.)
│   │   ├── objects/         # Game objects (Player, Enemy, Weapon, etc.)
│   │   ├── systems/         # Game systems (Physics, Combat, Loot, etc.)
│   │   ├── api/             # Backend API calls
│   │   ├── config/          # Game config
│   │   ├── assets/          # Sprites, sounds, maps
│   │   ├── main.ts          # Entry point
│   │   └── types.ts         # TypeScript types
│   ├── public/              # Static assets
│   ├── dist/                # Built game
│   ├── package.json
│   ├── tsconfig.json
│   ├── webpack.config.js
│   └── index.html
├── backend/                 # Django REST API
│   ├── hindi_land/          # Django project
│   ├── api/                 # API app
│   │   ├── models.py        # Player, Match, Stats
│   │   ├── serializers.py
│   │   ├── views.py         # REST endpoints
│   │   └── urls.py
│   ├── manage.py
│   ├── requirements.txt
│   └── config.env
├── docs/                    # Game design docs
│   ├── DESIGN.md           # Game design document
│   ├── API_SPEC.md         # Backend API specification
│   ├── ASSETS.md           # Asset requirements
│   └── ROADMAP.md          # Development roadmap
├── docker-compose.yml       # Docker setup for local dev
└── .gitignore
```

## 🚀 Quick Start

### Prerequisites
- Node.js 16+
- Python 3.9+
- Git

### Setup

```bash
# Clone and enter directory
cd hindi-land-game

# Setup Frontend
cd frontend
npm install
npm run dev

# In another terminal, setup Backend
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit `http://localhost:8080` to play!

## 🎮 MVP Features (Phase 1)

- ✅ Player movement & controls
- ✅ India-inspired map (cities, villages, deserts, mountains, coast)
- ✅ Combat system (cricket bat, chappal weapons)
- ✅ Loot spawning & collection
- ✅ AI enemies with basic behavior
- ✅ Safe zone / circle mechanics
- ✅ Game over screen with stats

## 🔜 Phase 2 Features

- Multiplayer (real-time sync)
- More weapons (desi themed)
- Vehicles (auto-rickshaw, tractor)
- Crafting system (jugaad)
- Emotes (Bollywood style)
- Festivals event system
- Leaderboards
- Hindi voice lines

## 📁 Game Assets Needed

See `docs/ASSETS.md` for sprite requirements, sound files, and map designs.

## 🛠️ Development

- **Frontend Dev**: `cd frontend && npm run dev`
- **Backend Dev**: `cd backend && python manage.py runserver`
- **Linting**: `npm run lint` (frontend), `pylint api` (backend)
- **Build**: `npm run build` (frontend)

## 📚 Documentation

- [Game Design Document](docs/DESIGN.md)
- [API Specification](docs/API_SPEC.md)
- [Development Roadmap](docs/ROADMAP.md)

## 📝 License

MIT License
