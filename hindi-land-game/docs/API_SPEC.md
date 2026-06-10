# 🎮 Hindi Land - API Specification

## Base URL
```
http://localhost:8000/api/
https://api.hindiland.com/api/
```

## Authentication

### JWT Token-Based Auth

**Endpoints**:
- `POST /auth/token/` - Get access & refresh tokens
- `POST /auth/token/refresh/` - Refresh access token

**Request**:
```json
{
  "username": "player_name",
  "password": "secure_password"
}
```

**Response**:
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Headers** (all protected routes):
```
Authorization: Bearer <access_token>
```

---

## Player Endpoints

### GET `/players/me/`
Get current player's profile

**Response**:
```json
{
  "id": 1,
  "user": {
    "id": 1,
    "username": "farmer_joe",
    "email": "joe@example.com"
  },
  "character_type": "farmer",
  "level": 5,
  "experience": 1200,
  "total_kills": 45,
  "total_deaths": 12,
  "total_matches": 20,
  "win_count": 3,
  "kill_death_ratio": 3.75,
  "win_rate": 15.0,
  "highest_kill_streak": 8,
  "total_damage_dealt": 3500,
  "created_at": "2026-05-01T10:30:00Z",
  "updated_at": "2026-05-10T14:22:00Z"
}
```

### POST `/players/create_profile/`
Create a new player profile

**Request**:
```json
{
  "character_type": "student"
}
```

**Response**: 201 Created
```json
{
  "id": 2,
  "user": {...},
  "character_type": "student",
  ...
}
```

### GET `/players/{id}/stats/`
Get specific player's statistics

**Response**:
```json
{
  "id": 1,
  "username": "farmer_joe",
  "total_kills": 45,
  "total_deaths": 12,
  "total_matches": 20,
  "win_count": 3,
  "kill_death_ratio": 3.75,
  "win_rate": 15.0
}
```

### GET `/players/{id}/matches_history/`
Get player's recent match history (last 20 matches)

**Response**:
```json
[
  {
    "match_id": 101,
    "placement": 1,
    "kills": 5,
    "damage_dealt": 450,
    "joined_at": "2026-05-10T14:00:00Z"
  },
  {
    "match_id": 100,
    "placement": 5,
    "kills": 2,
    "damage_dealt": 200,
    "joined_at": "2026-05-10T13:15:00Z"
  }
]
```

---

## Match Endpoints

### POST `/matches/create_match/`
Create a new match (admin/server only)

**Request**:
```json
{
  "game_mode": "solo"
}
```

**Response**: 201 Created
```json
{
  "id": 101,
  "game_mode": "solo",
  "status": "waiting",
  "max_players": 100,
  "current_players": 0,
  "duration": 900,
  "started_at": null,
  "ended_at": null,
  "winner": null,
  "players": [],
  "created_at": "2026-05-10T14:30:00Z"
}
```

### GET `/matches/{id}/`
Get match details

**Response**:
```json
{
  "id": 101,
  "game_mode": "solo",
  "status": "active",
  "max_players": 100,
  "current_players": 87,
  "duration": 900,
  "started_at": "2026-05-10T14:35:00Z",
  "ended_at": null,
  "winner": null,
  "players": [
    {
      "id": 1001,
      "player": { "id": 1, "username": "farmer_joe" },
      "kills": 5,
      "deaths": 0,
      "damage_dealt": 450,
      "damage_taken": 120,
      "placed_at": null,
      "elimination_time": null
    }
  ],
  "created_at": "2026-05-10T14:30:00Z"
}
```

### POST `/matches/{id}/join/`
Join an active match (max players limit applies)

**Response**: 200 OK
```json
{
  "id": 101,
  "game_mode": "solo",
  "status": "waiting",
  "current_players": 1,
  ...
}
```

### POST `/matches/{id}/start/`
Start the match (admin/server only)

**Response**:
```json
{
  "id": 101,
  "status": "active",
  "started_at": "2026-05-10T14:35:00Z",
  ...
}
```

### POST `/matches/{id}/end/`
End the match and record results

**Request**:
```json
{
  "winner_id": 1,
  "results": [
    {
      "player_id": 1,
      "placement": 1,
      "kills": 12,
      "damage_dealt": 2500,
      "damage_taken": 340,
      "elimination_time": 900
    }
  ]
}
```

**Response**:
```json
{
  "id": 101,
  "status": "ended",
  "ended_at": "2026-05-10T15:15:00Z",
  "winner": { "id": 1, "username": "farmer_joe" },
  ...
}
```

### GET `/matches/{id}/leaderboard/`
Get match leaderboard

**Response**:
```json
[
  {
    "rank": 1,
    "player": "farmer_joe",
    "kills": 12,
    "damage_dealt": 2500,
    "placement": 1
  },
  {
    "rank": 2,
    "player": "student_ram",
    "kills": 8,
    "damage_dealt": 1800,
    "placement": 2
  }
]
```

---

## Leaderboard Endpoints

### GET `/leaderboard/`
Get global leaderboard (top 100 by kills)

**Query Parameters**:
- `page`: Page number (default: 1)
- `limit`: Results per page (default: 10)

**Response**:
```json
[
  {
    "rank": 1,
    "user_username": "legendary_player",
    "total_kills": 500,
    "total_deaths": 80,
    "win_count": 50,
    "total_matches": 200,
    "kill_death_ratio": 6.25,
    "win_rate": 25.0
  }
]
```

### GET `/leaderboard/by_kills/`
Get top 50 players by kills

**Response**: Same as global leaderboard

### GET `/leaderboard/by_wins/`
Get top 50 players by win count

**Response**: Same as global leaderboard

### GET `/leaderboard/by_wins_rate/`
Get top 50 players by win rate (min 10 matches)

**Response**: Same as global leaderboard

---

## Health Check

### GET `/health/`
Check API status

**Response**: 200 OK
```json
{
  "status": "healthy",
  "timestamp": "2026-05-10T14:30:00Z"
}
```

---

## Error Responses

### 400 Bad Request
```json
{
  "error": "Invalid request data"
}
```

### 401 Unauthorized
```json
{
  "error": "Authentication required"
}
```

### 404 Not Found
```json
{
  "error": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal server error"
}
```

---

## Rate Limiting (Phase 2)

- Standard: 100 requests/minute
- Authenticated: 1000 requests/minute
- Match creation: 10 requests/minute

---

## WebSocket Events (Phase 2 - Real-time Multiplayer)

### Connection
```
ws://localhost:8000/ws/match/{match_id}/
```

### Events
- `player_joined`: New player joined match
- `player_moved`: Player position update
- `player_shot`: Gunshot event
- `player_hit`: Damage event
- `player_died`: Elimination event
- `circle_shrink`: Safe zone shrinks
- `match_ended`: Match concluded

---

**API Version**: 1.0  
**Last Updated**: May 2026
