<template>
  <div class="sub-body">
    <h1 class="header-title">Fixitures</h1>
    <button
      class="schedule-button"
      @click="schedule_match"
      v-show="match_schedules.length < 1"
    >
      Schedule Matches
    </button>

    <div class="matches-display">
      <div class="edit-container" @click="set_visiblity" v-if="!showOption">
        <fa class="i" icon="edit" size="1x" />
      </div>
      <div class="matches-gameweek">{{ game_week }}</div>
      <div class="matches-date">{{ game_week_date }}</div>

      <div
        class="match"
        v-for="match_schedule in match_schedules"
        :key="match_schedule.id"
      >
        <div class="match-container">
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
  </div>
</template>

<script>
import axios from "axios";
let path = "http://localhost:5000/admin";

export default {
  name: "AdminDash",
  data() {
    return {
      showOption: "",
      match_schedules: "",
      new_match_schedules: "",
      class_name: "match-0",
      game_week: `Gameweek - 0`,
      current_game_week: 1,
      number_of_game_weeks: 3,
      game_week_date: "Date",
      teams: [],
    };
  },
  created: function () {
    this.get_schedule();
    this.get_teams();
  },
  methods: {
    // Function to show and hide
    set_visiblity: function () {
      this.showOption = !this.showOption;
    },
    // Function to schedule Matches
    schedule_match: function () {
      console.log("Scheduling");
    },
    // Function to get schedules from DB
    get_schedule: function () {
      axios
        .get(`${path}/schedule/${this.current_game_week}`)
        .then((response) => {
          this.match_schedules = response.data;
          this.game_week = `Gameweek - ${this.match_schedules[0].game_week}`;
          this.game_week_date = this.match_schedules[0].date;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    get_teams: function () {
      this.teams = [
        "Information Tech",
        "Mechanical",
        "Electrical",
        "Software Eng",
        "Chemical",
        "Biomedical",
      ];
    },
    // Function to find change and send update request
    create_schedule: function () {
      let changed_schedule = [];
      let times = document.querySelectorAll(".time-selection");
      let dates = document.querySelectorAll(".date-selection");
      let i = 0;
      let curr_schedule;
      while (i < times.length) {
        let curr_time = times[i].value;
        let curr_date = dates[i].value;
        if (curr_time != this.match_schedules[i].time) {
          curr_schedule = {
            id: this.match_schedules[i].id,
            time: curr_time,
            date: this.match_schedules[i].date,
            state: this.match_schedules[i].state,
            score: this.match_schedules[i].score,
          };
          changed_schedule.push(curr_schedule);
        } else if (curr_date != this.match_schedules[i].date) {
          curr_schedule.date = curr_date;
        }
        i++;
      }
      return changed_schedule;
    },

    // Function to set Updated Schedule
    set_schedule: function () {
      let changed_schedule = this.create_schedule();
      console.log(changed_schedule);
      axios
        .post(`${path}/schedule/update`, {
          match_schedules: changed_schedule,
        })
        .then(() => {
          this.get_schedule();
          this.showOption = false;
        })
        .catch((err) => {
          console.log(err);
        });
    },

    show: function (e) {
      console.log(e.target);
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
  },
};
</script>

<style scoped>
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
  width: fit-content;
  height: fit-content;
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
</style>
