<template>
  <div class="sub-body">
    <nav>
      <h1>DL Cup Fantasy</h1>
    </nav>
    <navigation :activePage="'Stats'" />
    <div class="grid-container">
      <div class="skewed">
        <div class="category">Top Scorer</div>

        <div
          v-for="player in stat_info_all.goals_scored"
          :key="player.player_id"
        >
          <img :src="require(`@/assets/img/jerseys/${player.team_name}.png`)" />
          {{ player.player_name }} {{ player.goals_scored }}
        </div>
      </div>
      <div class="skewed">
        <div class="category">Most Assists</div>
        <div
          v-for="player in stat_info_all.assists_provided"
          :key="player.player_id"
        >
          <img :src="require(`@/assets/img/jerseys/${player.team_name}.png`)" />
          {{ player.player_name }} {{ player.assists_provided }}
        </div>
      </div>
      <div class="skewed">
        <div class="category">Most Cleansheets</div>
        <div
          v-for="player in stat_info_all.clean_sheets"
          :key="player.player_id"
        >
          <img :src="require(`@/assets/img/jerseys/${player.team_name}.png`)" />
          {{ player.player_name }} {{ player.clean_sheets }}
        </div>
      </div>
      <div class="skewed">
        <div class="category">Yellow Cards</div>
        <div
          v-for="player in stat_info_all.yellow_cards"
          :key="player.player_id"
        >
          <img :src="require(`@/assets/img/jerseys/${player.team_name}.png`)" />
          {{ player.player_name }} {{ player.yellow_cards }}
        </div>
      </div>
      <div class="skewed">
        <div class="category">Red Cards</div>
        <div v-for="player in stat_info_all.red_cards" :key="player.player_id">
          <img :src="require(`@/assets/img/jerseys/${player.team_name}.png`)" />
          {{ player.player_name }} {{ player.red_cards }}
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import Navigation from "../components/Navigation.vue";
let path = "http://localhost:5000";
export default {
  name: "Statistics",
  data() {
    return {
      stat_info_all: "",
    };
  },
  async mounted() {
    // Get Token from Local Storage
    let access_token = localStorage.getItem("token");

    // Prepare a header config
    let config = {
      headers: {
        Authorization: `Bearer ${access_token}`,
      },
    };

    axios
      .get(`${path}/statistics`, config)
      .then((response) => {
        console.log(response.data.goals_scored);
        this.stat_info_all = response.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  components: {
    navigation: Navigation,
  },
};
</script>
<style scoped>
body {
  min-height: 100vh;
  background: whitesmoke;
}

.grid-container {
  display: grid;
  justify-content: center;
  grid-template-columns: repeat(3, 25%);
  grid-gap: 40px 0;
  padding: 5rem 0;
  position: relative;
}

.skewed {
  transform: skewY(-10deg);
  width: 325px;
  height: 450px;
  background: #210b41;
  border-radius: 8px;
}

.skewed > div {
  padding: 7px 15px;
  padding-right: 30px;
  font-family: sans-serif;
  font-size: 1.2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: crimson;
  color: whitesmoke;
}

.skewed > .category {
  padding: 15px 10px;
  font-size: 1.5rem;
  font-weight: bold;
  background: whitesmoke;
  border-radius: 7px 7px 0 0;
  color: crimson;
}

.skewed img {
  width: 70px;
}
</style>
