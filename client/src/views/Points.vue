<template>
  <div class="body">
    <nav>
      <h1>DL Cup Fantasy</h1>
    </nav>
    <navigation :activePage="'Points'" />
    <div id="info"></div>
    <alert :msg="alertMsg" v-if="showMsg" />
    <!-- <pre>{{ $data }}</pre> -->
    <div id="team_selection">
      <div class="team">
        <div class="starting_team">
          <!-- GK -->
          <div class="goalkeeper">
            <div
              v-for="(player, i) in myTeam.goalkeeper.filter(
                (player) => player.status == 'active'
              )"
              :key="i"
              class="player-details"
            >
              <img
                :src="
                  require('@/assets/img/jerseys/' + player.department + '.png')
                "
                alt=""
              />
              <div class="details">
                <span>{{ player.score }}</span>
                <p>{{ player.fname }}</p>
              </div>
            </div>
          </div>
          <!-- DEF -->
          <div class="defender">
            <div
              v-for="(player, i) in myTeam.defender.filter(
                (player) => player.status == 'active'
              )"
              :key="i"
              class="player-details"
            >
              <img
                :src="
                  require('@/assets/img/jerseys/' + player.department + '.png')
                "
                alt=""
              />
              <div class="details">
                <span>{{ player.score }}</span>
                <p>{{ player.fname }}</p>
              </div>
            </div>
          </div>
          <!-- MID -->
          <div class="midfielder">
            <div
              v-for="(player, i) in myTeam.midfielder.filter(
                (player) => player.status == 'active'
              )"
              :key="i"
              class="player-details"
            >
              <img
                :src="
                  require('@/assets/img/jerseys/' + player.department + '.png')
                "
                alt=""
              />
              <div class="details">
                <span>{{ player.score }}</span>
                <p>{{ player.fname }}</p>
              </div>
            </div>
          </div>
          <!-- ST -->
          <div class="striker">
            <div
              v-for="(player, i) in myTeam.striker.filter(
                (player) => player.status == 'active'
              )"
              :key="i"
              class="player-details"
            >
              <img
                :src="
                  require('@/assets/img/jerseys/' + player.department + '.png')
                "
                alt=""
              />
              <div class="details">
                <span>{{ player.score }}</span>
                <p>{{ player.fname }}</p>
              </div>
            </div>
          </div>
        </div>
        <!-- SUB -->
        <div class="substitutes">
          <div class="reserve-goalkeeper">
            <!-- SUB GK -->
            <div
              v-for="(player, i) in myTeam.goalkeeper.filter(
                (player) => player.status == 'bench'
              )"
              :key="i"
              class="player-details"
            >
              <img
                :src="
                  require('@/assets/img/jerseys/' + player.department + '.png')
                "
                alt=""
              />
              <div class="details">
                <span>{{ player.score }}</span>
                <p>{{ player.fname }}</p>
              </div>
            </div>
          </div>

          <div class="reserve-outfield">
            <!-- SUB Players -->
            <div
              v-for="(player, i) in benchedPlayers"
              :key="i"
              class="player-details"
            >
              <img
                :src="
                  require('@/assets/img/jerseys/' + player.department + '.png')
                "
                alt=""
              />
              <div class="details">
                <span>{{ player.score }}</span>
                <p>{{ player.fname }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="sidebar">
        <h3>{{ myTeamName }}</h3>
        <div class="quick-info">
          <div>
            <span>{{ gameweekScore || "-" }}</span>
            <p>points</p>
          </div>
          <div>
            <p>Active GW</p>
            <select
              name="gameweek"
              id="gameweek"
              v-model="selectedGameweek"
              @change="getTeam"
            >
              <!-- <option v-for="i in availabeGameweeks" :key="i" value="i">GW {{ i }}</option> -->
              <!-- Show options if earlier or on the active gameweek -->
              <option value="1" v-if="this.activeGameweek >= 1">
                Gameweek 1
              </option>
              <option value="2" v-if="this.activeGameweek >= 2">
                Gameweek 2
              </option>
              <option value="3" v-if="this.activeGameweek >= 3">
                Gameweek 3
              </option>
              <option value="4" v-if="this.activeGameweek >= 4">
                Gameweek 4
              </option>
              <option value="5" v-if="this.activeGameweek >= 5">
                Gameweek 5
              </option>
            </select>
          </div>
        </div>
        <div class="skewed"></div>
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

      selectedGameweek: "",

      alertMsg: "",

      showMsg: false,
    };
  },

  computed: {
    benchedPlayers() {
      return this.myTeam.defender
        .concat(this.myTeam.midfielder.concat(this.myTeam.striker))
        .filter((player) => player.status == "bench");
    },

    gameweekScore() {
      let score = 0;
      for (const position in this.myTeam) {
        for (const player of this.myTeam[position]) {
          if (player.status == "active") score += player.score;
        }
      }

      return score;
    },

    // Gameweeks played or currently active
    // availabeGameweeks() {
    //   return [1,2,3,4,5].filter(gw => gw <= this.activeGameweek);
    // }
  },

  components: {
    alert: Alert,
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
          // Set active gameweek
          this.activeGameweek = res.data.activeGW;
          // Set selected gameweek to current (activeGameweek)
          this.selectedGameweek = this.activeGameweek;
          this.getTeam();
        })
        .catch((err) => console.error(err));
    },

    getTeam() {
      let userId = this.$store.state.userId;

      // Clear myTeam
      this.myTeam = {
        goalkeeper: [],
        defender: [],
        midfielder: [],
        striker: [],
      };
      
      let config = this.get_access_token();
      
      axios
        .get(
          "http://localhost:5000/getteam/" + userId + "/" + this.selectedGameweek,
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
          }
          // this.myTeam = res.data.team

          // Get points
          this.getPoints();
        })
        .catch((err) => console.error(err));
    },

    getPoints() {
      let config = this.get_access_token();
      for (const position in this.myTeam) {
        for (const [index, player] of this.myTeam[position].entries()) {
          axios
            .get(
              "http://localhost:5000/score/" +
                player.id +
                "/" +
                this.selectedGameweek,
                config
            )
            .then((res) => {
              player["score"] = res.data.score || 0;
              this.$set(this.myTeam[position], index, player);
            });
        }
      }
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
  /* cursor: pointer; */
}

#team_selection {
  padding: 2% 7%;
  display: grid;
  grid-template-columns: 3fr 1fr;
  grid-column-gap: 2rem;
}

.team {
  display: grid;
  grid-row-gap: 5rem;
}

.starting_team {
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

.starting_team > div,
.substitutes > div {
  display: flex;
  justify-content: center;
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
  bottom: 10px;
  left: 0;
  right: 0;
  margin: 0 auto;
  text-align: center;
  width: 100px;
}

#team_selection .player-details img {
  width: 200px;
  /* cursor: pointer; */
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

.substitutes,
.reserve-outfield {
  display: flex;
}

.substitutes {
  justify-content: space-around;
}
</style>
