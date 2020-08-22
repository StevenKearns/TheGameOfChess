<template>
  <v-app>
    <v-container>
      <h1 class="display-3 font-weight-bold my-5 text-center">
        You suffered a horrible {{ result }}
      </h1>
      <v-container class="text-center">
        <v-col
          ><v-btn
            large
            color="primary"
            class="mx-1"
            @click="
              $router.push({
                name: 'MainGame',
                query: { gameCode: gameCode },
              })
            "
            >Rematch</v-btn
          ></v-col
        >
        <v-col
          ><v-btn
            large
            color="primary"
            class="mx-1"
            @click="
              $router.push({
                name: 'MainMenu',
              })
            "
            >Return to Main Menu</v-btn
          ></v-col
        >

        <!-- <section class="headline"></section> -->
      </v-container>
    </v-container>
  </v-app>
</template>

<script>
export default {
  name: "MainScreen",
  data: () => ({}),
  computed: {
    gameCode: function() {
      return this.$route.query.gameCode;
    },
    result: function() {
      return this.$route.query.result;
    },
  },
  props: {},
};
</script>
