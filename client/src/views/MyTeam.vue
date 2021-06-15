<template>
  <div class="body">
    <nav>
      <h1>DL Cup Fantasy</h1>
    </nav>
    <navigation :activePage="'MyTeam'" />
    <div id="info"></div>
    <!-- <pre>{{ $data }}</pre> -->
    <alert :msg="msg" v-if="showMsg" />
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
              :class="{
                active: selected[0] == i && selected[1] == 'goalkeeper',
              }"
              @click="toggleActive($event, i, 'goalkeeper', player.id)"
            >
              <img
                :src="
                  require('@/assets/img/jerseys/' + player.department + '.png')
                "
                alt=""
              />
              <div class="details">
                <span>GK</span>
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
              :class="{ active: selected[0] == i && selected[1] == 'defender' }"
              @click="toggleActive($event, i, 'defender', player.id)"
            >
              <img
                :src="
                  require('@/assets/img/jerseys/' + player.department + '.png')
                "
                alt=""
              />
              <div class="details">
                <span>DEF</span>
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
              :class="{
                active: selected[0] == i && selected[1] == 'midfielder',
              }"
              @click="toggleActive($event, i, 'midfielder', player.id)"
            >
              <img
                :src="
                  require('@/assets/img/jerseys/' + player.department + '.png')
                "
                alt=""
              />
              <div class="details">
                <span>MID</span>
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
              :class="{ active: selected[0] == i && selected[1] == 'striker' }"
              @click="toggleActive($event, i, 'striker', player.id)"
            >
              <img
                :src="
                  require('@/assets/img/jerseys/' + player.department + '.png')
                "
                alt=""
              />
              <div class="details">
                <span>ST</span>
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
                <span>GK</span>
                <p>{{ player.fname }}</p>
                <span v-if="selected[1] == 'goalkeeper'">
                  <button
                    @click="changePlayer($event, player.id, player.position)"
                  >
                    <fa icon="exchange-alt" />
                  </button>
                </span>
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
                <span>{{ player.position }}</span>
                <p>{{ player.fname }}</p>
                <span v-if="selected[1] != 'goalkeeper' && selected[1]">
                  <button
                    @click="changePlayer($event, player.id, player.position)"
                  >
                    <fa icon="exchange-alt" />
                  </button>
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="sidebar">
        <h3>{{ myTeamName }}</h3>
        <div class="quick-info">
          <div>
            <span>07:00</span>
            <p>Deadline</p>
          </div>
          <div>
            <p></p>
            <span>GW {{ activeGameweek }}</span>
          </div>
        </div>
        <div class="skewed">
          <button @click="updateTeamApi">SAVE</button>
        </div>
      </div>
      <br />
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
      // Player being replaced in myTeam.<position>
      selectedPlayerIndex: null,

      // Active player order number and playing position
      selected: [],

      msg: "",

      showMsg: false,
    };
  },

  computed: {
    benchedPlayers() {
      return this.myTeam.defender
        .concat(this.myTeam.midfielder.concat(this.myTeam.striker))
        .filter((player) => player.status == "bench");
    },
  },

  components: {
    alert: Alert,
    navigation: Navigation,
  },

  methods: {
    // Get Access token
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
          // Team Selection for the coming Gameweek
          this.activeGameweek = res.data.activeGW + 1;
          this.getTeam();
        })
        .catch((err) => console.error(err));
    },

    // Get user Team API
    getTeam() {
      let userId = this.$store.state.userId;
      let config = this.get_access_token();
      axios
        .get(
          "http://localhost:5000/getteam/" + userId + "/" + this.activeGameweek,
          config
        )
        .then((res) => {
          // Check if user has picked team
          if (res.data.team.length == 0) this.$router.push("/pickteam");
          for (const player of res.data.team) {
            this.myTeam[player.position].push(player);
          }
          // this.myTeam = res.data.team
        })
        .catch((err) => console.error(err));
    },

    // Change player status
    changePlayer(e, playerId, playerPos) {
      // Check if selected(sub out) player is striker
      // Check if selected(sub out) player is the last striker
      // Show error if selected(sub out) player is not a striker
      if (
        this.selected[1] == "striker" &&
        this.myTeam.striker.filter((player) => player.status == "active")
          .length == 1 &&
        playerPos != "striker"
      ) {
        this.msg = "Minimum of one striker required!";
        this.showMsg = true;
        return;
      }
      // Make bench player active
      for (const player of this.myTeam[playerPos]) {
        if (player.id == playerId) player.status = "active";
      }

      // Bench active player
      for (const player of this.myTeam[this.selected[1]]) {
        if (player.id == this.selected[2]) player.status = "bench";
      }
    },

    // Add active player to selected
    toggleActive(e, playerNo, playerPos, playerId) {
      this.$set(this.selected, 0, playerNo);
      this.$set(this.selected, 1, playerPos);
      this.$set(this.selected, 2, playerId);
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

.substitutes,
.reserve-outfield {
  display: flex;
}

.substitutes {
  justify-content: space-around;
}
</style>
