<template>
  <div class="board">
    <v-row>
      <ChessSquare
        v-for="(color, index) in squares"
        :color="colors[(Math.floor(index / 8) + index) % 2]"
        v-bind:key="index"
        :index="index"
    /></v-row>
  </div>
</template>

<script>
import ChessSquare from "./ChessSquare";

export default {
  data: () => ({
    colors: ["brown", "white"],
    // Very proud of the colors
    squares: Array(8 * 8)
      .fill()
      .map(() => "color"),
  }),
  mounted() {
    this.$root.$on("clickedsquare", (index) => {
      console.log(index, "clicked");
      // this.pixels.splice(index, 1, this.color);
    });
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
