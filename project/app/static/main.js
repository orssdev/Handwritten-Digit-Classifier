const canvas = document.getElementById('writing-canvas');
const ctx = canvas.getContext('2d');
const clear = document.getElementById("clear");
const write = document.getElementById("write");
const erase = document.getElementById("erase");
const test = document.getElementById("test");

ctx.fillStyle = 'white';
ctx.fillRect(0, 0, 1200, 400)

let isPainting = false;
let lineWidth = 5;
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
    ctx.fillRect(0, 0, 1200, 400);
});

write.addEventListener('click', () => {
    lineWidth = 5;
    ctx.strokeStyle = '#000000';
});

erase.addEventListener('click', () => {
    lineWidth = 10;
    ctx.strokeStyle = '#ffffff';
});

canvas.addEventListener('mousemove', draw);

test.addEventListener('click', () => {
    let output = document.getElementById('output');
    output.innerText = 'Output:'
    fetch('/test')
    .then(res => res.json())
    .then(data => {
        let numbers = data.Numbers;
        for(const number of numbers)
        {
            output.innerText += ` ${number}`
        }
    });
});