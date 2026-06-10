# 🎮 Hindi Land - Asset Requirements

## Character Sprites

### Character Types
Each character type needs the following sprite variations:

**Resolution**: 64x64 pixels (or 128x128 for higher quality)
**Format**: PNG with transparency

#### 1. Farmer 👨‍🌾
- **Idle**: 4 frames (4x64 or 8x64)
- **Walk**: 8 frames (8x64)
- **Run**: 8 frames (8x64)
- **Attack**: 6 frames (6x64)
- **Hit**: 2 frames (2x64)
- **Death**: 4 frames (4x64)

#### 2. Student 👨‍🎓
- Same animation set as Farmer

#### 3. Worker 👷
- Same animation set as Farmer

#### 4. Vendor 🏪
- Same animation set as Farmer

#### 5. Teacher 👨‍🏫
- Same animation set as Farmer

---

## Weapon Sprites

**Resolution**: 32x32 pixels
**Format**: PNG with transparency

### Melee Weapons
- Cricket Bat (brown/red handle)
- Chappal/Slipper (orange/pink slipper)
- Lathi (wooden stick, brown)

### Ranged Weapons
- Revolver (metallic, compact)
- Rifle (long barrel, tactical)
- Shotgun (double-barrel)

---

## Loot Item Sprites

**Resolution**: 24x24 pixels
**Format**: PNG with transparency

### Health Items
- Medical Kit (red cross box)
- Health Potion (blue/green bottle)
- Bandage (wrapped cloth)

### Protective Gear
- Shield Potion (golden shield)
- Armor Vest (tactical vest)
- Helmet (hard hat/military helmet)

### Ammo
- Ammo Box (brown wooden box)
- Bullet Stack (stacked bullets)

---

## Environment Tiles

**Resolution**: 32x32 pixels (tileset)
**Format**: PNG with transparency

### Terrain Types
- **City**: Asphalt roads, concrete, buildings
- **Village**: Dirt paths, wooden structures
- **Desert**: Sand, rocks, minimal vegetation
- **Mountain**: Rock faces, snow, trees
- **Coast**: Sand beach, water, rocks
- **Farmland**: Tilled earth, crops, fences

### Building Components
- House walls (brick, concrete)
- Roofs (red tiles, flat metal)
- Windows & doors
- Fences & walls
- Trees & vegetation

---

## UI Elements

**Resolution**: Variable
**Format**: PNG/SVG

### HUD Elements
- Crosshair (simple + or custom design)
- Health bar (green gradient)
- Armor bar (blue gradient)
- Ammo counter background
- Minimap frame (small square)

### Menu Elements
- Buttons (play, settings, stats, exit)
- Panels (character select, loading)
- Icons (settings gear, stats chart)

### Icons
- Weapon icons (16x16)
- Item icons (24x24)
- Status icons (health, armor, low health warning)

---

## Background Music

### Main Menu
- File: `menu_background.mp3`
- Duration: 2-3 minutes (loopable)
- Mood: Upbeat, Indian classical fusion
- BPM: 120-140

### Gameplay
- File: `gameplay_background.mp3`
- Duration: 3-4 minutes (loopable)
- Mood: Intense, action-oriented
- BPM: 140-160

### Safe Zone Warning
- File: `safe_zone_warning.mp3`
- Duration: 30 seconds
- Mood: Urgent, alarm-like

### Victory Theme
- File: `victory_theme.mp3`
- Duration: 10-15 seconds
- Mood: Triumphant, celebratory

---

## Sound Effects

### Weapon Sounds
- `cricket_bat_swing.wav` (melee impact)
- `chappal_hit.wav` (comedic slap)
- `revolver_shot.wav` (pistol gunshot)
- `rifle_shot.wav` (rifle gunshot)
- `reload.wav` (magazine reload)

### Player Sounds
- `footstep_concrete.wav` (walking on hard surface)
- `footstep_dirt.wav` (walking on soil)
- `jump.wav` (player jump/dodge)
- `pain_grunt_male.wav` (taking damage)
- `pain_grunt_female.wav` (taking damage - female)
- `death_scream.wav` (elimination)

### Environment Sounds
- `door_open.wav` (opening building)
- `looting.wav` (picking up item)
- `circle_warning.wav` (safe zone shrinking)
- `helicopter_loop.wav` (match start)

### UI Sounds
- `button_click.wav` (UI interaction)
- `notification_ding.wav` (match notification)
- `kill_streak_sound.wav` (milestone achievement)

---

## Voice Lines (Hindi)

### Character Selection
- "Chaliye shuru karein!" (Let's start!)
- "Tayyar hoon main!" (I'm ready!)

### Taking Damage
- "Arre!" (exclamation)
- "Yeh toh dard hua!" (That hurt!)

### Eliminating Enemy
- "Ek aur mara!" (One more down!)
- "Badhaiya!" (Great!)

### Victory
- "Jai! Main jeeta!" (I won!)
- "Number 1 champion!" (English mix)

### Death
- "Hai Ram!" (Oh God!)
- "Yeh toh nahi sakte!" (Can't be!)

---

## Map Tilemap

### File Format
- **Tiled Map Editor** (.tmx)
- **Resolution**: 2560 x 1920 pixels
- **Tile Size**: 32x32 pixels
- **Layers**:
  1. Terrain (base ground)
  2. Buildings/Obstacles
  3. Decorations (trees, plants)
  4. Spawn Points (invisible markers)
  5. Loot Zones (invisible markers)

---

## Animations

### Character Animations
- **Idle**: Subtle breathing, blinking
- **Walk**: Natural gait (4-6 frames)
- **Run**: Faster gait (8 frames)
- **Attack**: Weapon-specific (5-8 frames)
- **Hit**: Knockback effect (2-3 frames)
- **Death**: Collapse animation (4-6 frames)

### Object Animations
- **Weapon Pickup**: Bounce effect
- **Loot Box**: Pulse/glow effect
- **Vehicle**: Idle animation

---

## Particle Effects

### Combat Effects
- **Bullet Impact**: Dust/spark particles
- **Explosion**: Smoke, fire, debris
- **Blood Splat**: Hit effect (optional for Indian audience)

### Environmental Effects
- **Footsteps**: Dust clouds (desert), mud splatter (farmland)
- **Fire**: Burning flames animation
- **Smoke**: Various smoke effects

---

## Estimated Asset Counts

| Category | Count | Total Size |
|----------|-------|-----------|
| Character Sprites | 5 types × 6 anims = 30 | ~15 MB |
| Weapon Sprites | 6 weapons = 6 | ~1 MB |
| Loot Items | 12 items = 12 | ~1 MB |
| Tileset | 200+ tiles = 1 | ~5 MB |
| UI Elements | 50+ elements | ~2 MB |
| Audio (Music) | 4 tracks | ~20 MB |
| Audio (SFX) | 20+ sounds | ~5 MB |
| Voice Lines | 50+ clips | ~10 MB |
| **TOTAL** | | **~59 MB** |

---

## Asset Creation Tools

### Recommended Software
- **Sprites**: Aseprite, Piskel, GIMP, Krita
- **Maps**: Tiled Map Editor
- **Audio**: Audacity, FL Studio, GarageBand
- **UI**: Figma, Adobe XD, Inkscape

### Free Resources
- **OpenGameArt.org**: Free sprites, music, SFX
- **Itch.io**: Asset packs, music
- **Freesound.org**: Sound effects
- **Unsplash/Pexels**: Reference images

---

**Document Version**: 1.0  
**Last Updated**: May 2026
