// Smooth scrolling for navigation links
document.querySelectorAll('.navbar a').forEach(link => {
    link.addEventListener('click', function(e) {
        if (this.hash !== "") {
            e.preventDefault();
            const target = document.querySelector(this.hash);
            if (target) {
                window.scrollTo({
                    top: target.offsetTop - 50,
                    behavior: 'smooth'
                });
            }
        }
    });
});

// Feature card animation
document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('click', () => {
        alert("Feature coming soon! Stay tuned for updates.");
    });
});
