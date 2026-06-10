import { GameConfig, MapLocation, Weapon } from '@types/types';

export const GAME_CONFIG: GameConfig = {
    mapSize: { x: 2560, y: 1920 },
    maxPlayers: 100,
    initialSafeZoneRadius: 400,
    gameDuration: 900000, // 15 minutes in ms

    characterSkins: ['farmer', 'student', 'worker', 'vendor', 'teacher'],

    weapons: [
        {
            type: 'cricket_bat',
            damage: 25,
            fireRate: 0.5,
            magazine: -1,
            ammo: -1,
            range: 50,
        },
        {
            type: 'chappal',
            damage: 10,
            fireRate: 0.8,
            magazine: -1,
            ammo: -1,
            range: 40,
        },
        {
            type: 'lathi',
            damage: 35,
            fireRate: 0.3,
            magazine: -1,
            ammo: -1,
            range: 60,
        },
        {
            type: 'revolver',
            damage: 45,
            fireRate: 0.6,
            magazine: 6,
            ammo: 18,
            range: 300,
        },
        {
            type: 'rifle',
            damage: 60,
            fireRate: 0.1,
            magazine: 30,
            ammo: 90,
            range: 600,
        },
    ],

    locations: [
        // Cities
        {
            name: 'Delhi',
            x: 200,
            y: 200,
            width: 300,
            height: 300,
            type: 'city',
            lootSpawns: 15,
            enemySpawns: 8,
        },
        {
            name: 'Mumbai',
            x: 1800,
            y: 1600,
            width: 280,
            height: 280,
            type: 'city',
            lootSpawns: 15,
            enemySpawns: 8,
        },
        {
            name: 'Bangalore',
            x: 1200,
            y: 1400,
            width: 250,
            height: 250,
            type: 'city',
            lootSpawns: 12,
            enemySpawns: 6,
        },

        // Villages
        {
            name: 'Rajpur Village',
            x: 600,
            y: 500,
            width: 200,
            height: 200,
            type: 'village',
            lootSpawns: 8,
            enemySpawns: 4,
        },
        {
            name: 'Goan Village',
            x: 1600,
            y: 1000,
            width: 180,
            height: 180,
            type: 'village',
            lootSpawns: 7,
            enemySpawns: 3,
        },

        // Deserts
        {
            name: 'Thar Desert',
            x: 800,
            y: 1200,
            width: 400,
            height: 400,
            type: 'desert',
            lootSpawns: 5,
            enemySpawns: 5,
        },

        // Mountains
        {
            name: 'Himalayas',
            x: 300,
            y: 1000,
            width: 350,
            height: 350,
            type: 'mountain',
            lootSpawns: 8,
            enemySpawns: 6,
        },

        // Coastal
        {
            name: 'Goa Beach',
            x: 1500,
            y: 1700,
            width: 280,
            height: 280,
            type: 'coast',
            lootSpawns: 10,
            enemySpawns: 5,
        },

        // Farmland
        {
            name: 'Punjab Farms',
            x: 400,
            y: 400,
            width: 320,
            height: 320,
            type: 'farmland',
            lootSpawns: 9,
            enemySpawns: 5,
        },
    ],
};
