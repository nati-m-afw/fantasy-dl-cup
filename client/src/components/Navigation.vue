<template>
  <div class="sticky-nav">
    <router-link to="/myteam" :class="activePage == 'MyTeam' ? 'active' : ''"
      >My team</router-link
    >
    <router-link to="/points" :class="activePage == 'Points' ? 'active' : ''"
      >Points</router-link
    >
    <router-link
      to="/transfers"
      :class="activePage == 'Transfers' ? 'active' : ''"
      >Transfers</router-link
    >
    <router-link to="" :class="activePage == 'myTeam' ? 'active' : ''"
      >League</router-link
    >
    <router-link to="" :class="activePage == 'myTeam' ? 'active' : ''"
      >Table</router-link
    >
    <router-link to="" :class="activePage == 'myTeam' ? 'active' : ''"
      >Fixtures</router-link
    >
    <router-link to="" :class="activePage == 'myTeam' ? 'active' : ''"
      >Stats</router-link
    >
    <div class="dropdown">
      <div class="dropdiv"></div>
      <div class="dropdown-content">
        <a href="#">Profile</a>
        <a href="#" @click.prevent="logout">Log Out</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["activePage"],

  methods: {
    // Logout
    logout() {
      localStorage.removeItem("user-id");
      this.$store.commit("setCurrentUserID");
      this.$router.push("/");
    },
  },
};
</script>

<style scoped></style>
