document.addEventListener('DOMContentLoaded', function() {
    let events = document.querySelectorAll('.life-event');
    let currentIndex = 0;

    function slideIn() {
        if (currentIndex >= events.length) {
            currentIndex = 0;  // Reset to the start to repeat
        }

        // Slide the current item into the frame
        events[currentIndex].style.left = '15vw';

        // Wait for a while and then slide out
        setTimeout(slideOut, 4000); 
    }

    function slideOut() {
        events[currentIndex].style.left = '100%';

        // Move to the next item after sliding out
        currentIndex++;

        // Wait for a while and then slide in the next item
        setTimeout(slideIn, 500);  
    }

        // Start the cycle with a 2-second delay before the first slide-in
        setTimeout(slideIn, 5000);
});


