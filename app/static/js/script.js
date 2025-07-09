document.addEventListener('DOMContentLoaded', function() {
    // Animar os cards de previsão
    const predictionCards = document.querySelectorAll('.prediction-card');
    
    predictionCards.forEach((card, index) => {
        setTimeout(() => {
            card.classList.add('animate-in');
        }, index * 200);
    });
    
    // Atualizar a página diariamente às 8:00
    function checkForDailyUpdate() {
        const now = new Date();
        const lastUpdateStr = document.querySelector('.last-update').textContent;
        const lastUpdateDate = new Date(lastUpdateStr.split(': ')[1]);
        
        if (now.getHours() === 8 && now.getMinutes() === 0 && 
            (now.getDate() !== lastUpdateDate.getDate() || 
             now.getMonth() !== lastUpdateDate.getMonth() || 
             now.getFullYear() !== lastUpdateDate.getFullYear())) {
            location.reload();
        }
    }
    
    // Verificar a cada minuto
    setInterval(checkForDailyUpdate, 60000);
});