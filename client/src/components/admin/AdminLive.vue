<template>
  <div class="sub-body">
    <FlashMessage :position="'top'"></FlashMessage>
    <h1 class="header-title">Gameweek {{ current_gameweek }}</h1>
    <div class="main-container">
      <div
        class="main-info"
        v-if="all_matches"
        v-bind:team_id="current_match.team"
        v-bind:opponent_id="current_match.opponent"
      >
        {{ teams[current_match.team - 1] }} vs
        {{ teams[current_match.opponent - 1] }}
      </div>

      <div class="players-main-container">
        <div class="team-main-container">
          <div class="player-info" v-for="player in team" :key="player.id">
            <div
              class="player-container"
              @click="get_scoring_system"
              v-bind:id="player.id"
            >
              <span class="player-position">{{ player.position }}</span
              >{{ player.fname }}
            </div>
            <div v-show="showScoring" class="scoring-form-container">
              <div class="left-scoring-container">
                <!-- Goals Scored -->
                <div
                  class="goals-scored-container"
                  v-if="current_player.goals_scored"
                >
                  <label for="goals-scored">Goals Scored:</label>
                  <input
                    type="number"
                    name="goals-scored"
                    v-model="current_goal_scored"
                  />
                </div>

                <!-- Goals Conceeded -->
                <div class="goals-conceeded-container" v-if="current_player">
                  <label for="goals-conceeded">Goals Conceeded:</label>
                  <input
                    type="number"
                    name="goals-conceeded"
                    v-model="current_goals_conceded"
                  />
                </div>

                <!-- Assists Provided -->
                <div class="assist-container">
                  <label for="assist">Assist:</label>
                  <input
                    type="number"
                    name="goals-conceeded"
                    v-model="assists_provided"
                  />
                </div>
              </div>
              <div class="right-scoring-container">
                <!--Minutes Played  -->
                <div class="minutes-played">
                  <label for="minutes-played">Minutes Played:</label>
                  <select name="minutes-played" v-if="minutes_played > 45">
                    <option value="45">1-45</option>
                    <option value="90" selected>46-90</option>
                  </select>

                  <select name="minutes-played" v-if="minutes_played <= 45">
                    <option value="45" selected>1-45</option>
                    <option value="90">46-90</option>
                  </select>
                </div>

                <!-- Yellow Cards -->
                <div class="yellow-card-container">
                  <label for="yellow-card">Yellow Card :</label>
                  <input
                    type="checkbox"
                    checked
                    name="yellow-card"
                    v-if="yellow_cards == 1"
                  />

                  <input
                    type="checkbox"
                    name="yellow-card"
                    v-if="yellow_cards == 0"
                  />
                </div>

                <!-- Red Cards -->
                <div class="red-card-container">
                  <label for="red-card">Red Card :</label>
                  <input
                    checked
                    type="checkbox"
                    name="yellow-card"
                    v-if="red_cards == 1"
                  />

                  <input
                    type="checkbox"
                    name="yellow-card"
                    v-if="red_cards == 0"
                  />
                </div>

                <button class="save" @click="save_data">Save</button>
              </div>
            </div>
          </div>
        </div>
        <div class="opponent-main-container">
          <div class="player-info" v-for="player in opponent" :key="player.id">
            <div
              class="player-container"
              v-bind:id="player.id"
              @click="get_scoring_system"
            >
              <span class="player-position">{{ player.position }}</span
              >{{ player.fname }}
            </div>
            <div v-show="showScoring" class="scoring-form-container">
              <div class="left-scoring-container">
                <!-- Goals Scored -->
                <div
                  class="goals-scored-container"
                  v-if="current_player.goals_scored"
                >
                  <label for="goals-scored">Goals Scored:</label>
                  <input
                    type="number"
                    name="goals-scored"
                    v-model="current_goal_scored"
                  />
                </div>

                <!-- Goals Conceeded -->
                <div class="goals-conceeded-container" v-if="current_player">
                  <label for="goals-conceeded">Goals Conceeded:</label>
                  <input
                    type="number"
                    name="goals-conceeded"
                    v-model="current_goals_conceded"
                  />
                </div>

                <!-- Assists Provided -->
                <div class="assist-container">
                  <label for="assist">Assist:</label>
                  <input
                    type="number"
                    name="goals-conceeded"
                    v-model="assists_provided"
                  />
                </div>
              </div>
              <div class="right-scoring-container">
                <!--Minutes Played  -->
                <div class="minutes-played">
                  <label for="minutes-played">Minutes Played:</label>
                  <select name="minutes-played" v-if="minutes_played > 45">
                    <option value="45">1-45</option>
                    <option value="90" selected>46-90</option>
                  </select>

                  <select name="minutes-played" v-if="minutes_played <= 45">
                    <option value="45" selected>1-45</option>
                    <option value="90">46-90</option>
                  </select>
                </div>

                <!-- Yellow Cards -->
                <div class="yellow-card-container">
                  <label for="yellow-card">Yellow Card :</label>
                  <input
                    type="checkbox"
                    checked
                    name="yellow-card"
                    v-if="yellow_cards == 1"
                  />

                  <input
                    type="checkbox"
                    name="yellow-card"
                    v-if="yellow_cards == 0"
                  />
                </div>

                <!-- Red Cards -->
                <div class="red-card-container">
                  <label for="red-card">Red Card :</label>
                  <input
                    checked
                    type="checkbox"
                    name="yellow-card"
                    v-if="red_cards == 1"
                  />

                  <input
                    type="checkbox"
                    name="yellow-card"
                    v-if="red_cards == 0"
                  />
                </div>

                <button class="save" @click="save_data">Save</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="navigation-container">
        <div class="previous-container" @click="get_prev_page">
          <fa
            class="i unclickable"
            size="1x"
            icon="arrow-circle-left"
            ref="prev_icon"
          />
        </div>
        <div class="next-container" @click="get_next_page">
          <fa class="i" size="1x" icon="arrow-circle-right" ref="next_icon" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
let path = "http://localhost:5000/admin";
export default {
  data() {
    return {
      // Keep track of current gameweek
      current_gameweek: "",
      // Keep track of all matches
      all_matches: [""],

      // Match info of the current page
      current_match: "",
      // team names
      teams: [],

      // Counter to display each detail on current page
      counter: 0,
      team_id: "",
      opponent_id: "",
      team: "",
      opponent: "",
      showScoring: "",
      current_player_id: "",
      current_player: "",
      // Keep track of each players Stat
      current_goal_scored: 0,
      current_goals_conceded: 0,
      assists_provided: 0,
      minutes_played: 0,
      yellow_cards: 0,
      red_cards: 0,
    };
  },
  async mounted() {
    // Get current gameweek
    await this.get_current_gameweek();
    // Get All Matches
    await this.get_all_matches();
    // Get Teams
    await this.get_teams();
    // Get Team IDs
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

    set_id: function () {
      let main_info = document.querySelectorAll(".main-info")[0];
      this.team_id = main_info.getAttribute("team_id");
      this.opponent_id = main_info.getAttribute("opponent_id");
    },
    handle_error: function (err) {
      // // 401 UnAuthorized
      // if (err.response.status == 401) {
      //   console.log("401 Error Handling");
      // }
      // // Tampered with JWT
      // else if (err.response.status == 422) {
      //   console.log("422 Error Handling");
      // }
      // // Non Admin Access
      // else if (err.response.status == 403) {
      //   console.log("403 Error Handling");
      // } else {
      //   console.log(err);
      // }
      console.log(err);
    },
    // Function to update score auto
    update_score: function (update_info) {
      axios
        .post(`${path}/score/${update_info.gameweek_id}`, { update_info })
        .then()
        .catch((err) => {
          console.log(err);
        });
    },
    // Function to save data after edit
    save_data: function () {
      let updated_stats = {
        player_id: this.current_player_id,
        gameweek_id: this.current_gameweek,
        goals_conceded: this.current_goals_conceded,
        goals_scored: this.current_goal_scored,
        assists_provided: this.assists_provided,
        minutes_played: this.minutes_played,
        yellow_cards: this.yellow_cards,
        red_cards: this.red_cards,
      };
      let config = this.get_access_token();
      axios
        .patch(
          `${path}/events/${this.current_gameweek}`,
          {
            updated_stats,
          },
          config
        )
        .then(() => {
          this.update_score(updated_stats);
          this.get_player_event();
          this.flashMessage.success({
            message: "Information Updated Successfully",
          });
        })
        .catch((err) => {
          this.handle_error(err);
        });
    },
    // Method for setting up score form for clicks
    get_scoring_system: function (e) {
      // Hide all other forms if showing
      let all_scoring_forms = document.querySelectorAll(
        ".scoring-form-container"
      );
      all_scoring_forms.forEach((scoring_form) => {
        scoring_form.classList.remove("show");
        scoring_form.classList.add("hide");
      });
      let target_elem_main;
      if (e.target.classList.contains("player-container")) {
        target_elem_main = e.target;
      } else {
        target_elem_main = e.target.parentElement;
      }
      this.current_player_id = parseInt(target_elem_main.getAttribute("id"));
      target_elem_main = target_elem_main.nextSibling;
      target_elem_main.classList.toggle("hide");
      target_elem_main.classList.toggle("show");
      this.get_player_event();
    },
    // Method to get current gameweek
    get_current_gameweek: function () {
      this.current_gameweek = 1;
    },
    // Method to get all matches
    get_all_matches: function () {
      let config = this.get_access_token();
      // Get Matches by ID
      axios
        .get(`${path}/schedule/${this.current_gameweek}`, config)
        .then((response) => {
          this.all_matches = response.data;
          this.current_match = this.all_matches[0];
          this.team_id = this.current_match.team;
          this.opponent_id = this.current_match.opponent;
          this.get_players(this.team_id, "team");
          this.get_players(this.opponent_id, "");
        })
        .catch((err) => {
          this.handle_error(err);
        });
    },
    // Method to get team names
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

    // Method to get players
    get_players: function (dept_id, state) {
      let config = this.get_access_token();
      axios
        .get(`${path}/players/${dept_id}`, config)
        .then((response) => {
          if (state == "team") {
            this.team = response.data.response_data;
          } else {
            this.opponent = response.data.response_data;
          }
        })
        .catch((err) => {
          this.handle_error(err);
        });
    },
    // Method to get player event info
    get_player_event: function () {
      let config = this.get_access_token();
      axios
        .get(`${path}/events/${this.current_player_id}`, config)
        .then((response) => {
          let data = response.data.response_data[0];
          this.current_player = data;
          this.current_goal_scored = data.goals_scored;
          this.current_goals_conceded = data.goals_conceded;
          this.assists_provided = data.assists_provided;
          this.minutes_played = data.minutes_played;
          this.yellow_cards = data.yellow_cards;
          this.red_cards = data.red_cards;
        })
        .catch((err) => {
          this.handle_error(err);
        });
    },

    // Function to get next page
    get_next_page: async function () {
      // If counter is at max
      if (this.counter == this.all_matches.length - 1) {
        this.$refs.next_icon.classList.add("unclickable");
      } else {
        this.counter++;
        // If next enable prev
        this.$refs.prev_icon.classList.remove("unclickable");
        // Get Players
        await (this.current_match = this.all_matches[this.counter]);
        this.set_id();
        this.get_players(this.team_id, "team");
        this.get_players(this.opponent_id, "");
        this.get_player_event();
      }
    },
    // Function to get prev page
    get_prev_page: async function () {
      // If counter is less than 1
      if (this.counter == 0) {
        this.$refs.prev_icon.classList.add("unclickable");
      } else {
        this.counter--;
        // If prev enable next
        this.$refs.next_icon.classList.remove("unclickable");
        this.current_match = this.all_matches[this.counter];
        this.set_id();
        this.get_players(this.team_id, "team");
        this.get_players(this.opponent_id, "");
        this.get_player_event();
      }
    },
  },
};
</script>

<style scoped>
/* Dynamic Class */
.hide {
  display: none !important;
}
.show {
  display: flex !important;
}
.unclickable {
  color: gray !important;
  cursor: auto;
  opacity: 0.55;
}
/* Dynamic Class */
.sub-body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  margin-bottom: 5%;
  padding-bottom: 5%;
}
.header-title {
  text-align: center;
  margin-top: 3%;
  font-family: "Poppins";
  letter-spacing: 2px;
}
.main-container {
  width: 87%;
  margin-left: auto;
  margin-right: auto;
  /* min-height: 120vh; */
  /* background-color: red; */
  overflow-y: auto;
  background-color: white;
  margin-top: 1%;
  padding: 3%;
}
.main-info {
  font-family: "Poppins";
  letter-spacing: 1.5px;
  text-align: center;
  font-size: 30px;
  font-weight: 600;
}
.edit {
  text-align: end;
  margin-top: 1%;
  margin-bottom: 1.5%;
}
.players-main-container {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 2%;
}

.team-main-container {
  width: 50%;
  display: flex;
  flex-direction: column;
  padding: 0 0 0 1%;
}
.opponent-main-container {
  width: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0 1% 0 0;
  margin-left: 0.5%;
}
.player-info {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.player-container {
  margin-top: 5%;
  width: 100%;
  display: flex;
  align-items: center;
  font-family: "SourceSans";
  font-size: 28px;
  letter-spacing: 1.2px;
  text-transform: capitalize;
  word-spacing: 8px;
  background-color: gainsboro;
  padding-left: 3%;
}
.player-position {
  font-family: "SourceSans";
  font-size: 16px;
  font-weight: bold;
  letter-spacing: 1px;
  text-transform: capitalize;
  min-width: 135px;
}
.scoring-form-container {
  /* background-color: red; */
  display: flex;
  padding: 2%;
  /* background-color: #9c27b0; */
}
.left-scoring-container {
  margin-right: 5%;
}
.right-scoring-container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin-top: auto;
  margin-bottom: auto;
}
.save {
  width: 65%;
  margin-left: 35%;
  margin-top: 15%;
  background-color: #9c27b0;
  padding-top: 0.25%;
  padding-bottom: 0.25%;
  font-family: "Poppins";
  font-size: 22px;
  color: rgba(255, 255, 255, 0.8);
  outline: none !important;
  border: none !important;
}
label {
  font-family: "SourceSans";
  font-weight: 300;
  font-size: 18px;
}

.goals-scored-container,
.goals-conceeded-container,
.assist-container,
.yellow-card-container,
.minutes-played-container,
.red-card-container {
  margin-top: 8%;
}
.goals-scored-container,
.goals-conceeded-container,
.assist-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-top: 8%;
}
.yellow-card-container,
.red-card-container,
.minutes-played-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
input {
  outline: none !important;
  border: 0.001px solid rgba(0, 0, 0, 0.35);
  margin-top: 1.5%;
  height: 26px;
  padding: 1% 5% 1% 5%;
  font-size: 18px;
}
input[type="number"] {
  width: 50%;
}

.navigation-container {
  width: 100%;
  margin-top: 6%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 3% 0 3%;
}
.i {
  width: 22px !important;
  height: auto;
  color: black;
}
</style>
