function connectSocket(username) {

    const socket = io()

    socket.on('connect', function() {
        socket.emit('login', { id: socket.id, username })
    })

    return socket

}



const btnNewGame = document.querySelector('#btn-new-game')

btnNewGame.addEventListener('click', function () {

    const username = prompt("Por favor, insira o nome do usuário")

    const socket = connectSocket(username)

    console.log('socket conectado', socket)
    
})