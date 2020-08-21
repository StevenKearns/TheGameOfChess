<template>
  <v-app>
    <v-container>
      <h1 class="display-3 font-weight-bold my-5 text-center">
        You suffered a horrible defeat
      </h1>
      <v-container class="text-center">
        <!-- TODO: rematch button. Not in MVP scope -->
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
  props: {},
};
</script>
