<template>
  <div class="body">
    <nav>
      <h1>DL Cup Fantasy</h1>
    </nav>
    <navigation :activePage="'Transfers'" />
    <div id="info"></div>
    <alert :msg="alertMsg" v-if="showMsg" />
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
        <h3>{{ myTeamName }}</h3>
        <div class="quick-info">
          <div>
            <span>{{ selected[1] == 'gk' ? "GK" : selected[1] == 'df' ? "DEF" :  selected[1] == 'md' ? "MID" : selected[1] == 'st' ? "ST" : "-"}}</span>
            <p></p>
          </div>
          <div>
            <p></p>
            <span>GW {{ activeGameweek }}</span>
          </div>
        </div>
        <div class="skewed">
          <!-- Show if server status is false or down -->
          <h2 v-if="!serverStatus">Server could not be reached.</h2>
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
          <br>
          <button @click="updateTeamApi">SAVE</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Alert from "../components/Alert.vue";
import Navigation from "../components/Navigation.vue";

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
    };
  },

  components: {
    alert: Alert,
    navigation: Navigation,
  },

  methods: {
    // gets active gameweek
    // calls getTeam
    getActiveGameweek() {
      axios
        .get("http://localhost:5000/getactivegw")
        .then((res) => {
          this.activeGameweek = res.data.activeGW + 1;
          this.getTeam();
        })
        .catch((err) => console.error(err));
    },

    // Fetches user's team for the current gameweek from API
    getTeam() {
      let userId = this.$store.state.userId;

      axios
        .get(
          "http://localhost:5000/getteam/" + userId + "/" + this.activeGameweek
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
          }
          // this.myTeam = res.data.team
        })
        .catch((err) => console.error(err));
    },

    // Get players from API
    getPlayers(e, selectedPlayerIndex) {
      const position = e.path[2].className;
      // console.log(e.path);

      axios
        .get("http://localhost:5000/getplayers/" + position)
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

      // Send myTeam to api
      axios
        .post("http://localhost:5000/updateuserplayers", payload)
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

    // Logout
    logout() {
      localStorage.removeItem("user-id");
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

.i {
  color: white;
  cursor: pointer;
}

#transfer_sidebar {
  background-color: white;
  display: flex;
}

li{
  list-style: none;
}

li.disabled {
  background-color: var(--secondary-color);
  color: black;
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

#team_selection img {
  width: 15vw;
  cursor: pointer;
}

.active {
  background-color: tomato;
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
</style>
