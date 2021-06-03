import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faUser,
  faUnlock,
  faUsers,
  faEnvelope,
  faExchangeAlt,
  faClock,
  faSync,
  faBuilding,
  faSignOutAlt,
  faPlayCircle,
  faEdit,
  faArrowCircleRight,
  faArrowCircleLeft,
  faPlus,
  faTrashAlt,
  faSave,
} from "@fortawesome/free-solid-svg-icons";

import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import VueProgressBar from "vue-progressbar";

// Custom CSS
// import "@/assets"

// Auth Config
import firebase from "firebase";
import randomWords from "random-words";
import FlashMessage from "@smartweb/vue-flash-message";

Vue.use(FlashMessage);
Vue.use(randomWords);
// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
var firebaseConfig = {
  apiKey: "AIzaSyAPzaJUfLJvCD_PtUjMovLA-pIPOwYS0WY",
  authDomain: "dl-cup-fantasy.firebaseapp.com",
  projectId: "dl-cup-fantasy",
  storageBucket: "dl-cup-fantasy.appspot.com",
  messagingSenderId: "956033126965",
  appId: "1:956033126965:web:660f34e0a535539d37177c",
  measurementId: "G-P841MCPGP4",
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();

Vue.config.productionTip = false;

// Add Font Awesome Icons
library.add(faUser);
library.add(faUnlock);
library.add(faUsers);
library.add(faEnvelope);
library.add(faExchangeAlt);
library.add(faClock);
library.add(faSync);
library.add(faBuilding);
library.add(faSignOutAlt);
library.add(faPlayCircle);
library.add(faEdit);
library.add(faArrowCircleRight);
library.add(faArrowCircleLeft);
library.add(faPlus);
library.add(faTrashAlt);
library.add(faSave);

Vue.component("fa", FontAwesomeIcon);

const progressBarOptions = {
  color: "rgb(255, 0, 140)",
  failedColor: "grey",
  thickness: "7px",
  transition: {
    speed: "0.5s",
    opacity: "0.1s",
    termination: 1000,
  },
  autoRevert: true,
  location: "top",
  inverse: false,
  autoFinish: true,
};

Vue.use(VueProgressBar, progressBarOptions);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
