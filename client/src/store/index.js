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
    myTeamName: 'Replace With Actual Team Name',
    userId: null,
  },
  mutations: {
    updateMyTeam(state, myTeamUpdate) {
      state.myTeam = myTeamUpdate;
      console.log("Store--> MyTeam Updated Successfully!");
    },

    updateMyTeamName(state, newTeamName) {
      state.myTeam = newTeamName;
      console.log("Store--> Team Name Updated Successfully!");
    },

    // Updater for User ID (AUTH)
    setCurrentUserID(state, currentUserId) {
      state.userId = currentUserId;
      console.log("Store--> User ID Updated Successfully!");
    },
  },
  actions: {},
  modules: {},
});
