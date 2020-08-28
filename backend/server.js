const Express = require("express");
const Http = require("http").Server(Express);
const Socketio = require("socket.io")(Http);

var chessboard = {
  squares: Array(8 * 8)
    .fill()
    .map(() => ""),
  playerTurn: 0,
};

Socketio.on("connection", (socket) => {
  console.log("Player", Socketio.engine.clientsCount, "has connected.");
  let playerCount = Socketio.engine.clientsCount;

  socket.on("initialize", (data) => {
    chessboard.squares = data;
    Socketio.emit("chessboard", chessboard);

    let playerId;
    if (playerCount == 1) {
      playerId = 1;
    } else {
      playerId = -1;
    }
    Socketio.emit("playerId", playerId);
  });

  socket.emit("chessboard", chessboard);

  socket.on("move", (data) => {
    chessboard.squares = data;
    Socketio.emit("chessboard", chessboard);
    console.log("Updated chessboard: ", chessboard.squares);
  });
});

Http.listen(3000, () => {
  console.log("Listening at :3000...");
});
