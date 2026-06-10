import Phaser from 'phaser';

export class MenuScene extends Phaser.Scene {
    constructor() {
        super({ key: 'MenuScene' });
    }

    create() {
        const width = this.cameras.main.width;
        const height = this.cameras.main.height;

        // Background
        this.cameras.main.setBackgroundColor('#1a1a2e');

        // Title
        const title = this.add.text(width / 2, height / 3, '🎮 HINDI LAND', {
            font: 'bold 80px Arial',
            fill: '#ff6b6b',
            align: 'center',
        });
        title.setOrigin(0.5);

        // Subtitle
        const subtitle = this.add.text(width / 2, height / 3 + 80, 'Battle Royale Game', {
            font: '30px Arial',
            fill: '#ffd93d',
            align: 'center',
        });
        subtitle.setOrigin(0.5);

        // Play Button
        const playButton = this.add.rectangle(width / 2, height / 2 + 50, 200, 60, 0x6bcf7f);
        playButton.setInteractive();
        playButton.on('pointerdown', () => {
            this.scene.start('GameplayScene');
        });
        playButton.on('pointerover', () => {
            playButton.setFillStyle(0x5ab86d);
        });
        playButton.on('pointerout', () => {
            playButton.setFillStyle(0x6bcf7f);
        });

        const playText = this.add.text(width / 2, height / 2 + 50, 'PLAY', {
            font: 'bold 28px Arial',
            fill: '#ffffff',
        });
        playText.setOrigin(0.5);

        // Settings Button
        const settingsButton = this.add.rectangle(width / 2, height / 2 + 130, 200, 60, 0x4d96ff);
        settingsButton.setInteractive();
        settingsButton.on('pointerdown', () => {
            console.log('Settings clicked');
        });

        const settingsText = this.add.text(width / 2, height / 2 + 130, 'SETTINGS', {
            font: 'bold 28px Arial',
            fill: '#ffffff',
        });
        settingsText.setOrigin(0.5);

        // Stats Button
        const statsButton = this.add.rectangle(width / 2, height / 2 + 210, 200, 60, 0xa29bfe);
        statsButton.setInteractive();

        const statsText = this.add.text(width / 2, height / 2 + 210, 'STATS', {
            font: 'bold 28px Arial',
            fill: '#ffffff',
        });
        statsText.setOrigin(0.5);

        // Version
        this.add.text(width - 10, height - 10, 'v0.1.0 - Alpha', {
            font: '12px Arial',
            fill: '#888888',
        }).setOrigin(1, 1);
    }
}
