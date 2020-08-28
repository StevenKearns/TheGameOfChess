const Express = require("express");
const Http = require("http").Server(Express);
const Socketio = require("socket.io")(Http);

var chessboard = {
  squares: Array(8 * 8)
    .fill()
    .map(() => ""),
  currentTurn: 0,
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
    } else if (playerCount == 2) {
      playerId = -1;
    } else {
      playerId = -2;
    }
    Socketio.emit("playerId", playerId);
    Socketio.emit("currentTurn", 1);
  });

  socket.emit("chessboard", chessboard);

  socket.on("move", (data) => {
    chessboard.squares = data.squares;
    Socketio.emit("chessboard", chessboard);
    chessboard.currentTurn = data.playerId * -1;
    Socketio.emit("currentTurn", chessboard.currentTurn);
    // console.log("Updated chessboard: ", chessboard.squares);
  });
});

Http.listen(3000, () => {
  console.log("Listening at :3000...");
});
