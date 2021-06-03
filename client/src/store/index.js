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
    myTeamName: localStorage.getItem('team-name') || '',
    userId: localStorage.getItem('user-id') || null,
  },
  
  getters: {
    isAuthenticated(state) {
        return state.userId && state.userId != "undefined" ? true : false;
      }
  },

  mutations: {
    updateMyTeam(state, myTeamUpdate) {
      state.myTeam = myTeamUpdate;
      console.log("Store--> MyTeam Updated Successfully!");
    },

    setMyTeamName(state, newTeamName) {
      localStorage.setItem("team-name", newTeamName);
      console.log("Store--> Team Name Updated Successfully!");
    },

    // Updater for User ID (AUTH)
    setCurrentUserID(state, userId) {
      // update state
      localStorage.setItem("user-id", userId);
      console.log("Store--> User ID Updated Successfully!");
    },
  },
  actions: {},
  modules: {},
});
