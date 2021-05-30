<template>
  <div class="body">
    <div id="info">
      <button @click="logout">LOGOUT</button>
    </div>
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
              :class="{
                active: selected[0] == i && selected[1] == 'goalkeeper',
              }"
              @click="toggleActive($event, i, 'goalkeeper', player.id)"
            >
              <fa class="i" icon="user" size="7x" />
              <span>GK{{ player.fname }}</span>
            </div>
          </div>
          <!-- DEF -->
          <div class="defender">
            <div
              v-for="(player, i) in myTeam.defender.filter(
                (player) => player.status == 'active'
              )"
              :key="i"
              :class="{ active: selected[0] == i && selected[1] == 'defender' }"
              @click="toggleActive($event, i, 'defender', player.id)"
            >
              <fa class="i" icon="user" size="7x" />
              <span>DEF{{ player.fname }}</span>
            </div>
          </div>
          <!-- MID -->
          <div class="midfielder">
            <div
              v-for="(player, i) in myTeam.midfielder.filter(
                (player) => player.status == 'active'
              )"
              :key="i"
              :class="{
                active: selected[0] == i && selected[1] == 'midfielder',
              }"
              @click="toggleActive($event, i, 'midfielder', player.id)"
            >
              <fa class="i" icon="user" size="7x" />
              <span>MID{{ player.fname }}</span>
            </div>
          </div>
          <!-- ST -->
          <div class="striker">
            <div
              v-for="(player, i) in myTeam.striker.filter(
                (player) => player.status == 'active'
              )"
              :key="i"
              :class="{ active: selected[0] == i && selected[1] == 'striker' }"
              @click="toggleActive($event, i, 'striker', player.id)"
            >
              <fa class="i" icon="user" size="7x" />
              <span>ST{{ player.fname }}</span>
            </div>
          </div>
        </div>
        <!-- SUB -->
        <div class="substitutes">
          <div>
            <!-- SUB GK -->
            <div
              v-for="(player, i) in myTeam.goalkeeper.filter(
                (player) => player.status == 'bench'
              )"
              :key="i"
            >
              <fa class="i" icon="user" size="7x" />
              <span>GK{{ player.fname }}</span>
              <span v-if="selected[1] == 'goalkeeper'">
                <button
                  @click="changePlayer($event, player.id, player.position)"
                >
                  <fa icon="exchange-alt" />
                </button>
              </span>
            </div>

            <!-- SUB Players -->
            <div v-for="(player, i) in benchedPlayers" :key="i">
              <fa class="i" icon="user" size="7x" />
              <span>{{ player.position }}{{ player.fname }}</span>
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
      <div class="sidebar"></div>
      <button @click="updateTeamApi">SAVE</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Alert from "../components/Alert.vue";

export default {
  data() {
    return {
      myTeam: {
        goalkeeper: [],
        defender: [],
        midfielder: [],
        striker: [],
      },

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
  },

  methods: {
    // Get user Team
    getTeam() {
      let userId = this.$store.state.userId;

      axios
        .get("http://localhost:5000/getteam/" + userId)
        .then((res) => {
          
          // Check if user has picked team
          if (res.data.team.length == 0)
            this.$router.push("/pickteam")
          for (const player of res.data.team) {
            this.myTeam[player.position].push(player);
          }
          // this.myTeam = res.data.team
        })
        .catch((err) => console.error(err));
    },

    // Change player status
    changePlayer(e, playerId, playerPos) {
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
        gameweekId: 1,
      };

      console.log(this.$store.state.userId);

      // push player id into payload
      for (const position in this.$store.state.myTeam) {
        // payload.team[position] = [];
        for (const player of this.$store.state.myTeam[position]) {
          payload.team.push({ 
            'playerId': player.id,
            'status': player.status,
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
    logout(){
      localStorage.removeItem("user-id");
      this.$store.commit("setCurrentUserID");
      this.$router.push("/");
    }
  },

  created() {
    this.getTeam();
  },
};
</script>

<style>
* {
  box-sizing: border-box;
}

.body {
  margin: 0;
  min-height: 100vh;

  background-color: #696969;
  padding: 5%;
}

#info {
  width: 100%;
  display: flex;
}

#team_selection {
  display: grid;
  grid-template-columns: 65vw 20vw;
  grid-template-rows: 800px;
  grid-column-gap: 2vw;
}

.team {
  background-color: black;
  display: grid;
  color: white;

  grid-template-rows: auto 1fr;
}

.team > div > div {
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.starting_team {
  display: grid;
  grid-template-rows: repeat(4, 1fr);
  grid-row-gap: 64px;
}

.substitutes {
  grid-row: -1;
}

.i {
  color: white;
  cursor: pointer;

  font-size: 112px;
}

.sidebar {
  background-color: white;
  display: flex;
}

.active {
  background-color: tomato;
}
</style>