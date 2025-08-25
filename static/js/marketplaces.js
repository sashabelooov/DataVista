// Simple filter functionality
document.querySelectorAll('.filter-btn').forEach(button => {
    button.addEventListener('click', function() {
        // Remove active class from all buttons
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        
        // Add active class to clicked button
        this.classList.add('active');
        
        // In a real application, you would filter the cards here
        // For this example, we'll just log the filter
        console.log('Filtering by: ' + this.textContent);
    });
});

// View button functionality
document.querySelectorAll('.view-btn').forEach(button => {
    button.addEventListener('click', function() {
        const card = this.closest('.card');
        const name = card.querySelector('.card-name').textContent;
        alert(`Viewing marketplace: ${name}`);
    });
});
