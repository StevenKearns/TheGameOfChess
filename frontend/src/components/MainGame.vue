<template>
  <v-app>
    <v-container>
      <h1 class="display-3 font-weight-bold my-5 text-center">
        The Game of Chess
      </h1>
      The gamecode is: {{ gameCode }} <br />Send this url to your opponent:
      http://localhost:8080/maingame?gameCode={{ gameCode }}
      <v-container class="text-center">
        <Chessboard></Chessboard>
      </v-container>
      <v-container class="text-center">
        <v-col
          ><v-btn
            large
            color="primary"
            class="mx-1"
            @click.stop="instructionsDialog = true"
            >Help</v-btn
          ></v-col
        >
        <v-col
          ><v-btn large color="error" class="mx-1" @click="resign"
            >Resign</v-btn
          ></v-col
        >
        <!-- TODO: make an "are you sure" dialog when resigning. -->
        <!-- TODO: propose a draw. Not in MVP scope. -->

        <v-dialog v-model="instructionsDialog" max-width="600"
          ><InstructionsPopup></InstructionsPopup
        ></v-dialog>
      </v-container>
    </v-container>
  </v-app>
</template>

<script>
import InstructionsPopup from "@/components/InstructionsPopup";
import Chessboard from "@/components/Chessboard";
export default {
  name: "MainScreen",
  data: () => ({ instructionsDialog: false }),
  // props: ["gameCode"],
  methods: {
    resign: function() {
      // TODO: get code function
      this.$router.push({
        name: "RoundEnd",
        query: { gameCode: this.gameCode, result: "defeat" },
      });
    },
  },
  computed: {
    gameCode: function() {
      return this.$route.query.gameCode;
    },
  },
  components: {
    InstructionsPopup: InstructionsPopup,
    Chessboard: Chessboard,
  },
};
</script>
