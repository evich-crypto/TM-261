// Плавное появление карточек при загрузке
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, i) => {
        card.style.opacity = 0;
        card.style.transform = 'translateY(20px)';
        setTimeout(() => {
            card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            card.style.opacity = 1;
            card.style.transform = 'translateY(0)';
        }, 100 * i);
    });

    // Плавное появление секций на страницах законов
    const topics = document.querySelectorAll('.topic');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = 1;
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    topics.forEach(topic => {
        topic.style.opacity = 0;
        topic.style.transform = 'translateY(25px)';
        topic.style.transition = 'opacity 0.7s ease, transform 0.7s ease';
        observer.observe(topic);
    });
});