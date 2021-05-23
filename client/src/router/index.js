import Vue from "vue";
import VueRouter from "vue-router";
import PickTeam from "../views/PickTeam.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/pickteam",
    name: "PickTeam",
    component: PickTeam,
    meta: { title: 'Pick Team' },
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title ? to.meta.title + ' - ' + 'Fantasy DL' : 'Fantasy DL';
  next();
});

export default router;
