// static/js/scripts.js
document.addEventListener('DOMContentLoaded', function() {
    console.log("Weather Data Aggregator and Analyzer Loaded");

//    alert("Welcome to the Weather Data Aggregator and Analyzer!");

    // Example of smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
