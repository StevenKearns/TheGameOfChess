<template>
  <div class="board">
    <h4>
      Player {{ playerId }} <br />
      Current Turn {{ currentTurn }}
    </h4>
    <v-row>
      <ChessSquare
        v-for="(piece, index) in squares"
        :key="index"
        :piece="piece"
        :color="colors[(Math.floor(index / 8) + index) % 2]"
        :index="index"
    /></v-row>
  </div>
</template>

<script>
import io from "socket.io-client";
import ChessSquare from "./ChessSquare";

export default {
  data: function() {
    return {
      socket: {},
      // playerId: -1 (black), 0(unconnected), 1(white)
      playerId: 0,
      currentTurn: 0,
      colors: ["white", "brown"],
      // Very proud of the colors
      squares: Array(8 * 8)
        .fill()
        .map(() => ""),
      firstSpot: null,
    };
  },
  created() {
    // TODO: make this socket based on user ip address
    this.socket = io("http://localhost:3000");
    // set player and turn

    // caps for white, lowercase for black
    this.squares[this.tileXYTo64(0, 0)] = "r";
    this.squares[this.tileXYTo64(0, 1)] = "n";
    this.squares[this.tileXYTo64(0, 2)] = "b";
    this.squares[this.tileXYTo64(0, 3)] = "q";
    this.squares[this.tileXYTo64(0, 4)] = "k";
    this.squares[this.tileXYTo64(0, 5)] = "b";
    this.squares[this.tileXYTo64(0, 6)] = "n";
    this.squares[this.tileXYTo64(0, 7)] = "r";
    for (let i = 0; i < 8; i++) {
      this.squares[this.tileXYTo64(1, i)] = "p";
    }
    this.squares[this.tileXYTo64(7, 0)] = "R";
    this.squares[this.tileXYTo64(7, 1)] = "N";
    this.squares[this.tileXYTo64(7, 2)] = "B";
    this.squares[this.tileXYTo64(7, 3)] = "Q";
    this.squares[this.tileXYTo64(7, 4)] = "K";
    this.squares[this.tileXYTo64(7, 5)] = "B";
    this.squares[this.tileXYTo64(7, 6)] = "N";
    this.squares[this.tileXYTo64(7, 7)] = "R";
    for (let i = 0; i < 8; i++) {
      this.squares[this.tileXYTo64(6, i)] = "P";
    }

    this.socket.emit("initialize", this.squares);
  },
  mounted() {
    this.socket.on("chessboard", (data) => {
      this.squares = data.squares;
      this.checkGameStatus();
    });
    this.socket.on("playerId", (data) => {
      this.playerId = data;
    });
    this.socket.on("currentTurn", (data) => {
      this.currentTurn = data;
    });
    this.$root.$on("clickedsquare", (index) => {
      console.log(index, "clicked");
      if (this.firstSpot) {
        this.move(this.firstSpot, index);
      } else {
        this.firstSpot = index;
      }
    });
  },
  methods: {
    isValidMove(pieceName, index1, index2) {
      console.log(pieceName, index1, "=>", index2);
      return true;
    },
    tile64ToXY(tile) {
      let col = tile % 8;
      let row = Math.floor(tile / 8);
      return row, col;
    },
    tileXYTo64(row, col) {
      return row * 8 + col;
    },
    move(i1, i2) {
      this.firstSpot = null;
      let val1 = this.squares[i1];
      if (i1 == i2) {
        // No move
        return;
      }
      if (this.currentTurn != this.playerId) {
        // return;
      }
      if (
        (this.playerId == 1 && val1 == val1.toLowerCase()) ||
        (this.playerId == -1 && val1 == val1.toUpperCase())
      ) {
        // Player attempting to move other player's pieces
        return;
      }
      if (val1 && this.isValidMove(val1, i1, i2)) {
        console.log(i1, "->", i2);
        this.updateSquare(i2, val1);
        this.updateSquare(i1, "");
        this.emitMove();
        this.checkGameStatus();
      }
    },
    checkGameStatus() {
      // Check for kings to see if player has won, lost, or drawn
      if (!this.squares.includes("k") && !this.squares.includes("K")) {
        this.$router.push({
          name: "RoundEnd",
          query: { gameCode: this.gameCode, result: "draw" },
        });
      } else if (!this.squares.includes("k")) {
        let result;
        this.playerId == 1 ? (result = "victory") : (result = "defeat");
        this.$router.push({
          name: "RoundEnd",
          query: { gameCode: this.gameCode, result: result },
        });
      } else if (!this.squares.includes("K")) {
        let result;
        this.playerId == -1 ? (result = "victory") : (result = "defeat");
        this.$router.push({
          name: "RoundEnd",
          query: { gameCode: this.gameCode, result: result },
        });
      }
    },
    emitMove() {
      let moveInfo = {
        squares: this.squares,
        playerId: this.playerId,
      };
      this.socket.emit("move", moveInfo);
    },
    updateSquare(index, value) {
      this.squares.splice(index, 1, value);
    },
  },
  components: {
    ChessSquare,
  },
};
</script>

<style scoped>
.board {
  display: flex;
  flex-wrap: wrap;
  min-width: 400px;
  max-width: 400px;
}
</style>
