import Vue from "vue";
import VueRouter from "vue-router";
import PickTeam from "../views/PickTeam.vue";
import Registration from "../views/Registration.vue";
import MyTeam from "../views/MyTeam.vue";

// Imports for Auth
import Login from "../views/Login.vue";
import RegisterUser from "../views/RegisterUser.vue";
import Reset from "../views/Reset.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Login",
    component: Login,
    meta: { title: "Login" },
  },
  {
    path: "/pickteam",
    name: "PickTeam",
    component: PickTeam,
    meta: {
      title: "Pick Team",
      // Change progress bar for specific routes
      // progress: {
      //   func: [
      //     {call: 'color', modifier: 'temp', argument: '#ffb000'},
      //     {call: 'fail', modifier: 'temp', argument: '#6e0000'},
      //     {call: 'location', modifier: 'temp', argument: 'top'},
      //     {call: 'transition', modifier: 'temp', argument: {speed: '1.5s', opacity: '0.6s', termination: 400}}
      //   ]
      // },
    },
  },
  {
    path: "/registration",
    name: "Registration",
    component: Registration,
    meta: { title: "Registration" },
    // Add navigation guard
    // Allow only registering users
  },
  {
    path: "/myteam",
    name: "MyTeam",
    component: MyTeam,
    meta: { title: "Manage your team" },
  },

  // Routes For Auth
  {
    path: "/login",
    name: "Login",
    component: Login,
    meta: { title: "Login" },
  },
  {
    path: "/register",
    name: "Register",
    component: RegisterUser,
    meta: { title: "Register" },
  },
  {
    path: "/reset",
    name: "Reset Password",
    component: Reset,
    meta: { title: "Reset" },
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title
    ? to.meta.title + " - " + "Fantasy DL"
    : "Fantasy DL";
  next();
});

export default router;
