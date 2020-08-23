const Express = require("express");
const Http = require("http").Server(Express);
const Socketio = require("socket.io")(Http);

/*
var chessboard = {

};
*/

/*
Socketio.onconnection("connection", socket => {
    socket.emit("chessboard", chessboard);
})
*/

Http.listen(3000, () => {
    console.log("Listening at :3000...");
})