<template>
  <div
    :class="['square', color, highlight ? 'highlight' : '']"
    @click.end="handleClick"
  >
    {{ piece }}
  </div>
</template>

<script>
export default {
  name: "ChessSquare",
  props: {
    color: String,
    highlight: Boolean,
    piece: String,
    index: Number,
  },
  methods: {
    handleClick: function() {
      this.$root.$emit("clickedsquare", this.index);
    },
  },
};
</script>

<style scoped>
.square {
  border: 2px solid grey;
  width: 50px;
  height: 50px;
  box-sizing: border-box;
}
.white {
  background-color: white;
}
.brown {
  background-color: rgb(101, 105, 105);
}
.square.highlight {
  border: 4px solid yellow;
}
</style>
