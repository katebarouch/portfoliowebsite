document.addEventListener('DOMContentLoaded', function() {
    let events = document.querySelectorAll('.life-event');
    let currentIndex = 0;

    function slideIn() {
        if (currentIndex >= events.length) {
            return;
        }

        // Slide the current item into the frame
        events[currentIndex].style.left = '15vw';

        // Wait for a while and then slide out
        setTimeout(slideOut, 7000);  // 7 seconds, adjust as needed
    }

        // If this is the last event, don't schedule a slideOut
        if (currentIndex === events.length - 1) {
            return;
        }

    function slideOut() {
        events[currentIndex].style.left = '100%';

        // Move to the next item after sliding out
        currentIndex++;

        // Wait for a while and then slide in the next item
        setTimeout(slideIn, 1000);  // 1 second delay, adjust as needed
    }

        // Start the cycle with a 2-second delay before the first slide-in
        setTimeout(slideIn, 2000);
});


