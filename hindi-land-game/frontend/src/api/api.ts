import axios, { AxiosInstance } from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

class HindiLandAPI {
    private api: AxiosInstance;

    constructor() {
        this.api = axios.create({
            baseURL: API_BASE_URL,
            headers: {
                'Content-Type': 'application/json',
            },
        });

        // Add auth token if available
        const token = localStorage.getItem('auth_token');
        if (token) {
            this.api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        }
    }

    // ===== AUTH =====
    async register(username: string, email: string, password: string) {
        return this.api.post('/auth/register/', { username, email, password });
    }

    async login(username: string, password: string) {
        const response = await this.api.post('/auth/login/', { username, password });
        if (response.data.access) {
            localStorage.setItem('auth_token', response.data.access);
            this.api.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
        }
        return response;
    }

    async logout() {
        localStorage.removeItem('auth_token');
        delete this.api.defaults.headers.common['Authorization'];
    }

    // ===== PLAYER STATS =====
    async getPlayerStats(playerId: string) {
        return this.api.get(`/players/${playerId}/stats/`);
    }

    async updatePlayerStats(playerId: string, stats: any) {
        return this.api.post(`/players/${playerId}/stats/`, stats);
    }

    // ===== MATCHES =====
    async createMatch(matchData: any) {
        return this.api.post('/matches/', matchData);
    }

    async getMatch(matchId: string) {
        return this.api.get(`/matches/${matchId}/`);
    }

    async endMatch(matchId: string, results: any) {
        return this.api.post(`/matches/${matchId}/end/`, results);
    }

    // ===== LEADERBOARD =====
    async getLeaderboard(page: number = 1, limit: number = 10) {
        return this.api.get('/leaderboard/', { params: { page, limit } });
    }

    async getPlayerRank(playerId: string) {
        return this.api.get(`/leaderboard/${playerId}/rank/`);
    }

    // ===== INVENTORY =====
    async getPlayerInventory(playerId: string) {
        return this.api.get(`/players/${playerId}/inventory/`);
    }

    async updateInventory(playerId: string, inventory: any) {
        return this.api.post(`/players/${playerId}/inventory/`, inventory);
    }

    // ===== HEALTH CHECK =====
    async healthCheck() {
        return this.api.get('/health/');
    }
}

export const api = new HindiLandAPI();
