<template>
  <div>
    <!-- <pre>{{ $store.state.myTeam }}</pre> -->
    <alert :msg="msg" v-if="showMsg" />
    <button @click="createdMe">CLK</button>
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

  methods: {
    createdMe() {
      // prepare payload
      const payload = {
        userId: this.$store.state.userId,
        team: [],
        gameweekId: 1,
      };
  
      for (const position in this.$store.state.myTeam) {
          // payload.team[position] = [];
          for(const player of this.$store.state.myTeam[position]){
            payload.team.push(player.id);
          }
      }
  
      // Initial default lineup
      for (const player in payload.team){
        if (['0','2','3','4','5','6','8'].includes(player)){
          payload.team[player] = {
            'playerId': payload.team[player],
            'status': 'active'
          };
        }
        else{
          payload.team[player] = {
            'playerId': payload.team[player],
            'status': 'bench'
          };
        }
      }
  
      
      // Send myTeam to api
      axios
        .post("http://localhost:5000/updateuserplayers", payload)
        .then(() => {
          this.isRegistered = true;
          this.msg = "Successfully registered!";
          this.showMsg = true;
          // this.$router.go();
        })
        .catch((err) => {
          console.error(err);
          this.msg = "An error occured. Please try again!";
          this.showMsg = true;
        });
    },

  },
};
</script>

<style scoped>
</style>