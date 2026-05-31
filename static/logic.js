const myBox = document.getElementById('myBox');
let btns = Array.from(myBox.querySelectorAll('button'));
console.log("Какая то длина = " + serverMatrix.length);
let indx = -1;
for (let i = 0; i < serverMatrix.length; i++) {
    for (let j = 0; j < serverMatrix.length; j++) {
        indx += 1;
        if (serverMatrix[i][j] === 'x') {
            btns[indx].classList.add('StateX');
        } else if (serverMatrix[i][j] === '0') {
            btns[indx].classList.add('State0');
        }
    }
}

myBox.addEventListener('click', function (event) {
    if (event.target.tagName === 'BUTTON') {
        let data = event.target.dataset.index;
        Move(data);

    }


});

async function Move(index) {
    const data = {
        number: index
    };
    const result = await fetch('/move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)

    });
    const res = await result.json();
    if (res.status === "ok") {
        btns[Number(index)].classList.add('StateX');
        let otvet = Number(res.move);
        btns[otvet].classList.add('State0');
    }

}

