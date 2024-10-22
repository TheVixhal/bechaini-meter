function setMeter(actualScore) {
    const needle = document.getElementById('needle');
    const randomInterval = 100; // Change position every 100 ms
    let randomTime = 0;
    const endTime = 7000; // 7 seconds in milliseconds
    const endRotation = (actualScore - 50) * 1.8; // Calculate final rotation based on score

    // Function to generate random rotation
    function randomRotation() {
        return Math.random() * 180 - 90; // Random rotation between -90 and 90 degrees
    }

    // Random movement of the needle
    const intervalId = setInterval(() => {
        needle.style.transform = `rotate(${randomRotation()}deg)`;
        randomTime += randomInterval;

        // After 7 seconds, stop the random movement and set to actual score
        if (randomTime >= endTime) {
            clearInterval(intervalId);
            needle.style.transition = 'transform 1s ease'; // Smooth transition to final position
            needle.style.transform = `rotate(${endRotation}deg)`;
        }
    }, randomInterval);
}
