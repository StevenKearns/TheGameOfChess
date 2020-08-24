<template>
  <div class="board">
    <v-row>
      <ChessSquare
        v-for="(piece, index) in squares"
        v-bind:key="index"
        :piece="piece"
        :color="colors[(Math.floor(index / 8) + index) % 2]"
        :index="index"
    /></v-row>
  </div>
</template>

<script>
import ChessSquare from "./ChessSquare";

export default {
  data: () => ({
    colors: ["white", "brown"],
    // Very proud of the colors
    squares: Array(8 * 8)
      .fill()
      .map(() => ""),
    firstSpot: null,
  }),
  mounted() {
    this.$root.$on("clickedsquare", (index) => {
      console.log(index, "clicked");
      // this.pixels.splice(index, 1, this.color);
      if (this.firstSpot) {
        // console.log(this.firstSpot, "->", index);
        this.move(this.firstSpot, index);
      } else {
        this.firstSpot = index;
      }
    });
    // caps for white, lowercase for black
    this.squares[0] = "r";
    this.squares[1] = "n";
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
      this.squares[this.tileXYTo64(6, i)] = "p";
    }
  },
  methods: {
    tile64ToXY(tile) {
      let col = tile % 8;
      let row = Math.floor(tile / 8);
      return row, col;
    },
    tileXYTo64(row, col) {
      console.log(row, col, "=>", row * 8 + col);
      return row * 8 + col;
    },
    move(i1, i2) {
      console.log(i1, "->", i2);
      this.firstSpot = null;
      this.squares[i2] = this.squares[i1];
      this.squares[i1] = "";
      console.log(this.squares);
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
  max-width: 400px;
}
</style>
