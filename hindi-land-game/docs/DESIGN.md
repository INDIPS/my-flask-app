# 🎮 Hindi Land - Design Document

## Game Overview

**Hindi Land** is a fast-paced 2D top-down battle royale game inspired by Garena Free Fire. The game is set on an India-inspired map featuring iconic Indian locations, characters, weapons, and cultural elements.

## Core Gameplay Loop

1. **Drop & Land**: Players start in a plane and choose where to land on the map
2. **Loot & Explore**: Find weapons, armor, and health items across various locations
3. **Combat**: Encounter enemies and NPCs, engage in tactical combat
4. **Survive**: Stay within the shrinking safe zone
5. **Victory**: Be the last player alive to win

## Map Design

### Locations (Based on Real Indian Places)

| Location | Type | Features | Strategic Value |
|----------|------|----------|-----------------|
| **Delhi** | City | Urban terrain, multiple buildings | High loot density |
| **Mumbai** | City | Coastal city, tall buildings | Medium-high loot |
| **Bangalore** | City | Tech hub, modern buildings | Medium loot |
| **Rajpur Village** | Village | Small houses, farms | Lower loot, safe early |
| **Goan Village** | Village | Beach houses, coconut trees | Moderate loot |
| **Thar Desert** | Desert | Open terrain, minimal cover | Low loot, high visibility |
| **Himalayas** | Mountain | Elevated terrain, caves | Strategic positioning |
| **Goa Beach** | Coast | Sandy beach, palm trees | Unique loot variety |
| **Punjab Farms** | Farmland | Agricultural fields, barns | Hidden items |

**Map Size**: 2560 x 1920 pixels (approximately 4:3 aspect ratio)

## Characters

### Available Skins

- **Farmer** 👨‍🌾 - Rural worker, traditional attire
- **Student** 👨‍🎓 - Modern youth, casual clothes
- **Worker** 👷 - Construction worker, heavy attire
- **Vendor** 🏪 - Street vendor, traditional outfit
- **Teacher** 👨‍🏫 - Educated professional, formal clothes

Each character has unique skins and voice lines in Hindi.

## Weapons System

### Melee Weapons
- **Cricket Bat**: Damage 25, Quick attacks
- **Chappal** (Slipper): Damage 10, Comedic effect
- **Lathi** (Stick): Damage 35, Longer range

### Ranged Weapons
- **Revolver**: Damage 45, 6 bullets, fire rate 0.6s
- **Rifle**: Damage 60, 30 bullets, fire rate 0.1s
- **Shotgun**: Damage 80, 8 bullets, close range

### Special Weapons (Phase 2)
- Bow & Arrow
- Throwing knives
- Molotov cocktails

## Items & Loot

### Health Items
- **Medical Kit**: Restores 50 health
- **Health Potion**: Restores 25 health
- **Bandage**: Restores 10 health

### Protective Gear
- **Shield Potion**: Adds 50 shield
- **Armor Vest**: Adds 75 armor
- **Helmet**: Reduces headshot damage by 50%

### Ammo & Resources
- **Ammo Box**: Restores 30 bullets
- **Components**: Used for crafting (Phase 2)

## Safe Zone Mechanics

### Circle System
1. **Phase 1**: 2 minutes before circle starts shrinking
2. **Phase 2-5**: Each circle shrinks by 30% radius, damage increases per phase
3. **Final Circle**: Last 100m radius, high damage

### Damage Outside Zone
- Phase 1: 0.5 HP/second
- Phase 2: 1 HP/second
- Phase 3: 2 HP/second
- Phase 4: 3 HP/second
- Phase 5: 5 HP/second

## Combat System

### Player Stats
- **Health**: 100 HP
- **Shield**: Max 100
- **Armor**: Max 100 (reduces damage by 30-50%)
- **Movement Speed**: 150-300 pixels/second

### Combat Flow
1. Spot enemy
2. Take aim (crosshair appears)
3. Fire weapon
4. Track damage dealt
5. Loot defeated enemy

## Victory Conditions

### Solo Mode
- Last player alive wins

### Duo Mode (Phase 2)
- Last team of 2 alive wins
- Both teammates must be alive

### Squad Mode (Phase 2)
- Last team of 4 alive wins
- Team can win even with 1 survivor

## MVP Features (Phase 1)

✅ Core gameplay loop
✅ Map with 8 locations
✅ 5 character skins
✅ 5 weapons
✅ Loot system
✅ AI enemies with basic behavior
✅ Safe zone with shrinking mechanic
✅ Health & armor system
✅ Game over screen with stats
✅ Basic UI (health, kills, time, players alive)

## Phase 2 Features

- Multiplayer networking (WebSocket/Firebase)
- Vehicles (auto-rickshaw, tractor, bike)
- Crafting system (Jugaad)
- Emotes (Bollywood dance, namaste, etc.)
- Festival events
- Voice chat integration
- Enhanced graphics & animations
- Leaderboards & ranks
- Battle pass system

## Phase 3 Features

- Mobile app (React Native)
- Advanced map regions
- Boss encounters
- Dynamic weather
- Day/Night cycle
- Pets & companions
- Social features (friends, clans)
- E-sports tournaments

## Art Style

- **2D Top-Down View**: Isometric or birds-eye perspective
- **Pixel Art / Low-Poly**: Retro-modern aesthetic
- **Indian Cultural Elements**: Colors (saffron, green, white), patterns, temples
- **Character Design**: Diverse, culturally authentic, varied body types
- **Environment**: Realistic Indian architecture mixed with game aesthetics

## Sound Design

### Audio Elements
- Hindi voice lines for characters
- Bollywood-inspired background music
- SFX: gunshots, footsteps, explosions
- UI: click sounds, notifications

### Voice Lines (Phase 1)
- Character selection: "Chaliye shuru karein!" (Let's start!)
- Taking damage: "Arre!" / "Yeh kya?"
- Victory: "Jai! Main jeeta!" (I won!)
- Death: "Hai Ram!" / "Yeh toh..." (exclamations)

## Performance Targets

- **FPS**: 60 FPS on desktop, 30+ on mobile (Phase 2)
- **Load Time**: < 5 seconds on 4G
- **Network Latency**: < 100ms for multiplayer
- **File Size**: < 50MB (web), < 200MB (mobile)

## Monetization (Future)

- Battle Pass ($4.99/season)
- Character skins ($2.99-$9.99)
- Weapon skins ($1.99-$4.99)
- Emote packs ($2.99)
- Battle Pass bundles (cosmetics + rewards)

**No Pay-to-Win**: All items are cosmetic or earned through gameplay.

---

**Document Version**: 1.0  
**Last Updated**: May 2026  
**Status**: Active Development
