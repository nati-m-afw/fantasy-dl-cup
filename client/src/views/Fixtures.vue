<template>
  <div class="body">
    <nav>
      <h1>DL Cup Fantasy</h1>
    </nav>
    <navigation :activePage="'Fixtures'" />

    <!-- GW Selector -->
    <div class="gw-select">
      <p>Active GW</p>
      <select
        name="gameweek"
        id="gameweek"
        v-model="selectedGameweek"
        @change="get_schedule"
      >
        <!-- <option v-for="i in availabeGameweeks" :key="i" value="i">GW {{ i }}</option> -->
        <!-- Show options if earlier or on the active gameweek -->
        <option value="1">Gameweek 1</option>
        <option value="2">Gameweek 2</option>
        <option value="3">Gameweek 3</option>
        <option value="4">Gameweek 4</option>
        <option value="5">Gameweek 5</option>
      </select>
    </div>
    <!-- GW Selector -->

    <!-- Match Info Section -->
    <div class="matches-display" v-show="dataLoaded">
      <!-- Gameweek and Date Section -->
      <div class="matches-gameweek">{{ game_week }}</div>
      <div class="matches-date">{{ game_week_date }}</div>
      <!-- Gameweek and Date Section -->

      <!-- Display Section -->

      <div
        class="match"
        v-for="match_schedule in match_schedules"
        :key="match_schedule.id"
      >
        <div class="match-container">
          <!-- Match Info Section -->
          <div class="match-info">
            <div class="match-team-one">
              {{ teams[match_schedule.team - 1] }}
            </div>
            <!-- Show Time if match is not played -->
            <div class="match-time" v-if="match_schedule.state == 0">
              {{ match_schedule.time }}
            </div>

            <!-- Show Score if match is played -->
            <div class="match-time" v-if="match_schedule.state == 1">
              {{ match_schedule.score }}
            </div>

            <div class="match-team-two">
              {{ teams[match_schedule.opponent - 1] }}
            </div>
          </div>
          <!-- Match Info Section -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Navigation from "../components/Navigation.vue";
let path = "http://localhost:5000";

export default {
  data() {
    return {
      dataLoaded: false,
      allPlayed: true,
      showOption: "",
      match_schedules: "",
      class_name: "match-0",
      game_week: `Gameweek - 0`,
      current_game_week: 1,
      current_game_week_info: [],
      number_of_game_weeks: "",
      game_week_date: "Date",
      teams: [],

      selectedGameweek: "",
    };
  },

  components: {
    navigation: Navigation,
  },

  methods: {
    // Function to get access token
    get_access_token: function () {
      // Get Token from Local Storage
      let access_token = sessionStorage.getItem("token");

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
          this.selectedGameweek = res.data.activeGW;
          this.get_schedule();
        })
        .catch((err) => console.error(err));
    },

    // Function to get team names
    get_teams() {
      let config = this.get_access_token();
      axios
        .get(`${path}/teams`, config)
        .then((response) => {
          // Load Team Names
          for (let i = 0; i < response.data.length; i++) {
            this.teams.push(response.data[i].team_name);
          }
          this.number_of_game_weeks = this.teams.length - 2;
        })
        .catch((err) => {
          console.error(err);
        });
    },

    // Function to get schedules from DB
    get_schedule() {
      // Get Access Token
      let config = this.get_access_token();
      axios
        .get(`${path}/schedule/${this.selectedGameweek}`, config)
        .then((response) => {
          this.match_schedules = response.data.response_data;
          this.game_week = `Gameweek - ${this.selectedGameweek}`;
					if (this.match_schedules.length == 0) return;
          this.game_week_date = this.match_schedules[0].date;
          if (this.match_schedules.length >= 1) {
            this.noData = true;
          }
          this.dataLoaded = true;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },

  created() {
    this.getActiveGameweek();
		this.get_teams();
  },
};
</script>

<style scoped>
select,
option {
  background-color: unset;
  color: unset;
}
/* Dynamic Classes */
.unclickable {
  cursor: auto !important;
  color: gray !important;
}

/* Dynamic Classes */
.sub-body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  margin-bottom: 5%;
}
.header-title {
  font-family: "Poppins";
  letter-spacing: 3px;
  text-align: center;
  margin-top: 4%;
  margin-bottom: 5%;
}
.edit-container {
  text-align: end;
}
.i {
  color: black;
  width: 22px;
  height: auto;
}
.schedule-button {
  width: 18%;
  padding-top: 0.5%;
  padding-bottom: 0.5%;
  height: fit-content;
  font-family: "Poppins";
  letter-spacing: 2px;
  font-size: 18px;
  margin-right: 10%;
  margin-left: auto;
  margin-bottom: 5%;
  background-color: #852795;
  border: 1px solid #852795;
  color: rgba(255, 255, 255, 0.719);
  outline: none;
}
.matches-display {
  width: 80%;
  padding: 2%;
  margin-left: 10%;
  margin-right: 10%;
  min-height: 48vh;
  box-shadow: 0 1px 4px 0 rgb(255 255 255 / 14%);
  color: #333;
  background: #fff;
  border-radius: 25px;
}
.matches-gameweek {
  text-align: center;
  font-family: "Poppins";
  font-size: 26px;
  margin-top: 0;
  margin-bottom: 2%;
  letter-spacing: 1px;
  font-weight: 700;
}
.matches-date {
  text-align: center;
  margin-bottom: 4%;
  font-family: "Poppins";
  font-size: 22px;
  background-color: gainsboro;
}
.match-info {
  background-color: rgba(220, 220, 220, 0.568);
  margin-top: 2.5%;
  padding: 0.4% 18% 0.4% 18%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.no-data-display {
  text-align: center;
  margin-top: 8%;
  margin-bottom: 8%;
}
.match-team-one,
.match-team-two {
  font-family: "Poppins";
  font-size: 20px;
  min-width: 200px;
  letter-spacing: 0.5px;
}
.match-team-one {
  text-align: end;
}
.match-team-two {
  text-align: start;
}
.match-time {
  font-family: "SourceSans";
  font-size: 26px;
  font-weight: 700;
}
.options-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-left: 10%;
  padding-right: 10%;
  padding-top: 1%;
  padding-bottom: 1%;
}
.label {
  font-family: "Poppins";
  margin-bottom: 2%;
}
.time-container,
.date-container {
  display: flex;
  flex-direction: column;
}
input,
select {
  font-family: "Poppins";
  font-size: 18px;
  margin-top: 1%;
  font-weight: 300;
  outline: none !important;
  font-style: italic;
}
.save-button {
  width: 12%;
  margin-left: 88%;
  margin-top: 3%;
  background-color: #9c27b0;
  padding-top: 0.25%;
  padding-bottom: 0.25%;
  font-family: "Poppins";
  font-size: 22px;
  color: rgba(255, 255, 255, 0.8);
  outline: none !important;
  border: none !important;
}
.save-button:hover {
  background-color: #852795;
}
.navigation-container {
  margin-top: 5%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-left: 5%;
  padding-right: 5%;
}
.navigation-prev,
.navigation-next {
  cursor: pointer;
}

.gw-select{
	margin: 0 13vw;
}
.gw-select p{
	margin: 0;
}
</style>