import Vue from "vue";
import VueRouter from "vue-router";
import store from "../store/index.js";
import PickTeam from "../views/PickTeam.vue";
import Registration from "../views/Registration.vue";
import MyTeam from "../views/MyTeam.vue";
import Points from "../views/Points.vue";
import Transfers from "../views/Transfers.vue";

// Imports for Auth
import Login from "../views/Login.vue";
import RegisterUser from "../views/RegisterUser.vue";
import Reset from "../views/Reset.vue";

// Imports for Admin
import AdminMain from "../views/AdminMain.vue";

// If authenticated continue / Else goto login
const ifAuthenticated = (to, from, next) => {
  // next()
  if (store.getters.isAuthenticated) next();
  else next("/");
};

// If not authenticated continue / Else goto myteam
// For Login % Register route
const ifNotAuthenticated = (to, from, next) => {
  // next()
  if (!store.getters.isAuthenticated) next();
  else next("/myteam");
};

const routes = [
  {
    path: "/pickteam",
    name: "PickTeam",
    component: PickTeam,
    meta: { title: "Pick Team" },
    beforeEnter: ifAuthenticated,
  },
  // Save team for the first time
  {
    path: "/registration",
    name: "Registration",
    component: Registration,
    meta: { title: "Registration" },
    beforeEnter: ifAuthenticated,
  },
  {
    path: "/myteam",
    name: "MyTeam",
    component: MyTeam,
    meta: { title: "Manage your team" },
    beforeEnter: ifAuthenticated,
  },
  {
    path: "/points",
    name: "Points",
    component: Points,
    meta: { title: "Points" },
    beforeEnter: ifAuthenticated,
  },
  {
    path: "/transfers",
    name: "Transfers",
    component: Transfers,
    meta: { title: "Trading Block" },
    beforeEnter: ifAuthenticated,
  },

  // Routes For Auth
  {
    path: "/",
    alias: ["/login"],
    name: "Login",
    component: Login,
    meta: { title: "Login" },
    beforeEnter: ifNotAuthenticated,
  },
  {
    path: "/register",
    name: "Register",
    component: RegisterUser,
    meta: { title: "Register" },
    beforeEnter: ifNotAuthenticated,
  },
  {
    path: "/reset",
    name: "Reset Password",
    component: Reset,
    meta: { title: "Reset" },
    // add nav guard
  },

  // Route for Admin
  {
    path: "/admin",
    name: "Admin Dash",
    component: AdminMain,
    meta: { title: "Admin Dashboard" },
  },
];

Vue.use(VueRouter);

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

// Add page title
router.beforeEach((to, from, next) => {
  document.title = to.meta.title
    ? to.meta.title + " - " + "Fantasy DL"
    : "Fantasy DL";
  next();
});

export default router;
