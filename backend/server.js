const Express = require("express");
const Http = require("http").Server(Express);
const Socketio = require("socket.io")(Http);

var chessboard = {
    colors: ["white", "brown"],
    // Very proud of the colors
    squares: Array(8 * 8)
        .fill()
        .map(() => ""),
    firstSpot: null,
};

Socketio.on("connection", socket => {
    console.log("Player has connected.");
    socket.emit("chessboard", chessboard);
    console.log(chessboard);
    socket.on("move", data => {
        console.log(data);
        chessboard.squares = data;
        Socketio.emit("chessboard", chessboard);
    });
});

Http.listen(3000, () => {
    console.log("Listening at :3000...");
});