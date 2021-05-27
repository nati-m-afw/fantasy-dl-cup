import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    myTeam: {
      goalkeeper: [null, null],
      defender: [null, null, null],
      midfielder: [null, null, null],
      striker: [null, null],
    },
    userId: 1,
  },
  mutations: {
    updateMyTeam(state, myTeamUpdate) {
      state.myTeam = myTeamUpdate;
      console.log("Store--> MyTeam Updated Successfully!");
    }
  },
  actions: {},
  modules: {},
});
