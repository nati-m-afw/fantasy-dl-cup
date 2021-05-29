<template>
  <div class="body">
    <div id="info"></div>
    <pre>{{ $data }}</pre>
    <div id="team_selection">
      <div class="team">
        <div class="starting_team">
          <div><fa icon="user" size="7x" /></div>
          <div>
            <fa icon="user" size="7x" />
            <fa icon="user" size="7x" />
            <fa icon="user" size="7x" />
          </div>
          <div>
            <fa icon="user" size="7x" />
            <fa icon="user" size="7x" />
          </div>
          <div>
            <fa icon="user" size="7x" />
          </div>
        </div>
        <div class="substitutes">
          <div>
            <fa icon="user" size="7x" />
            <fa icon="user" size="7x" />
            <fa icon="user" size="7x" />
          </div>
        </div>
      </div>
      <div class="sidebar"></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      myTeam: {
        goalkeeper: [],
        defender: [],
        midfielder: [],
        striker: [],
      },
    };
  },

  methods: {
    getTeam() {
      let userId = this.$store.state.userId;

      axios  
        .get("http://localhost:5000/getteam/" + userId)
        .then((res) => {
          for (const player of res.data.team){
            this.myTeam[player.position].push(player);
          };
          // this.myTeam = res.data.team
        })
        .catch((err) => console.error(err));
    },
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

i {
  color: white;
  cursor: pointer;

  font-size: 112px;
}

.sidebar {
  background-color: white;
  display: flex;
}
</style>