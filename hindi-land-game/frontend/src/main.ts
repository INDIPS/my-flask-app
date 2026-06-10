import Phaser from 'phaser';
import { BootScene } from '@scenes/BootScene';
import { MenuScene } from '@scenes/MenuScene';
import { GameplayScene } from '@scenes/GameplayScene';
import { GameOverScene } from '@scenes/GameOverScene';

// Hide loading screen
const loadingScreen = document.getElementById('loading');
if (loadingScreen) {
    loadingScreen.classList.add('hidden');
}

const config: Phaser.Types.Core.GameConfig = {
    type: Phaser.AUTO,
    width: 1280,
    height: 720,
    parent: 'game-container',
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 0 },
            debug: false,
        },
    },
    scene: [BootScene, MenuScene, GameplayScene, GameOverScene],
    render: {
        antialias: true,
        pixelArt: false,
    },
};

const game = new Phaser.Game(config);
