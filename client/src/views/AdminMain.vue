<template>
  <div class="body">
    <div class="side-nav-container">
      <div class="side-nav-title-container">DL Cup Fantasy</div>
      <div class="side-nav-component" @click="component = 'admin-matches'">
        <fa class="i" icon="clock" size="1x" />
        <span class="side-nav-component-text">Schedule</span>
      </div>
      <div class="side-nav-component" @click="component = 'admin-live'">
        <fa class="i" icon="sync" size="1x" />
        <span class="side-nav-component-text">Live Update</span>
      </div>
      <div class="side-nav-component" @click="component = 'admin-players'">
        <fa class="i" icon="users" size="1x" />
        <span class="side-nav-component-text">Players</span>
      </div>

      <div class="side-nav-component" @click="component = 'admin-season'">
        <fa class="i" icon="play-circle" size="1x" />
        <span class="side-nav-component-text">Season</span>
      </div>
      <div class="side-nav-component" @click="logout">
        <fa class="i" icon="sign-out-alt" size="1x" />
        <span class="side-nav-component-text">Logout</span>
      </div>
    </div>

    <div class="main-container">
      <keep-alive>
        <component v-bind:is="component"></component>
      </keep-alive>
    </div>
  </div>
</template>

<script>
import AdminSchedule from "../components/admin/AdminSchedule.vue";
import AdminLive from "../components/admin/AdminLive";
import AdminPlayers from "../components/admin/AdminPlayers";
import AdminSeason from "../components/admin/AdminSeason";
export default {
  components: {
    "admin-matches": AdminSchedule,
    "admin-live": AdminLive,
    "admin-players": AdminPlayers,
    "admin-season": AdminSeason,
  },
  data() {
    return {
      component: "admin-matches",
    };
  },
  methods: {
    logout() {
      sessionStorage.removeItem("user-id");
      this.$store.commit("setCurrentUserID");
      this.$router.push("/");
    },
  },
};
</script>

<style scoped>
/* Fonts */
/* Defining Fonts */
@font-face {
  font-family: "Poppins";
  src: local("Poppins"),
    url("../assets/fonts/Poppins/Poppins-Regular.ttf") format("truetype");
}
@font-face {
  font-family: "SourceSans";
  src: local("SourceSans"),
    url("../assets/fonts/SourceSans/SourceSansPro-Regular.ttf")
      format("truetype");
}
/* Styling for dynamic stuff */
.body {
  /* TEMP */
  height: 100vh;
  width: 100% !important;
  background-image: linear-gradient(
      to right,
      rgba(0, 0, 0, 0.5),
      rgba(0, 0, 0, 0.55)
    ),
    url("../assets/img/Admin_Backround.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  /* TEMP */
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  display: flex;
  overflow-x: hidden;
}

.side-nav-container {
  /* TEMP */
  background-color: rgba(255, 255, 255, 0.65);
  /* TEMP */
  width: 15%;
  height: 100%;
  padding: 0 1.5% 0 1.5%;
  box-shadow: 5px 5px 12px rgba(0, 0, 0, 0.45);
}
.side-nav-title-container {
  margin-top: 15%;
  padding-left: 10%;
  padding-right: 10%;
  font-size: 36px;
  font-weight: 900;
  letter-spacing: 2px;
  font-family: "Poppins";
  text-align: center;
  margin-bottom: 20%;
}
.active {
  background-color: #9c27b0;
  box-shadow: 0 4px 20px 0 rgb(0 0 0 / 14%),
    0 7px 10px -5px rgb(156 39 176 / 40%);
}
.side-nav-component {
  margin-top: 15%;
  cursor: pointer;
  font-family: "SourceSans";
  font-size: 24px;
  letter-spacing: 1px;
  padding: 5% 3% 5% 10%;
  display: flex;
  align-items: center;
  box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.25);
  transition: all 0.75s ease 0s;
}
.side-nav-component:hover {
  background-color: #9c27b0;
  box-shadow: 0 4px 20px 0 rgb(0 0 0 / 14%),
    0 7px 10px -5px rgb(156 39 176 / 40%);
  transform: translateY(-7px);
}
.side-nav-component:hover .i {
  color: white;
}
.i {
  width: 21px;
  height: auto;
  color: black;
}
.side-nav-component-text {
  margin-left: 6%;
}

.main-container {
  width: 85%;
  height: 100%;
}
</style>
