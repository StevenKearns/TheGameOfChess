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
            color="primary"
            class="mx-1"
            @click.stop="startGameDialog = true"
            >Play</v-btn
          ></v-col
        >
        <v-col
          ><v-btn
            large
            color="primary"
            class="mx-1"
            @click.stop="instructionsDialog = true"
            >Instructions</v-btn
          ></v-col
        ><v-col>
          <v-btn
            large
            color="primary"
            class="mx-1"
            @click.stop="aboutDialog = true"
            >About</v-btn
          ></v-col
        >
        <v-dialog v-model="startGameDialog" max-width="600"
          ><StartGamePopup></StartGamePopup
        ></v-dialog>
        <v-dialog v-model="instructionsDialog" max-width="600"
          ><InstructionsPopup></InstructionsPopup
        ></v-dialog>
        <v-dialog v-model="aboutDialog" max-width="600"
          ><AboutPopup></AboutPopup
        ></v-dialog>
      </v-container>
    </v-container>
  </v-app>
</template>

<script>
import AboutPopup from "@/components/AboutPopup";
import StartGamePopup from "@/components/StartGamePopup";
import InstructionsPopup from "@/components/InstructionsPopup";
export default {
  name: "MainScreen",
  data: () => ({
    startGameDialog: false,
    instructionsDialog: false,
    aboutDialog: false,
  }),
  components: {
    AboutPopup,
    StartGamePopup,
    InstructionsPopup,
  },
};
</script>
