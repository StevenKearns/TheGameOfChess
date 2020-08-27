<template>
  <v-card
    ><v-container
      ><v-card-title>Start Game</v-card-title>

      <v-row>
        <v-col
          ><v-text-field
            v-model="inputCode"
            placeholder="123456"
            label="Game Code"
          ></v-text-field></v-col
        ><v-col>
          <v-btn
            large
            color="primary"
            class="mx-1"
            @click="
              $router.push({
                name: 'MainGame',
                query: { gameCode: inputCode },
              })
            "
            >Enter Game code</v-btn
          ></v-col
        > </v-row
      ><v-divider></v-divider>
      <v-row
        ><v-col
          ><v-text-field
            readonly
            v-model="generatedCode"
            label="Generated Code"
          ></v-text-field></v-col
        ><v-col
          ><v-btn large color="primary" class="mx-1" @click="generateCode"
            >Generate Game Code</v-btn
          ></v-col
        ></v-row
      ><v-btn
        large
        color="primary"
        class="mx-1"
        @click="
          $router.push({
            name: 'MainGame',
          })
        "
        >Take me to next screen</v-btn
      ></v-container
    ></v-card
  >
</template>

<script>
export default {
  name: "MainScreen",
  methods: {
    generateCode: function() {
      // TODO: get code function
      this.$router.push({
        name: "MainGame",
        query: { gameCode: this.generatedCode },
      });
    },
  },
  data: () => ({
    generatedCode: "",
    inputCode: "",
  }),
};
</script>
