<template>
  <div class="body">
    <div id="info">
      <h1>{{ myTeamName }}</h1>
    </div>
    <!-- <pre>{{ $data }}</pre> -->
    <div id="team_selection">
      <div id="transfer_field">
        <div class="goalkeeper">
          <i></i>
          <!-- Render two placeholders -->
          <div
            v-for="i in [0, 1]"
            :key="i"
            :class="{ active: selected[0] == i && selected[1] == 'gk' }"
            @click="toggleActive($event, i, 'gk')"
          >
            <!-- Set selectedPlayerIndex when clicked -->
            <!-- <fa
              @click="getPlayers($event, i)"
              class="i"
              icon="user"
              size="7x"
            /> -->
            <img
              @click="getPlayers($event, i)"
              class="i"
              :src="require('@/assets/img/jerseys/placeholdershirt.png')"
              alt=""
            />
            <span>GK</span>
            <!-- Check if any selected players in myTeam -->
            <!-- If so display name -->
            <span v-if="myTeam.goalkeeper[i]">{{
              myTeam.goalkeeper[i].fname
            }}</span>
          </div>
          <i></i>
        </div>
        <div class="defender">
          <!-- Render three placeholders -->
          <div
            v-for="i in [0, 1, 2]"
            :key="i"
            :class="{ active: selected[0] == i && selected[1] == 'df' }"
            @click="toggleActive($event, i, 'df')"
          >
            <!-- <fa
              @click="getPlayers($event, i)"
              class="i"
              icon="user"
              size="7x"
            /> -->
            <img
              @click="getPlayers($event, i)"
              class="i"
              :src="require('@/assets/img/jerseys/placeholdershirt.png')"
              alt=""
            />
            <span>DEF</span>
            <span v-if="myTeam.defender[i]">{{
              myTeam.defender[i].fname
            }}</span>
          </div>
        </div>
        <div class="midfielder">
          <div
            v-for="i in [0, 1, 2]"
            :key="i"
            :class="{ active: selected[0] == i && selected[1] == 'md' }"
            @click="toggleActive($event, i, 'md')"
          >
            <!-- <fa
              @click="getPlayers($event, i)"
              class="i"
              icon="user"
              size="7x"
            /> -->
            <img
              @click="getPlayers($event, i)"
              class="i"
              :src="require('@/assets/img/jerseys/placeholdershirt.png')"
              alt=""
            />
            <span>MID</span>
            <span v-if="myTeam.midfielder[i]">{{
              myTeam.midfielder[i].fname
            }}</span>
          </div>
        </div>
        <div class="striker">
          <i></i>
          <div
            v-for="i in [0, 1]"
            :key="i"
            :class="{ active: selected[0] == i && selected[1] == 'st' }"
            @click="toggleActive($event, i, 'st')"
          >
            <!-- <fa
              @click="getPlayers($event, i)"
              class="i"
              icon="user"
              size="7x"
            /> -->
            <img
              @click="getPlayers($event, i)"
              class="i"
              :src="require('@/assets/img/jerseys/placeholdershirt.png')"
              alt=""
            />
            <span>ST</span>
            <span v-if="myTeam.striker[i]">{{ myTeam.striker[i].fname }}</span>
          </div>
          <i></i>
        </div>
      </div>
      <div id="transfer_sidebar">
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
      </div>
      <div>
        <!-- <router-link to="Registration" @click.native="submit"> -->
        <button @click="submit">Save</button>
        <!-- </router-link> -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      // Stores users selection
      myTeam: {
        goalkeeper: [null, null],
        defender: [null, null, null],
        midfielder: [null, null, null],
        striker: [null, null],
      },

      myTeamName: "",

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

  methods: {
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

    submit() {
      // Check for if team is complete
      let teamCompleted = true;
      for (const position in this.myTeam) {
        for (const player of this.myTeam[position]) {
          teamCompleted = !player ? false : true;
        }
      }

      if (teamCompleted) {
        this.$store.commit("updateMyTeam", this.myTeam);
        this.$router.push("/registration");
        return;
      }

      alert("You need to complete your team before registration!");
    },
  },

  created() {
    this.myTeamName = this.$store.state.myTeamName;
    axios
      .get("http://localhost:5000/getteam/" + this.$store.state.userId + "/5")
      .then((res) => {
        // Check if user has picked team
        if (res.data.team.length != 0) this.$router.push("/myteam");
      })
      .catch((err) => console.error(err));
  },
};
</script>

<style scoped>
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

#transfer_field {
  background-color: black;
  display: grid;
  color: white;

  grid-template-rows: repeat(4, 1fr);
}

#transfer_field > div {
  display: flex;

  justify-content: space-around;
  align-items: center;
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

li.disabled {
  background-color: #696969;
  color: black;
}

.active {
  background-color: tomato;
}
#team_selection img {
  width: 15vw;
  cursor: pointer;
}
</style>
