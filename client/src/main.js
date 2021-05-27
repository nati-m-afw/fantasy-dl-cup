import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUser } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import VueProgressBar from 'vue-progressbar'

Vue.config.productionTip = false;

library.add(faUser);

Vue.component("fa", FontAwesomeIcon);

const progressBarOptions = {
  color: 'rgb(255, 0, 140)',
  failedColor: 'grey',
  thickness: '7px',
  transition: {
    speed: '0.5s',
    opacity: '0.1s',
    termination: 1000
  },
  autoRevert: true,
  location: 'top',
  inverse: false,
  autoFinish: true,
};

Vue.use(VueProgressBar, progressBarOptions);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
