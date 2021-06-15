<template>
  <div class="body">
    <nav>
      <h1>DL Cup Fantasy</h1>
    </nav>
    <navigation :activePage="'League'" />
    <section id="table_container">
      <table>
        <thead>
          <tr>
            <th></th>
            <th id="total" title="Total Points">Total Pts</th>
            <th id="current" title="Games Played">Current GW</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(team, index) in table" :key="index" :class="team.teamName == $store.state.myTeamName ? 'highlight' : ''">
						<td>{{ team.teamName }}</td>
						<td>{{ team.score.reduce( (a,b) => a + b, 0 ) }}</td>
						<td>{{ team.score[activeGameweek - 1] }}</td>
          </tr>
        </tbody>
        <tfoot></tfoot>
      </table>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import Navigation from "../components/Navigation.vue";
export default {
  data() {
		return {
			table: [],

      activeGameweek: "",
		}
	},

  components: {
    navigation: Navigation,
  },

  methods: {
    // Function to get access token
    get_access_token: function () {
      // Get Token from Local Storage
      let access_token = localStorage.getItem("token");

      // Prepare a header config
      let config = {
        headers: {
          Authorization: `Bearer ${access_token}`,
        },
      };
      return config;
    },

    getActiveGameweek() {
      let config = this.get_access_token();

      axios
        .get("http://localhost:5000/getactivegw", config)
        .then((res) => {
          this.activeGameweek = res.data.activeGW;
        })
        .catch((err) => console.error(err));
    },

    getGlobalLeague() {
      let config = this.get_access_token();

      axios.get("http://localhost:5000/globalleague", config)
      .then(res => {
				this.table = res.data.teams;
      });
    }
  },

  created(){
    this.getActiveGameweek();
    this.getGlobalLeague();
  }
};
</script>

<style scoped>
.highlight {
  background-color: gold;
}
</style>