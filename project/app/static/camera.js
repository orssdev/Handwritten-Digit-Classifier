canvas = document.getElementById('canvas');

navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        const videoElement = document.getElementById('video');
        videoElement.srcObject = stream;

        test.addEventListener('click', () => {
            output.innerText = 'Output:'
            const canvas = document.createElement('canvas');
            const context = canvas.getContext('2d');
            canvas.width = videoElement.videoWidth;
            canvas.height = videoElement.videoHeight;
            context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
            const frameData = canvas.toDataURL('image/png');
            fetch('test/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ image: frameData })
            })
            .then(res => res.json())
            .then(data => {
                output.innerText = `Output: ${data.digit} confidence: ${data.confidence}`;
            });
        });
    })
    .catch(err => {
        console.log('Error accessing camera: ', err);
    });

canvas.addEventListener('click', () => {
    window.location.href = '/';
});