<template>
  <div class="body">
    <div id="info"></div>
    <pre>{{ $data }}</pre>
    <div id="team_selection">
      <div id="transfer_field">
        <div class="goalkeeper">
          <i></i>
          <fa @click="getPlayers" class="i" icon="user" size="7x" />
          <fa @click="getPlayers" class="i" icon="user" size="7x" />
          <i></i>
        </div>
        <div class="defender">
          <fa @click="getPlayers" class="i" icon="user" size="7x" />
          <fa @click="getPlayers" class="i" icon="user" size="7x" />
          <fa @click="getPlayers" class="i" icon="user" size="7x" />
        </div>
        <div class="midfielder">
          <fa @click="getPlayers" class="i" icon="user" size="7x" />
          <fa @click="getPlayers" class="i" icon="user" size="7x" />
          <fa @click="getPlayers" class="i" icon="user" size="7x" />
        </div>
        <div class="striker">
          <i></i>
          <fa @click="getPlayers" class="i" icon="user" size="7x" />
          <fa @click="getPlayers" class="i" icon="user" size="7x" />
          <i></i>
        </div>
      </div>
      <div id="transfer_sidebar">
        <ul>
          <li v-for="(player, index) in playersApi" :key="index">
            <span>{{ player.fname }}</span>
            <span>{{ player.lname }}</span>
            <span>{{ player.position }}</span>
            <button @click="addPlayer($event, player.id, player.position)">+</button>
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
      activePosition: "",
    };
  },

  methods: {
    getPlayers(e){
      const position= e.path[2].className;
      
      axios.get('http://localhost:5000/getplayers/' + position)
      .then(res => this.playersApi = res.data.players);
      // .then(res => console.log(res.data));
    },

    addPlayer(e, playerId, playerPosition){
      // check if user has already added current player
      // 
      this.myTeam[playerPosition].includes(playerId) ? 0 : this.myTeam[playerPosition].push(playerId);
    }

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
</style>