let pvp = document.querySelector("#pvp");
let pvc = document.querySelector("#pvc");
let closeBtn = document.querySelector("#closeModal");
let startGameBtn = document.querySelector("#startGame");
let gameType = null;
// 0 = player vs computer, 1 = player vs player
const showModal = () => {
    let modal = document.querySelector(".modal-hidden");
    modal.className = "modal";
}
const closeModal = () => {
    let modal = document.querySelector(".modal");
    modal.className = "modal-hidden";
}
pvc.addEventListener("click", () => {
    showModal();
    gameType = 0;
});
pvp.addEventListener("click", () => {
    showModal();
    gameType = 1;
})
closeBtn.addEventListener("click",  closeModal);
startGameBtn.addEventListener("click", () => {
    let values = [document.querySelector("#ship1").value,document.querySelector("#ship2").value, document.querySelector("#ship3").value, document.querySelector("#ship4").value];
    let invalidValue = false;
    for (let index = 0; index < values.length; index++) {
        const element = values[index];
        if(isNaN(parseInt(element))){
            invalidValue = true;
            break
        }
    }
    if(invalidValue) {
        message("Please check your values")
    } else {
        message("valid values");
    }
})
const message = (message) => {
    toast = siiimpleToast.setOptions({
        container: 'body',
        class: 'toast',
        position: 'bottom|right',
        margin: (15*2),
        delay: 0,
        duration: 3000,
        style: {},
    });
    toast.message(message)
}