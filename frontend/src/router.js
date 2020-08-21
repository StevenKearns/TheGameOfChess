import Vue from "vue";
import VueRouter from "vue-router";
import MainGame from "@/components/MainGame";
import MainMenu from "@/components/MainMenu";
import RoundEnd from "@/components/RoundEnd";

Vue.use(VueRouter);
export default new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "MainMenu",
      component: MainMenu,
    },
    {
      path: "/maingame",
      name: "MainGame",
      component: MainGame,
    },
    {
      path: "/roundend",
      name: "RoundEnd",
      component: RoundEnd,
    },
  ],
});
