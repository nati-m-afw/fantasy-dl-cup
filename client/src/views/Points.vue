<template>
  <div class="body">
    <nav>
      <h1>DL Cup Fantasy</h1>
    </nav>
    <navigation :activePage="'Points'" />
    <div id="info">
      {{ myTeamName }}
      |GW-> {{ activeGameweek }}
    </div>
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
            >
              <img
                :src="
                  require('@/assets/img/jerseys/' + player.department + '.png')
                "
                alt=""
              />
              <span class="player-details">GK{{ player.fname }}</span>
            </div>
          </div>
          <!-- DEF -->
          <div class="defender">
            <div
              v-for="(player, i) in myTeam.defender.filter(
                (player) => player.status == 'active'
              )"
              :key="i"
            >
              <img
                :src="
                  require('@/assets/img/jerseys/' + player.department + '.png')
                "
                alt=""
              />
              <span class="player-details">DEF{{ player.fname }}</span>
            </div>
          </div>
          <!-- MID -->
          <div class="midfielder">
            <div
              v-for="(player, i) in myTeam.midfielder.filter(
                (player) => player.status == 'active'
              )"
              :key="i"
            >
              <img
                :src="
                  require('@/assets/img/jerseys/' + player.department + '.png')
                "
                alt=""
              />
              <span class="player-details">MID{{ player.fname }}</span>
            </div>
          </div>
          <!-- ST -->
          <div class="striker">
            <div
              v-for="(player, i) in myTeam.striker.filter(
                (player) => player.status == 'active'
              )"
              :key="i"
            >
              <img
                :src="
                  require('@/assets/img/jerseys/' + player.department + '.png')
                "
                alt=""
              />
              <span class="player-details">ST{{ player.fname }}</span>
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
              <img
                :src="
                  require('@/assets/img/jerseys/' + player.department + '.png')
                "
                alt=""
              />
              <span class="player-details">GK{{ player.fname }}</span>
            </div>

            <!-- SUB Players -->
            <div v-for="(player, i) in benchedPlayers" :key="i">
              <img
                :src="
                  require('@/assets/img/jerseys/' + player.department + '.png')
                "
                alt=""
              />
              <span class="player-details"
                >{{ player.position }}{{ player.fname }}</span
              >
            </div>
          </div>
        </div>
      </div>
      <div class="sidebar"></div>
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
    getActiveGameweek() {
      axios.get("http://localhost:5000/getactivegw")
        .then(res => {
          this.activeGameweek = res.data.activeGW;
          this.getTeam();
        })
        .catch(err => console.error(err));
    },

    getTeam() {
      let userId = this.$store.state.userId;

      axios
        .get(
          "http://localhost:5000/getteam/" + userId + "/" + this.activeGameweek
        )
        .then((res) => {
          if(res.data.team == false && this.activeGameweek == 0){
            this.alertMsg = 'Gameweek has not started!';
            this.showMsg = true;
          }
          else if(res.data.team == false){
            this.alertMsg = 'No team for current GW in DB';
            this.showMsg = true;
          };
          for (const player of res.data.team) {
            this.myTeam[player.position].push(player);
          }
          // this.myTeam = res.data.team
        })
        .catch((err) => console.error(err));
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

.starting_team {
  display: grid;
  grid-template-rows: repeat(4, 150px);
  /* justify-items: center; */
}

.starting_team > div,
.substitutes > div {
  display: flex;
  justify-content: center;
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
  position: absolute;
  bottom: -10px;
  left: 37%;
}

#info {
  display: inline-flex;
  font-size: 1.7rem;
  font-weight: bold;
  background-color: cadetblue;
  margin: 0 6rem;
  padding: 0.7rem;
}
</style>