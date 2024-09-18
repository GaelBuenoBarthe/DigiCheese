window.onload = function() {
    // Remplacer le lien CSS par le fichier local
    const link = document.querySelector('link[href*="swagger-ui.css"]');
    if (link) {
        link.href = '/static/custom_swagger.css?v=1';
    }
    // Remplacer le script JS par le fichier local
    const script = document.querySelector('script[src*="swagger-ui-bundle.js"]');
    if (script) {
        script.src = '/static/swagger-ui-bundle.js?v=1';
    }
};