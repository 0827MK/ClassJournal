window.addEventListener('load', () => {
    const canvas = document.querySelector('#draw-area');
    const context = canvas.getContext('2d');
    const lastPosition = { x: null, y: null };
    let isDrag = false;

    let currentColor = '#000000';

    function draw(x, y) {
        if(!isDrag) {
        return;
        }
        
        context.lineCap = 'round';
        context.lineJoin = 'round';
        context.lineWidth = 5;
        context.strokeStyle = currentColor;
        if (lastPosition.x === null || lastPosition.y === null) {
        context.moveTo(x, y);
        } else {
        context.moveTo(lastPosition.x, lastPosition.y);
        }
        context.lineTo(x, y);
        context.stroke();

        lastPosition.x = x;
        lastPosition.y = y;
    }

    function clear() {
        context.clearRect(0, 0, canvas.width, canvas.height);
    }

    function dragStart(event) {
        context.beginPath();

        isDrag = true;
    }

    function dragEnd(event) {
        context.closePath();
        isDrag = false;
        lastPosition.x = null;
        lastPosition.y = null;
    }

    function initEventHandler() {
        const clearButton = document.querySelector('#clear-button');
        clearButton.addEventListener('click', clear);

      // 消しゴムモード
        const eraserButton = document.querySelector('#eraser-button');
        eraserButton.addEventListener('click', () => {
        currentColor = '#FFFFFF';
    });

        canvas.addEventListener('mousedown', dragStart);
        canvas.addEventListener('mouseup', dragEnd);
        canvas.addEventListener('mouseout', dragEnd);
        canvas.addEventListener('mousemove', (event) => {
        draw(event.layerX, event.layerY);
        });
    }

    // カラーパレットの設置
    function initColorPalette() {
        const joe = colorjoe.rgb('color-palette', currentColor);

        joe.on('done', color => {

        currentColor = color.hex();
        });
    }

    initEventHandler();

    initColorPalette();
    });