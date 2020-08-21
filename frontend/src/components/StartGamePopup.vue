<template>
  <v-card
    ><v-container
      ><v-card-title>Start Game</v-card-title>
      <v-card-text>hello its me mr chess</v-card-text>
      <v-card-actions
        ><v-btn
          large
          color="primary"
          class="mx-1"
          @click="
            $router.push({
              name: 'MainGame',
            })
          "
          >Play</v-btn
        ></v-card-actions
      ></v-container
    ></v-card
  >
</template>
