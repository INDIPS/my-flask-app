import Phaser from 'phaser';

export class BootScene extends Phaser.Scene {
    constructor() {
        super({ key: 'BootScene' });
    }

    preload() {
        // Load assets here
        // TODO: Load sprites, sounds, maps

        // Progress bar
        const progressBar = this.add.graphics();
        const progressBox = this.add.graphics();
        progressBox.fillStyle(0x222222, 0.8);
        progressBox.fillRect(240, 270, 320, 50);

        const width = this.cameras.main.width;
        const height = this.cameras.main.height;
        const loadingText = this.make.text(
            {
                x: width / 2,
                y: height / 2 - 50,
                text: 'Loading...',
                style: {
                    font: '20px monospace',
                    fill: '#ffffff',
                },
            },
            false
        );
        loadingText.setOrigin(0.5, 0.5);

        const percentText = this.make.text(
            {
                x: width / 2,
                y: height / 2 + 30,
                text: '0%',
                style: {
                    font: '18px monospace',
                    fill: '#ffffff',
                },
            },
            false
        );
        percentText.setOrigin(0.5, 0.5);

        this.load.on('progress', (value: number) => {
            progressBar.clear();
            progressBar.fillStyle(0x00ff00, 1);
            progressBar.fillRect(250, 280, 300 * value, 30);
            percentText.setText(Math.round(value * 100) + '%');
        });

        this.load.on('complete', () => {
            progressBar.destroy();
            progressBox.destroy();
            loadingText.destroy();
            percentText.destroy();
        });
    }

    create() {
        // Initialize game
        this.scene.start('MenuScene');
    }
}
