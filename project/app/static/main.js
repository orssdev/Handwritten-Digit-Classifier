const canvas = document.getElementById('writing-canvas');
const ctx = canvas.getContext('2d');
const clear = document.getElementById("clear");
const write = document.getElementById("write");
const big = document.getElementById("big");
const small = document.getElementById("small");
const erase = document.getElementById("erase");
const test = document.getElementById("test");
const camera = document.getElementById("camera");
let output = document.getElementById('output');

ctx.fillStyle = 'white';
ctx.fillRect(0, 0, 500, 500)

let isPainting = false;
let lineWidth = 15;
let startX;
let startY;

canvas.addEventListener('mousedown', (e) => {
    const canvasRect = canvas.getBoundingClientRect();
    isPainting = true;
    startX = e.clientX - canvasRect.left;
    startY = e.clientY - canvasRect.top;
    ctx.moveTo(startX, startY);
});

canvas.addEventListener('mouseup', (e) => {
    isPainting = false;
    ctx.stroke();
    ctx.beginPath();
});

const draw = e => {
    if(!isPainting) 
    {
        return;
    }

    ctx.lineWidth = lineWidth;
    ctx.lineCap = 'round';

    const canvasRect = canvas.getBoundingClientRect();
    const currentX = e.clientX - canvasRect.left;
    const currentY = e.clientY - canvasRect.top;

    ctx.lineTo(currentX, currentY);
    ctx.stroke();

    lastX = currentX;
    lastY = currentY;
}

clear.addEventListener('click', () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillRect(0, 0, 500, 500);
    output.innerText = 'Output:'
    
});

write.addEventListener('click', () => {
    ctx.strokeStyle = '#000000';
});
big.addEventListener('click', () => {
    lineWidth = 15;
});
small.addEventListener('click', () => {
    lineWidth = 5;
});

erase.addEventListener('click', () => {
    ctx.strokeStyle = '#ffffff';
});

canvas.addEventListener('mousemove', draw);

test.addEventListener('click', () => {
    const dataURL = canvas.toDataURL('image/png');
    output.innerText = 'Output:'
    fetch('test/', {
        method: 'POST',
        headers: { 
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ image: dataURL })
    })
    .then(res => res.json())
    .then(data => {
        output.innerText = `Output: ${data.digit} confidence: ${data.confidence}`;
    });
});

camera.addEventListener('click', () => {
    window.location.href = 'camera/';
});