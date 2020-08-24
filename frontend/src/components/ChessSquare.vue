<template>
  <div
    :class="['square', color, highlight ? 'highlight' : '']"
    @click="handleClick"
  ></div>
</template>

<script>
export default {
  props: {
    color: String,
    highlight: Boolean,
    pieceName: String,
    index: Number,
  },
  methods: {
    handleClick: function() {
      // if (this.isInColorPicker) {
      //   this.$root.$emit("updatecolor", this.color);
      // }
    },
  },
};
</script>

<style scoped>
.square {
  border: 2px solid black;
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
