// Animação dos cards
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.prediction-card');
    cards.forEach((card, i) => {
        setTimeout(() => {
            card.style.opacity = 1;
        }, i * 200);
    });

    // Verificar atualizações às 8:00
    setInterval(() => {
        const now = new Date();
        if (now.getHours() === 8 && now.getMinutes() === 0) {
            location.reload();
        }
    }, 60000);
});