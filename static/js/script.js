// Initialize charts when the page loads
document.addEventListener('DOMContentLoaded', function() {
    // Sales Chart
    const salesCtx = document.getElementById('salesChart').getContext('2d');
    const salesChart = new Chart(salesCtx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            datasets: [{
                label: 'Sales ($)',
                data: [12000, 19000, 15000, 25000, 22000, 30000, 28000, 35000, 30000, 40000, 38000, 45000],
                borderColor: '#4361ee',
                tension: 0.3,
                fill: true,
                backgroundColor: 'rgba(67, 97, 238, 0.1)'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        drawBorder: false
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            }
        }
    });
    
    // Traffic Chart
    const trafficCtx = document.getElementById('trafficChart').getContext('2d');
    const trafficChart = new Chart(trafficCtx, {
        type: 'doughnut',
        data: {
            labels: ['Direct', 'Social Media', 'Search Engines', 'Referrals', 'Email'],
            datasets: [{
                data: [35, 25, 20, 15, 5],
                backgroundColor: [
                    '#4361ee',
                    '#3f37c9',
                    '#4cc9f0',
                    '#fca311',
                    '#e5383b'
                ],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'right'
                }
            }
        }
    });
    
    // Category Chart
    const categoryCtx = document.getElementById('categoryChart').getContext('2d');
    const categoryChart = new Chart(categoryCtx, {
        type: 'bar',
        data: {
            labels: ['Electronics', 'Clothing', 'Home & Garden', 'Beauty', 'Sports'],
            datasets: [{
                label: 'Sales by Category',
                data: [65, 59, 80, 45, 56],
                backgroundColor: '#4361ee'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        drawBorder: false
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            }
        }
    });
    
    // Satisfaction Chart
    const satisfactionCtx = document.getElementById('satisfactionChart').getContext('2d');
    const satisfactionChart = new Chart(satisfactionCtx, {
        type: 'line',
        data: {
            labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
            datasets: [{
                label: 'Satisfaction Rate',
                data: [85, 92, 78, 95],
                borderColor: '#4cc9f0',
                tension: 0.3,
                fill: false,
                pointBackgroundColor: '#4cc9f0',
                pointRadius: 5
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    min: 50,
                    max: 100,
                    grid: {
                        drawBorder: false
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            }
        }
    });

    // Modal functionality
    const modal = document.getElementById('contact-modal');
    const contactLink = document.getElementById('contact-link');
    const footerContactLink = document.getElementById('footer-contact-link');
    const closeModal = document.querySelector('.close-modal');

    function openModal() {
        modal.style.display = 'flex';
    }

    function closeModalFunc() {
        modal.style.display = 'none';
    }

    contactLink.addEventListener('click', function(e) {
        e.preventDefault();
        openModal();
    });

    footerContactLink.addEventListener('click', function(e) {
        e.preventDefault();
        openModal();
    });

    closeModal.addEventListener('click', closeModalFunc);

    window.addEventListener('click', function(e) {
        if (e.target === modal) {
            closeModalFunc();
        }
    });

    // Form submission
    const contactForm = document.getElementById('contact-form');
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        alert('Thank you for your message! We will get back to you soon.');
        contactForm.reset();
        closeModalFunc();
    });
});
