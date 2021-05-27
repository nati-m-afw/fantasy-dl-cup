<template>
  <div>
    <pre>{{ $store.state.myTeam }}</pre>
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
      team: this.$store.state.myTeam,
    };

    // Send myTeam to api
    axios
      .post("http://localhost:5000/", payload)
      .then(() => {
        this.isRegistered = true;
        this.msg = "Successfully registered!";
        this.showMsg = true;
      })
      .catch((err) => {
        console.error(err);
        this.msg = "An error occured. Please try again!";
        this.showMsg = true;
      });
  },
};
</script>

<style scoped>
</style>