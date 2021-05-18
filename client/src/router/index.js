import Vue from "vue";
import VueRouter from "vue-router";
import PickTeam from "../views/PickTeam.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/pick_team",
    name: "PickTeam",
    component: PickTeam,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
