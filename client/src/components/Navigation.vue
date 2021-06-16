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
    <router-link to="/league" :class="activePage == 'League' ? 'active' : ''"
      >League</router-link
    >
    <router-link to="/table" :class="activePage == 'Table' ? 'active' : ''"
      >Table</router-link
    >
    <router-link to="/fixtures" :class="activePage == 'Fixtures' ? 'active' : ''"
      >Fixtures</router-link
    >
    <router-link to="/statistics" :class="activePage == 'Stats' ? 'active' : ''"
      >Stats</router-link
    >
    <div class="dropdown">
      <div class="dropdiv"></div>
      <div class="dropdown-content">
        <router-link to="/profile">Profile</router-link>
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
      sessionStorage.removeItem("user-id");
      this.$store.commit("setCurrentUserID");
      this.$router.push("/");
    },
  },
};
</script>

<style scoped></style>
