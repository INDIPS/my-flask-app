// Game Types and Interfaces

export interface Vector2 {
    x: number;
    y: number;
}

export interface Player {
    id: string;
    username: string;
    x: number;
    y: number;
    health: number;
    maxHealth: number;
    armor: number;
    character: CharacterType;
    weapon: WeaponType;
    isAlive: boolean;
}

export type CharacterType = 'farmer' | 'student' | 'worker' | 'vendor' | 'teacher';
export type WeaponType = 'cricket_bat' | 'chappal' | 'lathi' | 'revolver' | 'rifle';
export type VehicleType = 'auto_rickshaw' | 'tractor' | 'bike';
export type LootType = 'weapon' | 'health' | 'armor' | 'ammo';

export interface Weapon {
    type: WeaponType;
    damage: number;
    fireRate: number;
    magazine: number;
    ammo: number;
    range: number;
}

export interface Loot {
    type: LootType;
    position: Vector2;
    item: WeaponType | string;
    quantity: number;
}

export interface Enemy {
    id: string;
    x: number;
    y: number;
    health: number;
    behavior: 'patrol' | 'chase' | 'attack';
    weapon: WeaponType;
    character: CharacterType;
}

export interface GameStats {
    kills: number;
    deaths: number;
    damageDealt: number;
    damageTaken: number;
    playersEliminated: number;
    survivedSeconds: number;
}

export interface SafeZone {
    x: number;
    y: number;
    radius: number;
    shrinkRate: number;
    currentPhase: number;
}

export interface MapLocation {
    name: string;
    x: number;
    y: number;
    width: number;
    height: number;
    type: 'city' | 'village' | 'desert' | 'mountain' | 'coast' | 'farmland';
    lootSpawns: number;
    enemySpawns: number;
}

export interface GameConfig {
    mapSize: Vector2;
    maxPlayers: number;
    initialSafeZoneRadius: number;
    gameDuration: number;
    characterSkins: CharacterType[];
    weapons: Weapon[];
    locations: MapLocation[];
}
