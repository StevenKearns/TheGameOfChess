<template>
  <div>
    <h2 v-if="title" class="display-1 font-weight-bold text-center">
      {{ title }}
    </h2>
    <v-row
      v-for="(letter, index1) of letters"
      v-bind:key="index1"
      align="start"
      justify="center"
    >
      <v-col v-for="index2 in 8" v-bind:key="index2" cols="1">
        <ChessSquare></ChessSquare>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import ChessSquare from "./ChessSquare";
export default {
  props: ["people", "title"],
  data: () => ({ letters: ["a", "b", "c", "d", "e", "f", "g"] }),
  components: {
    ChessSquare,
  },
};
</script>
