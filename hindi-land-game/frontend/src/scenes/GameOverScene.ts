import Phaser from 'phaser';
import { GameStats } from '@types/types';

export class GameOverScene extends Phaser.Scene {
    constructor() {
        super({ key: 'GameOverScene' });
    }

    init(data: { stats: GameStats }) {
        this.registry.set('gameStats', data.stats);
    }

    create() {
        const width = this.cameras.main.width;
        const height = this.cameras.main.height;
        const stats = this.registry.get('gameStats') as GameStats;

        // Background
        this.cameras.main.setBackgroundColor('#0a0a0a');

        // Game Over Title
        this.add.text(width / 2, height / 4, 'GAME OVER', {
            font: 'bold 80px Arial',
            fill: '#ff0000',
            align: 'center',
        }).setOrigin(0.5);

        // Stats
        const statsX = width / 2 - 150;
        const statsY = height / 2 - 100;
        const lineHeight = 40;

        this.add.text(statsX, statsY, `Kills: ${stats.kills}`, {
            font: 'bold 24px Arial',
            fill: '#ffff00',
        });

        this.add.text(statsX, statsY + lineHeight, `Damage Dealt: ${stats.damageDealt.toFixed(0)}`, {
            font: 'bold 24px Arial',
            fill: '#00ff00',
        });

        this.add.text(statsX, statsY + lineHeight * 2, `Survived: ${stats.survivedSeconds}s`, {
            font: 'bold 24px Arial',
            fill: '#00ffff',
        });

        this.add.text(statsX, statsY + lineHeight * 3, `Players Eliminated: ${stats.playersEliminated}`, {
            font: 'bold 24px Arial',
            fill: '#ff00ff',
        });

        // Restart Button
        const restartButton = this.add.rectangle(width / 2, height / 2 + 150, 200, 60, 0x6bcf7f);
        restartButton.setInteractive();
        restartButton.on('pointerdown', () => {
            this.scene.start('GameplayScene');
        });

        this.add.text(width / 2, height / 2 + 150, 'RESTART', {
            font: 'bold 28px Arial',
            fill: '#ffffff',
        }).setOrigin(0.5);

        // Menu Button
        const menuButton = this.add.rectangle(width / 2, height / 2 + 230, 200, 60, 0x4d96ff);
        menuButton.setInteractive();
        menuButton.on('pointerdown', () => {
            this.scene.start('MenuScene');
        });

        this.add.text(width / 2, height / 2 + 230, 'MENU', {
            font: 'bold 28px Arial',
            fill: '#ffffff',
        }).setOrigin(0.5);
    }
}
