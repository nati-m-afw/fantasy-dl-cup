<template>
  <div class="body">
    <div id="info"></div>
    <!-- <pre>{{ $data }}</pre> -->
    <div id="team_selection">
      <div id="transfer_field">
        <div class="goalkeeper">
          <i></i>
            <div v-for="i in [0,1]" :key="i">
              <fa @click="getPlayers" class="i" icon="user" size="7x" />
              <span>GK</span>
              <span v-if="myTeam.goalkeeper[i]">{{ myTeam.goalkeeper[i].fname }}</span>
            </div>
          <i></i>
        </div>
        <div class="defender">
          <div v-for="i in [0,1,2]" :key="i">
              <fa @click="getPlayers" class="i" icon="user" size="7x" />
              <span>DEF</span>
              <span v-if="myTeam.defender[i]">{{ myTeam.defender[i].fname }}</span>
          </div>
        </div>
        <div class="midfielder">
          <div v-for="i in [0,1,2]" :key="i">
              <fa @click="getPlayers" class="i" icon="user" size="7x" />
              <span>MID</span>
              <span v-if="myTeam.midfielder[i]">{{ myTeam.midfielder[i].fname }}</span>
            </div>
        </div>
        <div class="striker">
          <i></i>
          <div v-for="i in [0,1]" :key="i">
              <fa @click="getPlayers" class="i" icon="user" size="7x" />
              <span>ST</span>
              <span v-if="myTeam.striker[i]">{{ myTeam.striker[i].fname }}</span>
          </div>
          <i></i>
        </div>
      </div>
      <div id="transfer_sidebar">
        <h2 v-if="!serverStatus">Server could not be reached.</h2>
        <ul>
          <li v-for="(player, index) in playersApi" :key="index" :class="checkSelected(player) ? 'disabled' : 'active'">
            <span>{{ player.fname }}</span>
            <span>{{ player.lname }}</span>
            <span>{{ player.position }}</span>
            <button @click="addPlayer($event, player)" :disabled="checkSelected(player)">+</button>
          </li>
        </ul>
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
        goalkeeper: [],
        defender: [],
        midfielder: [],
        striker: [],
      },

      // Players from api based on position
      playersApi: [],

      // Server status Up == True
      serverStatus: true,
    };
  },

  methods: {
    // Get players from api
    getPlayers(e){
      const position= e.path[3].className;
      // console.log(e.path);
      
      axios.get('http://localhost:5000/getplayers/' + position)
      .then(res => {
        this.playersApi = res.data.players;
        this.serverStatus = true;
      })
      .catch(err => {
        this.serverStatus = false;
        console.error(err);
      });
      // .then(res => console.log(res.data));
    },

    // Add selected player to myTeam based on position
    addPlayer(e, player){
      // check if user has already added current player
      this.myTeam[player.position].includes(player) ? 0 : this.myTeam[player.position].push(player);
    },

    // Check if player is in myTeam.<position>
    checkSelected(player){
      return this.myTeam[player.position].includes(player) ? true : false
    },

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

.i {
  color: white;
  cursor: pointer;
}

#transfer_sidebar {
  background-color: white;
  display: flex;
}

li.disabled{
  background-color: #696969;
  color: black;
}
</style>