<template>
  <div class="sub-body">
    <h1 class="header-title">Gameweek Fix</h1>
    <div class="main-container">
      <div class="main-info" v-if="all_matches">
        {{ teams[current_match.team - 1] }} vs
        {{ teams[current_match.opponent - 1] }}
      </div>
      <div class="edit" @click="edit" v-show="!showScoring">
        <fa class="i" icon="edit" size="1x" />
      </div>
      <div class="players-main-container">
        <div class="team-main-container">
          <div class="player-info" v-for="player in team" :key="player.id">
            <div class="player-container" @click="edit_2" v-bind:id="player.id">
              <span class="player-position">{{ player.position }}</span
              >{{ player.fname }}
            </div>
            <div v-show="showScoring" class="scoring-form-container">
              <div class="left-scoring-container">
                <!-- Goals Scored -->
                <div class="goals-scored-container">
                  <label for="goals-scored">Goals Scored:</label>
                  <input
                    type="number"
                    name="goals-scored"
                    v-bind:value="current_player[0]"
                  />
                </div>

                <!-- Goals Conceeded -->
                <div class="goals-conceeded-container" v-if="current_player">
                  <label for="goals-conceeded">Goals Conceeded:</label>
                  <input
                    type="number"
                    name="goals-conceeded"
                    v-bind:value="current_player[1]"
                  />
                </div>

                <!-- Assists Provided -->
                <div class="assist-container">
                  <label for="assist">Assist:</label>
                  <input
                    type="number"
                    name="goals-conceeded"
                    v-bind:value="current_player[2]"
                  />
                </div>
              </div>
              <div class="right-scoring-container">
                <!--Minutes Played  -->
                <div class="minutes-played">
                  <label for="minutes-played">Minutes Played:</label>
                  <select
                    name="minutes-played"
                    id=""
                    v-if="current_player[3] > 45"
                  >
                    <option value="45">1-45</option>
                    <option value="90" selected>46-90</option>
                  </select>

                  <select
                    name="minutes-played"
                    id=""
                    v-if="current_player[3] <= 45"
                  >
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
                    v-if="current_player[4] == 1"
                  />

                  <input
                    type="checkbox"
                    name="yellow-card"
                    v-if="current_player[4] == 0"
                  />
                </div>

                <!-- Red Cards -->
                <div class="red-card-container">
                  <label for="red-card">Red Card :</label>
                  <input
                    checked
                    type="checkbox"
                    name="yellow-card"
                    v-if="current_player[5] == 1"
                  />

                  <input
                    type="checkbox"
                    name="yellow-card"
                    v-if="current_player[5] == 0"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="opponent-main-container">
          <div class="player-info" v-for="player in opponent" :key="player.id">
            <div class="player-container" v-bind:id="player.id" @click="edit_2">
              <span class="player-position">{{ player.position }}</span
              >{{ player.fname }}
            </div>
            <div v-show="showScoring" class="scoring-form-container">
              <div class="left-scoring-container">
                <!-- Goals Scored -->
                <div class="goals-scored-container">
                  <label for="goals-scored">Goals Scored:</label>
                  <input
                    type="number"
                    name="goals-scored"
                    v-bind:value="current_player[0]"
                  />
                </div>

                <!-- Goals Conceeded -->
                <div class="goals-conceeded-container" v-if="current_player">
                  <label for="goals-conceeded">Goals Conceeded:</label>
                  <input
                    type="number"
                    name="goals-conceeded"
                    v-bind:value="current_player[1]"
                  />
                </div>

                <!-- Assists Provided -->
                <div class="assist-container">
                  <label for="assist">Assist:</label>
                  <input
                    type="number"
                    name="goals-conceeded"
                    v-bind:value="current_player[2]"
                  />
                </div>
              </div>
              <div class="right-scoring-container">
                <!--Minutes Played  -->
                <div class="minutes-played">
                  <label for="minutes-played">Minutes Played:</label>
                  <select
                    name="minutes-played"
                    id=""
                    v-if="current_player[3] > 45"
                  >
                    <option value="45">1-45</option>
                    <option value="90" selected>46-90</option>
                  </select>

                  <select
                    name="minutes-played"
                    id=""
                    v-if="current_player[3] <= 45"
                  >
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
                    v-if="current_player[4] == 1"
                  />

                  <input
                    type="checkbox"
                    name="yellow-card"
                    v-if="current_player[4] == 0"
                  />
                </div>

                <!-- Red Cards -->
                <div class="red-card-container">
                  <label for="red-card">Red Card :</label>
                  <input
                    checked
                    type="checkbox"
                    name="yellow-card"
                    v-if="current_player[5] == 1"
                  />

                  <input
                    type="checkbox"
                    name="yellow-card"
                    v-if="current_player[5] == 0"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <button @click="save_data" class="save" v-show="showScoring">Save</button>
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
      current_gameweek: "",
      all_matches: [""],
      current_match: "",
      teams: [],
      counter: 0,
      team_id: "",
      opponent_id: "",
      team: "",
      opponent: "",
      showScoring: "",
      current_player_id: "",
      current_player: "",
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
    edit_2: function (e) {
      let target_elem_main;
      if (e.target.classList.contains("player-container")) {
        target_elem_main = e.target;
      } else {
        target_elem_main = e.target.parentElement;
      }
      this.current_player_id = target_elem_main.getAttribute("id");
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
      axios
        .get(`${path}/schedule/${this.current_gameweek}`)
        .then((response) => {
          this.all_matches = response.data;
          this.current_match = this.all_matches[0];
          this.team_id = this.current_match.team;
          this.opponent_id = this.current_match.opponent;
          this.get_players(this.team_id, "team");
          this.get_players(this.opponent_id, "");
        })
        .catch((err) => {
          console.log(err);
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
    edit: function (e) {
      let target_elem_main;
      if (e.target.classList.contains("player-container")) {
        target_elem_main = e.target;
      } else {
        target_elem_main = e.target.parentElement;
      }
      console.log(target_elem_main.getAttribute("id"));
      this.showScoring = true;
    },
    save_data: function () {
      this.showScoring = false;
    },
    set_id: function () {
      this.team_id = this.current_match.team;
      this.opponent_id = this.current_match.opponent;
      console.log(this.team_id);
    },

    // Method to get players
    get_players: function (dept_id, state) {
      axios
        .get(`${path}/players/${dept_id}`)
        .then((response) => {
          if (state == "team") {
            this.team = response.data;
          } else {
            this.opponent = response.data;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },

    // Method to get player event info
    get_player_event: function () {
      console.log("Data for " + this.current_player_id);
      this.current_player = ["2", "2", "1", "75", "1", "0"];
      console.log(this.current_player);
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
  color: red !important;
  cursor: auto;
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
  padding: 0 0 0 5%;
}
.opponent-main-container {
  width: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0 5% 0 0;
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
}
.left-scoring-container {
  /* background-color: green; */
  margin-right: 5%;
}
.right-scoring-container {
  /* background-color: purple; */
  margin-top: auto;
  margin-bottom: auto;
}
label {
  font-family: "SourceSans";
  font-weight: 300;
  font-size: 18px;
}
label[type="number"] {
  background-color: red;
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
.assist-container,
.minutes-played-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-top: 8%;
}
.yellow-card-container,
.red-card-container {
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
.save {
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
.navigation-container {
  width: 100%;
  background-color: aqua;
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
