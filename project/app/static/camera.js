canvas = document.getElementById('canvas');

navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        const videoElement = document.getElementById('video');
        videoElement.srcObject = stream;
    })
    .catch(err => {
        console.log('Error accessing camera: ', err);
    });

test.addEventListener('click', () => {
    output.innerText = 'Output:'
    fetch('test/')
    .then(res => res.json())
    .then(data => {
        let numbers = data.Numbers;
        for(const number of numbers)
        {
            output.innerText += ` ${number}`
        }
    });
});

canvas.addEventListener('click', () => {
    window.location.href = '/';
});