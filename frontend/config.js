const ECO_TERRACE_CONFIG = { 
    development: { 
        API_BASE: 'http://127.0.0.1:5000', 
        FRONTEND_URL: 'file:///e:/Ecoterrace/frontend/index.html' 
    }, 
    production: { 
        API_BASE: 'http:// 10.50.31.254:5000', 
        FRONTEND_URL: 'http:// 10.50.31.254:8000' 
    } 
 
const getEnvironment = () =
window.EcoTerrace = { 
    config: ECO_TERRACE_CONFIG.production, 
    environment: 'production' 
}; 
