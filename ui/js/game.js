let player1 = document.querySelector("#player-1");
let player2 = document.querySelector("#player-2");
let p1coords = [];
let params = new URLSearchParams(window.location.search);
const gameType = params.get("gameType");
//maps table x and y coordinates
const addTableIdentifiers = (table) => {
    row = table.children[0].children;
    for (let index = 0; index < row.length; index++) {
        row[index].setAttribute('x', index + 1)
        for (let jay = 0; jay < row[index].children.length; jay++) {
            row[index].children[jay].setAttribute('y', jay + 1);
        }
    }
}

window.onload = () => {
    addTableIdentifiers(player1)
    addTableIdentifiers(player2)
    console.log(gameType);
    if(gameType == 0) {
        document.querySelectorAll(".title span")[1].innerText = "Computer";
        eel.pvb();
    }
    if(gameType == 1){
        document.querySelectorAll(".title span")[1].innerText = "Player 2";
        eel.pvp();
    }
    eel.getBoard();
}
player1.addEventListener("click", (event) => {
    if(gameType == 1){
        let coords = [parseInt(event.target.parentNode.getAttribute('x')), event.target.getAttribute('y')]
        eel.attack(coords[0], coords[1], 1);
    }
});
player2.addEventListener("click", (event) => {
    let coords = [parseInt(event.target.parentNode.getAttribute('x')), event.target.getAttribute('y')]
    eel.attack(coords[0], coords[1], 0);
});
eel.expose(mapBoard)
function mapBoard(board, playerNum) {
    board = JSON.parse(board);
    let selectedTable;
    if (parseInt(playerNum) == 0) {
        selectedTable = player1.children[0].children;
    } else {
        selectedTable = player2.children[0].children;
    }
    for (let index = 0; index < board.length; index++) {
        tableRow = selectedTable[index].cells;
        console.log(board)
        for (let jay = 0; jay < tableRow.length; jay++) {
            const element = tableRow[jay];
            if (board[index][jay] == 0) {
                element.className = "";
            } else if(board[index][jay] == 1 ){
                if(selectedTable == player1.children[0].children){
                    element.className = "ship-cell";
                }else{
                    element.className = "";
                }
                
            } else if(board[index][jay] == 2){
                element.className = "miss-cell";
            } else {
                element.className = "hit-cell";
            }
        }
    }
}
eel.expose(gameAlert)
function gameAlert(message) {
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
eel.expose(showWinner)
function showWinner(winner) {
    let modal = document.querySelector(".modal-hidden");
    modal.className = "modal";
    document.querySelector("#gameResult").innerText = winner;
}