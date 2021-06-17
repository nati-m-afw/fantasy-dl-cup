<template>
  <div class="modal-container">
    <div class="player-info-modal">
      <h3 class="player-modal-name">
        {{ player.fname + ' ' + player.lname }}
      </h3>

      <div>Total Points: {{ this.totalPts }}</div>
      <div>Total Goals: {{ this.totalGoals }}</div>
      <div>Total Assists: {{ this.totalAssists }}</div>
      <div>Clean Sheets: {{ this.cleansheets }}</div>
      <div>Yellow Cards: {{ this.yellowCards }}</div>
      <div>Red Cards: {{ this.redCards }}</div>

      <button @click="$emit('close')">close</button>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  props: ["player"],

  data() {
    return {
      totalPts: "",
      totalGoals: "",
      totalAssists: "",
      cleansheets: "",
      yellowCards: "",
      redCards: "",
    };
  },

  methods: {
    getPlayerStats() {
      axios
        .get(`http://127.0.0.1:5000/stat/${this.player.id}`)
        .then((res) => {
          this.totalPts = res.data.total_points;
          this.totalGoals = res.data.total_goals;
          this.totalAssists = res.data.total_assists;
          this.cleansheets = res.data.clean_sheets;
          this.yellowCards = res.data.yellow_cards;
          this.redCards = res.data.red_cards;
        })
        .catch((err) => console.error(err));
    },
    // close() {
    //     this.showModal = false;
    // }
  },
  created() {
    this.getPlayerStats();
  },
};
</script>
<style scoped>
.modal-container {
  position: fixed;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  z-index: 100;
  background: linear-gradient(to right, rgba(33, 33, 33, 0.4), rgba(33, 33, 33, 0.4));
}

.player-info-modal {
  height: 500px;
  width: 500px;
  background: var(--secondary-color);
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 1%;
  display: grid;
  grid-template-rows: repeat(8, 50px);
  grid-row-gap: .2rem;
}

.player-modal-name {
    background: var(--primary-color);
    color: var(--secondary-color);
    text-align: center;
}
</style>
