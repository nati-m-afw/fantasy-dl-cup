<template>
  <div>
    <!-- <pre>{{ $store.state.myTeam }}</pre> -->
    <alert :msg="msg" v-if="showMsg" />
  </div>
</template>

<script>
import axios from "axios";
import Alert from "../components/Alert.vue";

export default {
  data() {
    return {
      isRegistered: false,
      msg: "",
      showMsg: false,
    };
  },

  components: {
    alert: Alert,
  },

  created() {
    // prepare payload
    const payload = {
      userId: this.$store.state.userId,
      team: [],
      gameweekId: this.$store.state.activeGameweek + 1,
    };

    // push player id into payload
    for (const position in this.$store.state.myTeam) {
      // payload.team[position] = [];
      for (const player of this.$store.state.myTeam[position]) {
        payload.team.push(player.id);
      }
    }

    // Initial default lineup
    for (const player in payload.team) {
      if (["0", "2", "3", "4", "5", "6", "8"].includes(player)) {
        payload.team[player] = {
          playerId: payload.team[player],
          status: "active",
        };
      } else {
        payload.team[player] = {
          playerId: payload.team[player],
          status: "bench",
        };
      }
    }

    // Send myTeam to API
    axios
      .post("http://localhost:5000/updateuserplayers", payload)
      .then(() => {
        this.isRegistered = true;
        this.msg = "Successfully registered!";
        this.showMsg = true;
        this.$router.push("/myteam");
      })
      .catch((err) => {
        console.error(err);
        this.msg = "An error occured. Please try again!";
        this.showMsg = true;
      });
  },
};
</script>

<style scoped></style>
