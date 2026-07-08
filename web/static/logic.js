const myBox = document.getElementById('myBox');
const MyForm = document.getElementById('MyForm');

let btns = Array.from(myBox.querySelectorAll('button'));
console.log("Какая то длина = " + serverMatrix.length);

for (let i = 0; i < serverMatrix.length; i++) {

    if (serverMatrix[i] === 'x') {
        btns[i].classList.add('StateX');
    } else if (serverMatrix[i] === '0') {
        btns[i].classList.add('State0');
    }
}

myBox.addEventListener('click', function (event) {
    if (event.target.tagName === 'BUTTON') {
        let data = event.target.dataset.index;
        Move(data);

    }


});

MyForm.addEventListener('submit', function (event) {
    event.preventDefault();
    let login = document.getElementById('login').value;
    let password = document.getElementById('password').value;
    Register(login, password);
});
async function Register(name, pass) {
    const data = {
        name: name,
        password: pass
    };
    /*
    const result = await fetch(`/registration`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    const res = await result.json();
    if (res.status === "ok") {
        MyForm.classList.add('MyFormOff');
        myBox.classList.add('loyout');
    }
    */
    MyForm.classList.add('MyFormOff');
    myBox.classList.remove('loyoutOff')
    myBox.classList.add('loyout');
    alert(data);
}

async function Move(index) {
    const data = {
        number: index
    };
    const result = await fetch(`/move/${game_id}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)

    });
    const res = await result.json();
    if (res.status === "ok") {
        btns[index].classList.add('StateX');
        let otvet = Number(res.move);
        btns[otvet].classList.add('State0');
        if (res.win === "player") {
            alert("Ты выйграл");
            location.reload();
        } else if (res.win === "bot") {
            alert("Ты проиграл");
            location.reload();
        } else if (res.win === "draw") {
            alert("Ничья");
            location.reload();
        }
    } else {
        alert("не возможный ход")
    }

}
