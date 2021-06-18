<template>
  <div class="sub-body">
    <!-- Flash Message Section -->
    <FlashMessage :position="'top'"></FlashMessage>
    <!-- Flash Message Section -->

    <!-- Title Header -->
    <h1 class="header-title">Fixitures</h1>
    <!-- Title Header -->

    <!-- Button To Generate Matches -->
    <button
      class="schedule-button"
      @click="schedule_match"
      v-show="match_schedules.length < 1"
    >
      Schedule Matches
    </button>
    <!-- Button To Generate Matches -->

    <!-- Spinner Display -->
    <spinner v-show="dataLoaded == false"></spinner>
    <!-- Spinner Display -->

    <!-- Match Info Section -->
    <div class="matches-display" v-show="dataLoaded">
      <!-- Edit Button Section -->
      <div
        class="edit-container"
        @click="set_visiblity"
        v-show="!showOption && !allPlayed"
      >
        <fa class="i" icon="edit" size="1x" />
      </div>
      <!-- Edit Button Section -->

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

          <!-- Options Container-Menu -->
          <div
            class="options-container"
            v-if="showOption && match_schedule.state == 0"
          >
            <div class="time-container">
              <label for="time-selection" class="label">Kick Off Time</label>
              <select v-bind:value="match_schedule.time" class="time-selection">
                <option value="12:00">12:00</option>
                <option value="13:00">13:00</option>
                <option value="14:00">14:00</option>
                <option value="15:00">15:00</option>
                <option value="16:00">16:00</option>
                <option value="17:00">17:00</option>
                <option value="18:00">18:00</option>
              </select>
            </div>

            <div class="date-container">
              <label for="date" class="label">Kick Off Date</label>
              <input
                type="date"
                name="date"
                v-bind:value="match_schedule.date"
                class="date-selection"
              />
            </div>
          </div>
          <!-- Options Container-Menu -->
        </div>
      </div>

      <button v-if="showOption" @click="set_schedule" class="save-button">
        Save
      </button>

      <div class="navigation-container">
        <div
          class="navigation-prev"
          @click="prev_game_week"
          ref="previous_text"
        >
          <fa class="i" icon="arrow-circle-left" ref="prev_icon" size="1x" />
        </div>
        <div class="navigation-next" @click="next_game_week">
          <fa class="i" icon="arrow-circle-right" size="1x" ref="next_icon" />
        </div>
      </div>
    </div>
    <div class="gameweek-buttons">
      <button class="end-gameweek" @click="end_gameweek">End Gameweek</button>
      <button class="start-gameweek" @click="start_gameweek">
        Start Gameweek
      </button>
    </div>
    <!-- Display Section -->
  </div>
</template>

<script>
// Imports
import axios from "axios";
let path = "http://localhost:5000/admin";
import Spinner from "../Spinner.vue";

export default {
  name: "AdminDash",

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
    };
  },

  components: {
    spinner: Spinner,
  },
  created: async function () {
    // Get Schedule on Load
    await this.get_schedule();

    // Get Teams on Load
    await this.get_teams();
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

    // Function to show and hide
    set_visiblity: function () {
      this.showOption = !this.showOption;
    },

    // Function to check if all are played
    check_state: function () {
      for (let i = 0; i < this.match_schedules.length; i++) {
        // If One unplayed allow Edit
        if (this.match_schedules[i].state == 0) {
          this.allPlayed = false;
          break;
        }
      }
    },

    // Function to get team names
    get_teams: function () {
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
          this.handle_error(err);
        });
    },
    // Function to Generate Matches when no matches exsist
    schedule_match: function () {
      let config = this.get_access_token();

      axios
        .get(`${path}/matches`, config)
        .then(() => {
          this.get_schedule();
          this.flashMessage.success({
            message: "Matches Generated Succesfully",
          });
        })
        .catch((err) => {
          this.handle_error(err)
        });
    },
    // Function to get schedules from DB
    get_schedule: function () {
      // Get Access Token
      let config = this.get_access_token();
      axios
        .get(`${path}/schedule/${this.current_game_week}`, config)
        .then((response) => {
          this.match_schedules = response.data;
          this.game_week = `Gameweek - ${this.match_schedules[0].game_week}`;
          this.game_week_date = this.match_schedules[0].date;
          this.check_state();
          if (this.match_schedules.length >= 1) {
            this.noData = true;
          }
          this.dataLoaded = true;
        })
        .catch((err) => {
          this.handle_error(err);
        });
    },
    // Function to find change and send update request
    create_schedule: function () {
      // Empty New Schedule Array
      let changed_schedule = [];
      let times = document.querySelectorAll(".time-selection");
      let dates = document.querySelectorAll(".date-selection");

      // Iterate through Times
      for (let i = 0; i < times.length; i++) {
        // If No Change Time and date change
        if (
          times[i].value == this.match_schedules[i].time &&
          dates[i].value == this.match_schedules[i].date
        ) {
          continue;
        } else {
          let current_schedule = {
            id: this.match_schedules[i].id,
            time: times[i].value,
            date: dates[i].value,
          };
          // Append to final array
          changed_schedule.push(current_schedule);
        }
      }
      return changed_schedule;
    },

    // Function to set Updated Schedule
    set_schedule: function () {
      let changed_schedule = this.create_schedule();

      let config = this.get_access_token();
      axios
        .patch(
          `${path}/schedule/1`,
          {
            match_schedules: changed_schedule,
          },
          config
        )
        .then(() => {
          // REPLACE WITH NOTIFICATION
          this.flashMessage.success({
            message: "Match Info Updated Succesfully",
          });
          this.get_schedule();
          this.showOption = false;
        })
        .catch((err) => {
          this.handle_error(err);
        });
    },

    // Function to get next game week
    next_game_week: function () {
      // If max gameweek number
      if (this.current_game_week > this.number_of_game_weeks) {
        // Gray Out Icon for next
        this.$refs.next_icon.classList.add("unclickable");
        // Enable Next Icon
        this.$refs.prev_icon.classList.remove("unclickable");
      } else {
        //  Increment game_week_value
        this.current_game_week++;
        // Call function to get schedule
        this.get_schedule();
        this.$refs.prev_icon.classList.remove("unclickable");
      }
    },

    prev_game_week: function () {
      if (this.current_game_week > 1) {
        this.$refs.prev_icon.classList.remove("unclickable");
        this.current_game_week--;
        this.get_schedule();
        this.$refs.next_icon.classList.remove("unclickable");
      } else {
        this.$refs.prev_icon.classList.add("unclickable");
      }
    },
    // End Gameweek
    end_gameweek: function () {
      let config = this.get_access_token();
      axios.patch(`${path}/gameweek`, config).then(() => {
        this.flashMessage.success({
          message: `Gameweek ${this.game_week} ended.`,
        });
      });
    },
    start_gameweek: function () {
      let config = this.get_access_token();
      axios.put(`${path}/gameweek`, config).then(() => {
        this.flashMessage.success({
          message: `Gameweek started.`,
        });
      });
    },

     handle_error: function (err) {
      // 401 UnAuthorized or 
      // Tampered with JWT
      if (err.response.status == 401 || err.response.status == 422)   {
        sessionStorage.clear()
        location.reload()
      }
    
      // Non Admin Access
      else if (err.response.status == 403) {
        sessionStorage.clear()
        location.reload()
        this.flashMessage.warning({message:"Error You is not an Admin"})
      } else {
        console.log(err)
      }
    },
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
.gameweek-buttons {
  margin-top: 5%;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  width: 40%;
  margin-left: auto;
  margin-right: auto;
}
.gameweek-buttons button {
  outline: none !important;
  padding: 0.75% 2% 0.75% 2%;
  font-size: 20px;
}
</style>
