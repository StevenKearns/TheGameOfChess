<template>
  <v-app>
    <v-container>
      <h1 class="display-3 font-weight-bold my-5 text-center">
        The Game of Chess
      </h1>
      <v-container class="text-center">
        <v-col
          ><v-btn
            large
            color="blue"
            class="mx-1"
            @click="
              $router.push({
                name: 'GameScreen',
              })
            "
            >Play</v-btn
          ></v-col
        >

        <v-col
          ><v-btn
            large
            color="blue"
            class="mx-1"
            @click="
              $router.push({
                name: 'GameScreen',
              })
            "
            >Instructions</v-btn
          ></v-col
        ><v-col>
          <v-btn
            large
            color="blue"
            class="mx-1"
            @click="
              $router.push({
                name: 'GameScreen',
              })
            "
            >About</v-btn
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
};
</script>
