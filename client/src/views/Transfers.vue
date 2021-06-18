<template>
  <div class="body">
    <player-stats-modal :player="playerModalInfo" v-if="showModal" @close="closeModal" />
    <nav>
      <h1>DL Cup Fantasy</h1>
    </nav>
    <navigation :activePage="'Transfers'" />
    <div id="info"></div>
    <alert :msg="alertMsg" v-if="showMsg" />
    <FlashMessage :position="'top'" style="position: relative; z-index: 10" />

    <!-- <pre>{{ $data }}</pre> -->
    <div id="team_selection">
      <div class="team">
        <div id="transfer_field">
          <div class="goalkeeper">
            <i></i>
            <!-- Render two placeholders -->
            <div
              v-for="i in [0, 1]"
              :key="i"
              class="player-details"
              :class="{ active: selected[0] == i && selected[1] == 'gk' }"
              @click="toggleActive($event, i, 'gk')"
            >
              <!-- Set selectedPlayerIndex when clicked -->
              <img
                v-if="myTeam.goalkeeper[i]"
                @click="getPlayers($event, i)"
                class="i"
                :src="
                  require('@/assets/img/jerseys/' +
                    myTeam.goalkeeper[i].department +
                    '.png')
                "
                alt=""
              />
              <div class="details">
                <span>GK</span>
                <!-- Check if any selected players in myTeam -->
                <p v-if="myTeam.goalkeeper[i]">
                  <!-- If so display name -->
                  {{ myTeam.goalkeeper[i].fname }}
                </p>
              </div>
            </div>
            <i></i>
          </div>
          <div class="defender">
            <!-- Render three placeholders -->
            <div
              v-for="i in [0, 1, 2]"
              :key="i"
              class="player-details"
              :class="{ active: selected[0] == i && selected[1] == 'df' }"
              @click="toggleActive($event, i, 'df')"
            >
              <img
                v-if="myTeam.defender[i]"
                @click="getPlayers($event, i)"
                class="i"
                :src="
                  require('@/assets/img/jerseys/' +
                    myTeam.defender[i].department +
                    '.png')
                "
                alt=""
              />
              <div class="details">
                <span>DEF</span>
                <!-- Check if any selected players in myTeam -->
                <p v-if="myTeam.defender[i]">
                  <!-- If so display name -->
                  {{ myTeam.defender[i].fname }}
                </p>
              </div>
            </div>
          </div>
          <div class="midfielder">
            <div
              v-for="i in [0, 1, 2]"
              :key="i"
              class="player-details"
              :class="{ active: selected[0] == i && selected[1] == 'md' }"
              @click="toggleActive($event, i, 'md')"
            >
              <img
                v-if="myTeam.midfielder[i]"
                @click="getPlayers($event, i)"
                class="i"
                :src="
                  require('@/assets/img/jerseys/' +
                    myTeam.midfielder[i].department +
                    '.png')
                "
                alt=""
              />
              <div class="details">
                <span>MID</span>
                <!-- Check if any selected players in myTeam -->
                <p v-if="myTeam.midfielder[i]">
                  <!-- If so display name -->
                  {{ myTeam.midfielder[i].fname }}
                </p>
              </div>
            </div>
          </div>
          <div class="striker">
            <i></i>
            <div
              v-for="i in [0, 1]"
              :key="i"
              class="player-details"
              :class="{ active: selected[0] == i && selected[1] == 'st' }"
              @click="toggleActive($event, i, 'st')"
            >
              <img
                v-if="myTeam.striker[i]"
                @click="getPlayers($event, i)"
                class="i"
                :src="
                  require('@/assets/img/jerseys/' +
                    myTeam.striker[i].department +
                    '.png')
                "
                alt=""
              />
              <div class="details">
                <span>ST</span>
                <!-- Check if any selected players in myTeam -->
                <p v-if="myTeam.striker[i]">
                  <!-- If so display name -->
                  {{ myTeam.striker[i].fname }}
                </p>
              </div>
            </div>
            <i></i>
          </div>
        </div>
      </div>
      <div class="sidebar">
        <!-- Show if server status is false or down -->
        <h2 v-if="!serverStatus">Server could not be reached.</h2>

        <h3>{{ myTeamName }}</h3>
        <div class="quick-info">
          <div>
            <span>{{
              selected[1] == "gk"
                ? "GK"
                : selected[1] == "df"
                ? "DEF"
                : selected[1] == "md"
                ? "MID"
                : selected[1] == "st"
                ? "ST"
                : "-"
            }}</span>
            <p></p>
          </div>
          <div>
            <p></p>
            <span>GW {{ activeGameweek }}</span>
          </div>
        </div>
        <div class="skewed">
          <div
            v-for="(player, index) in playersApi"
            :key="index"
            :class="checkSelected(player) ? 'disabled' : ''"
            class="player-options"
            @click="launchModal($event, player)"
          >
            <img
              @click="getPlayers($event, i)"
              class="i sidebar-img"
              :src="
                require('@/assets/img/jerseys/' + player.department + '.png')
              "
              alt=""
            />
            <p class="player-name">{{ player.fname }}</p>
            <button
              @click="addPlayer($event, player)"
              :disabled="checkSelected(player)"
              class="player-options-add"
            >
              Add
            </button>
          </div>
        </div>
        <div class="submit-button-container">
          <button @click="updateTeamApi" class="team-submit-button">
            Save
          </button>
        </div>
        <!-- <div class="skewed">
          <ul>
            <li
              v-for="(player, index) in playersApi"
              :key="index"
              :class="checkSelected(player) ? 'disabled' : ''"
            >
              <span>{{ player.fname }}</span>
              <span>{{ player.lname }}</span>
              <span>{{ player.position }}</span>
              <button
                @click="addPlayer($event, player)"
                :disabled="checkSelected(player)"
              >
                +
              </button>
            </li>
          </ul>
          <br />
          <button @click="updateTeamApi">SAVE</button>
        </div> -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Alert from "../components/Alert.vue";
import Navigation from "../components/Navigation.vue";
import PlayerStatsModal from "../components/PlayerStatsModal.vue";

export default {
  data() {
    return {
      myTeam: {
        goalkeeper: [],
        defender: [],
        midfielder: [],
        striker: [],
      },

      myTeamName: "",

      activeGameweek: "",

      alertMsg: "",

      showMsg: false,

      // Players from api based on position
      playersApi: [],

      // Server status Up == True
      serverStatus: true,

      // Player being replaced in myTeam.<position>
      selectedPlayerIndex: null,

      // Active player order number and playing position
      selected: [],

      // Team Limit Counter
      teamCounter: {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
      },

      showModal: false,

      playerModalInfo: "",
    };
  },

  components: {
    alert: Alert,
    navigation: Navigation,
    playerStatsModal: PlayerStatsModal,
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

    // gets active gameweek
    // calls getTeam
    getActiveGameweek() {
      let config = this.get_access_token();

      axios
        .get("http://localhost:5000/getactivegw", config)
        .then((res) => {
          this.activeGameweek = res.data.activeGW + 1;
          this.getTeam();
        })
        .catch((err) => console.error(err));
    },

    // Fetches user's team for the current gameweek from API
    getTeam() {
      let userId = this.$store.state.userId;
      let config = this.get_access_token();

      axios
        .get(
          "http://localhost:5000/getteam/" + userId + "/" + this.activeGameweek,
          config
        )
        .then((res) => {
          if (res.data.team == false && this.activeGameweek == 0) {
            this.alertMsg = "Gameweek has not started!";
            this.showMsg = true;
          } else if (res.data.team == false) {
            this.alertMsg = "No team for current GW in DB";
            this.showMsg = true;
          }
          for (const player of res.data.team) {
            this.myTeam[player.position].push(player);
            this.teamCounter[player.dept_id] += 1;
          }
          // this.myTeam = res.data.team
        })
        .catch((err) => console.error(err));
    },

    // Get players from API
    getPlayers(e, selectedPlayerIndex) {
      const position = e.path[2].className;
      // console.log(e.path);
      let config = this.get_access_token();

      axios
        .get("http://localhost:5000/getplayers/" + position, config)
        .then((res) => {
          this.playersApi = res.data.players;
          this.serverStatus = true;
          this.selectedPlayerIndex = selectedPlayerIndex;
        })
        .catch((err) => {
          this.serverStatus = false;
          console.error(err);
        });
    },

    // Add selected player to myTeam based on position
    addPlayer(e, player) {
      this.teamCounter[player.dept_id] += 1;
      // Check team limit
      if (this.teamCounter[player.dept_id] > 3) {
        this.teamCounter[player.dept_id] -= 1;
        this.flashMessage.error({
          message: "Can not pick more than three players from the same team!",
        });
        return;
      }
      player["status"] =
        this.myTeam[player.position][this.selectedPlayerIndex].status;
      this.$set(this.myTeam[player.position], this.selectedPlayerIndex, player);
    },

    // Check if player is in myTeam.<position>
    checkSelected(player) {
      let check = false;
      this.myTeam[player.position].filter(function (myPlayer) {
        if (myPlayer && myPlayer.id == player.id) check = true;
      });
      return check;
    },

    // Add active player to selected
    toggleActive(e, playerNo, playerPos) {
      this.$set(this.selected, 0, playerNo);
      this.$set(this.selected, 1, playerPos);
    },

    // Update team API
    updateTeamApi() {
      this.$store.commit("updateMyTeam", this.myTeam);

      const payload = {
        userId: this.$store.state.userId,
        team: [],
        gameweekId: this.activeGameweek,
      };

      console.log(this.$store.state.userId);

      // push player id into payload
      for (const position in this.$store.state.myTeam) {
        // payload.team[position] = [];
        for (const player of this.$store.state.myTeam[position]) {
          payload.team.push({
            playerId: player.id,
            status: player.status,
          });
        }
      }

      let config = this.get_access_token();

      // Send myTeam to api
      axios
        .post("http://localhost:5000/updateuserplayers", payload, config)
        .then(() => {
          this.isRegistered = true;
          this.msg = "Team Updated!";
          this.showMsg = true;
          this.$router.push("/myteam");
        })
        .catch((err) => {
          console.error(err);
          this.msg = "An error occured. Please try again!";
          this.showMsg = true;
        });
    },

    launchModal(e, player) {
      this.playerModalInfo = player;
      this.showModal = true;
    },

    closeModal() {
      this.showModal = false;
    },

    // Logout
    logout() {
      sessionStorage.removeItem("user-id");
      this.$store.commit("setCurrentUserID");
      this.$router.push("/");
    },
  },

  created() {
    this.myTeamName = this.$store.state.myTeamName;
    this.getActiveGameweek();
  },
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}

@import "../assets/css/styles.css";
@import "../assets/css/sidebar.css";

#team_selection img {
  width: 15vw;
  cursor: pointer;
}

#team_selection {
  padding: 2% 7%;
  display: grid;
  grid-template-columns: 3fr 1fr;
  grid-column-gap: 2rem;
}

#transfer_field {
  display: grid;
  grid-template-rows: repeat(4, 150px);
  grid-gap: 1rem;
  background-color: var(--secondary-color);
  background-image: url("../assets/img/fields/Field4.0.png");
  background-repeat: no-repeat;
  animation: rise 1s forwards;
}

@keyframes rise {
  0% {
    background-position: 50% -50%;
  }
  100% {
    background-position: 50%;
  }
}

#transfer_field > div {
  display: flex;
  justify-content: center;
}

#transfer_field > div > div > img {
  display: block;
}

#transfer_sidebar {
  background-color: white;
  display: flex;
}

div.disabled {
  pointer-events: none;
  opacity: 0.7;
}
.active {
  background-color: tomato;
  animation: pop 0.4s forwards;
  border-radius: 10%;
}

@keyframes pop {
  0% {
    margin: 0%;
  }
  100% {
    margin: 10px 10px 0;
  }
}

.active {
  background: url("../assets/img/epic_waves.jpg");
  border-radius: 10%;
}

.starting_team div,
.substitutes div {
  position: relative;
}

.player-details {
  position: relative;
  text-align: center;
}

.details {
  position: absolute;
  bottom: -10px;
  left: 0;
  right: 0;
  margin: 0 auto;
  text-align: center;
  width: 100px;
}

#team_selection .player-details img {
  width: 200px;
  cursor: pointer;
}

.details > span {
  display: block;
  background-color: var(--accent-color);
  color: var(--secondary-color);
}

.details > p {
  background-color: var(--secondary-color);
  color: var(--accent-color);
}

.player-options {
  display: grid;
  grid-template-columns: 20px 3fr 50px;
  grid-column-gap: 1em;
  padding: 0 10%;
  align-content: center;
  background: var(--secondary-color);
  margin-bottom: 5%;
  cursor: pointer;
}

.player-options * {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: montserrat-light;
  color: var(--primary-color);
}

.player-name {
  overflow-wrap: break-word;
  word-wrap: break-word;
}

.player-options button {
  font-family: futura-pt;
  /* border-radius: solid thin; */
  outline: none;
  border-top: none;
  border-bottom: none;
  background: var(--accent-color);
  color: var(--secondary-color);
}

#team_selection .sidebar-img {
  width: 50px !important;
}

.submit-button-container {
  position: relative;
  margin-top: 30px;
}

.team-submit-button {
  font-size: 1.5rem;
  letter-spacing: 0.8px;
  width: 100%;
  padding: 2% 0;
  margin-bottom: 10%;
  position: relative;
  border: 1px solid black;
  border-radius: 0 0 5px 5px;
  /* background: var(--primary-color); */
  color: var(--primary-color);
}

.team-submit-button:after {
  content: "";
  width: 100%;
  height: 5px;
  background: linear-gradient(
    40deg,
    #dc143c,
    #e22f72,
    #c071c7,
    #8d9fed,
    #78b0f6,
    #5ffbf1
  );
  background-size: 400%;
  position: absolute;
  /* z-index: -1; */
  top: 99%;
  left: 0;
  border-radius: inherit;
  animation: glimmer 20s infinite alternate;
}

.team-submit-button:active {
  transform: translateY(5px);
}

.team-submit-button:active:after {
  width: 0;
}

@keyframes glimmer {
  0% {
    background-position: 0;
  }
  100% {
    background-position: 100%;
  }
}
</style>
