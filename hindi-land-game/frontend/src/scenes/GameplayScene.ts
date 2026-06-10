import Phaser from 'phaser';
import { GAME_CONFIG } from '@config/gameConfig';
import { Player, Enemy, Loot, SafeZone, GameStats } from '@types/types';

export class GameplayScene extends Phaser.Scene {
    private player!: Phaser.Physics.Arcade.Sprite;
    private cursors!: Phaser.Types.Input.Keyboard.CursorKeys;
    private enemies: Phaser.Physics.Arcade.Group | undefined;
    private loots: Phaser.Physics.Arcade.Group | undefined;
    private safeZone!: SafeZone;
    private gameStats: GameStats = {
        kills: 0,
        deaths: 0,
        damageDealt: 0,
        damageTaken: 0,
        playersEliminated: 0,
        survivedSeconds: 0,
    };
    private playerHealth: number = 100;
    private playerArmor: number = 0;
    private gameTimer: number = 0;
    private timeText!: Phaser.GameObjects.Text;
    private healthText!: Phaser.GameObjects.Text;
    private killsText!: Phaser.GameObjects.Text;
    private playersAliveText!: Phaser.GameObjects.Text;
    private playersAlive: number = 100;

    constructor() {
        super({ key: 'GameplayScene' });
    }

    create() {
        // Setup world
        this.physics.world.setBounds(0, 0, GAME_CONFIG.mapSize.x, GAME_CONFIG.mapSize.y);

        // Create map (placeholder - generate terrain)
        this.createMap();

        // Create player
        this.player = this.physics.add.sprite(400, 400, 'player');
        this.player.setBounce(0.2);
        this.player.setCollideWorldBounds(true);
        this.player.setMaxVelocity(300, 300);

        // Setup camera to follow player
        this.cameras.main.setBounds(0, 0, GAME_CONFIG.mapSize.x, GAME_CONFIG.mapSize.y);
        this.cameras.main.startFollow(this.player);

        // Input
        this.cursors = this.input.keyboard!.createCursorKeys();

        // Create UI
        this.createUI();

        // Create safe zone
        this.initializeSafeZone();

        // Spawn enemies
        this.spawnEnemies(10);

        // Spawn loot
        this.spawnLoot();

        // Start game timer
        this.time.addEvent({
            delay: 100,
            callback: this.updateGameTimer,
            callbackScope: this,
            loop: true,
        });
    }

    private createMap() {
        // Create simple map with different terrain types
        const graphics = this.make.graphics({ x: 0, y: 0, add: false });

        // Desert areas (sandy color)
        graphics.fillStyle(0xdaa520, 1);
        graphics.fillRect(800, 1200, 400, 400);

        // Mountains (gray)
        graphics.fillStyle(0x808080, 1);
        graphics.fillRect(300, 1000, 350, 350);

        // Farmland (green)
        graphics.fillStyle(0x228b22, 1);
        graphics.fillRect(400, 400, 320, 320);

        // Coast (blue)
        graphics.fillStyle(0x4169e1, 1);
        graphics.fillRect(1500, 1700, 280, 280);

        // Cities (dark gray - buildings)
        graphics.fillStyle(0x4a4a4a, 1);
        graphics.fillRect(200, 200, 300, 300);
        graphics.fillRect(1800, 1600, 280, 280);

        graphics.generateTexture('map', GAME_CONFIG.mapSize.x, GAME_CONFIG.mapSize.y);
        graphics.destroy();

        this.add.image(GAME_CONFIG.mapSize.x / 2, GAME_CONFIG.mapSize.y / 2, 'map');
    }

    private createUI() {
        const width = this.cameras.main.width;
        const height = this.cameras.main.height;

        // Time UI
        this.timeText = this.add.text(20, 20, 'Time: 00:00', {
            font: 'bold 20px Arial',
            fill: '#ffffff',
        });
        this.timeText.setScrollFactor(0);

        // Health UI
        this.healthText = this.add.text(20, 60, `Health: ${this.playerHealth}`, {
            font: 'bold 16px Arial',
            fill: '#00ff00',
        });
        this.healthText.setScrollFactor(0);

        // Kills UI
        this.killsText = this.add.text(20, 90, `Kills: ${this.gameStats.kills}`, {
            font: 'bold 16px Arial',
            fill: '#ffff00',
        });
        this.killsText.setScrollFactor(0);

        // Players Alive UI
        this.playersAliveText = this.add.text(width - 20, 20, `Players: ${this.playersAlive}`, {
            font: 'bold 20px Arial',
            fill: '#ff0000',
        });
        this.playersAliveText.setOrigin(1, 0);
        this.playersAliveText.setScrollFactor(0);

        // Safe Zone indicator
        this.add.text(width / 2, 20, '⭕ Safe Zone Active', {
            font: 'bold 16px Arial',
            fill: '#ffffff',
        }).setOrigin(0.5, 0).setScrollFactor(0);
    }

    private initializeSafeZone() {
        this.safeZone = {
            x: GAME_CONFIG.mapSize.x / 2,
            y: GAME_CONFIG.mapSize.y / 2,
            radius: GAME_CONFIG.initialSafeZoneRadius,
            shrinkRate: 0.98,
            currentPhase: 0,
        };

        // Draw safe zone
        this.drawSafeZone();

        // Start shrinking after 60 seconds
        this.time.delayedCall(60000, () => {
            this.shrinkSafeZone();
        });
    }

    private drawSafeZone() {
        // Draw circle for safe zone
        const graphics = this.make.graphics({ x: 0, y: 0, add: false });
        graphics.lineStyle(3, 0x00ff00, 1);
        graphics.strokeCircleShape(
            new Phaser.Geom.Circle(this.safeZone.x, this.safeZone.y, this.safeZone.radius)
        );
        graphics.generateTexture('safeZone', this.safeZone.radius * 2, this.safeZone.radius * 2);
        graphics.destroy();

        const zone = this.add.sprite(this.safeZone.x, this.safeZone.y, 'safeZone');
        zone.setDepth(-1);
    }

    private shrinkSafeZone() {
        this.tweens.add({
            targets: this.safeZone,
            radius: this.safeZone.radius * this.safeZone.shrinkRate,
            duration: 5000,
            onUpdate: () => {
                this.drawSafeZone();
            },
        });
    }

    private spawnEnemies(count: number) {
        this.enemies = this.physics.add.group();

        for (let i = 0; i < count; i++) {
            const x = Phaser.Math.Between(100, GAME_CONFIG.mapSize.x - 100);
            const y = Phaser.Math.Between(100, GAME_CONFIG.mapSize.y - 100);

            const enemy = this.enemies.create(x, y, 'enemy');
            enemy.setMaxVelocity(200, 200);
            enemy.setData('health', 50);
        }
    }

    private spawnLoot() {
        this.loots = this.physics.add.group();

        GAME_CONFIG.locations.forEach((location) => {
            for (let i = 0; i < location.lootSpawns; i++) {
                const x = Phaser.Math.Between(location.x, location.x + location.width);
                const y = Phaser.Math.Between(location.y, location.y + location.height);

                const loot = this.loots!.create(x, y, 'loot');
                loot.setData('item', 'health_pack');
            }
        });
    }

    private updateGameTimer = () => {
        this.gameTimer += 100;
        const seconds = Math.floor(this.gameTimer / 1000);
        const minutes = Math.floor(seconds / 60);
        const secs = seconds % 60;

        this.timeText.setText(
            `Time: ${minutes.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`
        );
        this.healthText.setText(`Health: ${this.playerHealth}`);
        this.killsText.setText(`Kills: ${this.gameStats.kills}`);
        this.playersAliveText.setText(`Players: ${this.playersAlive}`);
    };

    update() {
        // Player movement
        if (this.cursors.up.isDown || this.input.keyboard!.addKey('W').isDown) {
            this.player.setAcceleration(0, -500);
        } else if (this.cursors.down.isDown || this.input.keyboard!.addKey('S').isDown) {
            this.player.setAcceleration(0, 500);
        } else {
            this.player.setAccelerationY(0);
        }

        if (this.cursors.left.isDown || this.input.keyboard!.addKey('A').isDown) {
            this.player.setAcceleration(-500, 0);
        } else if (this.cursors.right.isDown || this.input.keyboard!.addKey('D').isDown) {
            this.player.setAcceleration(500, 0);
        } else {
            this.player.setAccelerationX(0);
        }

        // Check if player is outside safe zone
        const distance = Phaser.Math.Distance.Between(
            this.player.x,
            this.player.y,
            this.safeZone.x,
            this.safeZone.y
        );

        if (distance > this.safeZone.radius) {
            this.takeDamage(0.5); // Damage per frame outside zone
        }

        // Collision detection with loot
        if (this.loots) {
            this.physics.overlap(this.player, this.loots, (_, loot: any) => {
                console.log('Loot collected!');
                loot.destroy();
            });
        }

        // Simple enemy AI
        if (this.enemies) {
            this.enemies.children.entries.forEach((enemy: any) => {
                const distance = Phaser.Math.Distance.Between(
                    this.player.x,
                    this.player.y,
                    enemy.x,
                    enemy.y
                );

                if (distance < 300) {
                    // Chase player
                    const angle = Phaser.Math.Angle.Between(this.player.x, this.player.y, enemy.x, enemy.y);
                    enemy.setVelocity(Math.cos(angle) * -150, Math.sin(angle) * -150);
                } else {
                    // Patrol
                    enemy.setVelocity(Phaser.Math.Between(-50, 50), Phaser.Math.Between(-50, 50));
                }
            });
        }
    }

    private takeDamage(amount: number) {
        if (this.playerArmor > 0) {
            const damageToArmor = Math.min(this.playerArmor, amount * 0.5);
            this.playerArmor -= damageToArmor;
            amount -= damageToArmor;
        }

        this.playerHealth -= amount;
        this.gameStats.damageTaken += amount;

        if (this.playerHealth <= 0) {
            this.endGame();
        }
    }

    private endGame() {
        this.scene.start('GameOverScene', { stats: this.gameStats });
    }
}
