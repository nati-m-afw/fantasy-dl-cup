<template>
  <div class="sub-body">
    <FlashMessage :position="'top'"></FlashMessage>
    <h1 class="header-title">Admin Players</h1>

    <!-- Main Container -->

    <div class="main-container">
      <!-- Team Select and Add  new Player Sections -->
      <div class="select-team-container">
        <!-- Select Team Options -->
        <label for="SelectTeam" class="select-team-label">Team:</label>
        <select
          name="SelectTeam"
          v-model="selected_team"
          class="select-option"
          @change="work"
        >
          <option value="">Select the team</option>
          <option
            v-bind:value="team.id"
            v-for="team in all_teams"
            :key="team.id"
          >
            {{ team.team_name }}
          </option>
        </select>
        <!-- Select Team Options -->

        <!-- Add New Player Button -->
        <button class="add-new-player-container" @click="add_new_player">
          <fa class="i" size="1x" icon="plus" />
          <div>Add New Player</div>
        </button>
        <!-- Add New Player Button -->
      </div>
      <!-- Team Select and Add new Player Section -->

      <!-- Loader for Players Data -->
      <div class="loader" v-show="loader == 1">Loading</div>
      <!-- Loader for Player Data -->

      <!-- Info Section for players -->
      <div
        class="players-container"
        v-show="all_players[0]"
        v-if="showDetails == true"
      >
        <!-- Team Name Display -->
        <h1 class="team-title-header">{{ selected_team_name }}</h1>

        <div
          v-for="player in all_players"
          :key="player.id"
          v-bind:player-id="player.id"
          class="players-main-container"
        >
          <!-- Position Selection Section -->
          <select
            class="player-position-container"
            v-bind:value="player.position"
            :disabled="editing == false"
          >
            <option value="goalkeeper">GoalKeeper</option>
            <option value="defender">Defender</option>
            <option value="midfielder">Midfielder</option>
            <option value="striker">Striker</option>
          </select>
          <!-- Position Selection Section -->

          <!-- Player Name Section -->
          <div class="player-name-container">
            <input
              type="text"
              name="PlayerName"
              v-bind:value="player.fname + ' ' + player.lname"
              :disabled="editing == false"
            />
          </div>
          <!-- Player Name Section -->

          <!-- Option for Delete,Save,Edit Section -->
          <div class="options-container">
            <!-- Save Option -->
            <div
              class="save-container"
              @click="save_player"
              v-show="editing == true"
            >
              <fa class="i" size="1x" icon="save" />
            </div>
            <!-- Save Option -->

            <!-- Edit Option -->
            <div
              class="edit-container"
              @click="edit_player"
              v-show="editing == false"
            >
              <fa class="i" size="1x" icon="edit" />
            </div>
            <!-- Edit Option -->

            <!-- Delete Option -->
            <div class="remove-container" @click="delete_player">
              <fa class="i" size="1x" icon="trash-alt" />
            </div>
            <!-- Delete Option -->
          </div>

          <!-- Option for Delete,Save,Edit Section -->
        </div>
      </div>
      <!-- Info Section for Players -->

      <!-- Modal For Adding New Player -->
      <div class="add_player_container" v-show="showDetails == false">
        <!-- New Player Position Section -->
        <div class="new-player-postion-container">
          <label for="NewPlayerPosition" class="new-player-label"
            >Position :</label
          >
          <select
            name="NewPlayerPosition"
            v-model="new_player_position"
            value="goalkeeper"
          >
            <option value="goalkeeper" default>GoalKeeper</option>
            <option value="defender">Defender</option>
            <option value="midfielder">Midfielder</option>
            <option value="Striker">Striker</option>
          </select>
        </div>
        <!-- New Player Position Section -->

        <!-- New Player Name Section -->
        <div class="new-player-fullname-container">
          <label for="firstName" class="new-player-label">First Name :</label>
          <input type="text" name="firstName" v-model="new_player_fname" />
          <label for="firstName" class="new-player-lastname-label"
            >Last Name :</label
          >
          <input type="text" name="lastName" v-model="new_player_lname" />
        </div>
        <!-- New Player Name Section -->

        <!-- New Player Team Section -->
        <div class="new-player-team-container">
          <label for="NewPlayerPosition" class="new-player-label">Team :</label>
          <select
            name="NewPlayerPosition"
            v-model="new_player_team"
            class="select-option"
          >
            <option>Select the team</option>
            <option
              v-bind:value="team.id"
              v-for="team in all_teams"
              :key="team.id"
            >
              {{ team.team_name }}
            </option>
          </select>
        </div>

        <!-- Save and Cancel Options for New Player From -->
        <div class="new-player-options-container">
          <!-- Save Button -->
          <button @click="save_new_player" class="new-player-save-button">
            Save
          </button>
          <!-- Save Button -->

          <!-- Cancel Button -->
          <button @click="cancel_new_player" class="new-player-cancel-button">
            Cancel
          </button>
          <!-- Cancel Button -->
        </div>
        <!-- Save and Cancel Options for New Player From -->
      </div>
      <!-- Modal For Adding New Player -->
    </div>

    <!-- Main Container -->
  </div>
</template>

<style scoped>
/* Dynamic Classes */

/* Dynamic Classes */
.sub-body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  width: 100%;
  height: 100vh;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
  text-align: center;
}
.header-title {
  font-family: "Poppins";
  letter-spacing: 2px;
  margin-top: 2%;
}
.main-container {
  background-color: white;
  width: 80%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 5%;
  min-height: 65vh;
  display: flex;
  flex-direction: column;
}
.select-team-container {
  width: 30%;
  margin-left: 70%;
  min-height: 10vh;
  margin-top: 2%;
}
.select-team-label {
  font-family: "Poppins";
  font-size: 20px;
  letter-spacing: 2px;
  margin-right: 2%;
}
.select-option {
  width: 45%;
  font-family: "SourcSans";
  font-size: 20px;
  font-weight: lighter;
  letter-spacing: 1px;
  outline: none;
  border: 1px solid rgba(0, 0, 0, 0.109);
  padding-top: 1.2%;
  padding-bottom: 1.2%;
}
.add-new-player-container {
  background-color: #9c27b0;
  margin-top: 5%;
  width: 45%;
  margin-left: auto;
  margin-right: auto;
  padding-top: 1.5%;
  padding-bottom: 1.5%;
  padding-left: 2%;
  padding-right: 2%;
  border: 0 !important;
  outline: none !important;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: gainsboro;
}
.add-new-player-container .i {
  width: 15px !important;
  height: auto;
}
.add-new-player-container div {
  font-family: "Poppins";
  font-size: 17px;
}
.players-container {
  min-height: 60vh;
  width: 100%;
  margin-top: 2.5%;
}
.team-title-header {
  font-family: "Poppins";
  letter-spacing: 2px;
}
.players-main-container {
  display: flex;
  justify-content: space-between;
  margin-top: 3%;
  font-family: "SourceSans";
  font-size: 22px;
  padding-left: 15%;
  padding-right: 15%;
  background-color: gainsboro;
}
.player-position-container {
  display: flex;
  min-width: 130px;
  text-align: start;
  align-items: center;
  justify-content: center;
  padding: 0.5% 0 0.5% 0;
  font-family: "Poppins";
  letter-spacing: 1.5px;
}
.player-name-container {
  min-width: 150px;
  font-weight: bolder;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: "Poppins";
  font-size: 18px;
  font-weight: bold;
}
input[type="text"] {
  height: 32px;
  padding: 0.5% 0 0.5% 0;
  margin: 0 !important;
  border: 1px solid rgba(0, 0, 0, 0.2);
  outline: none;
  font-family: "Poppins";
  font-weight: bold;
  letter-spacing: 2px;
  padding-left: 2%;
  padding-right: 0.5%;
}
.players-main-container select {
  outline: none !important;
  border: 1px solid rgba(0, 0, 0, 0.2);
  font-family: "Poppins";
  background-color: white;
}
.options-container {
  display: flex;
  min-width: 60px;
  justify-content: space-between;
  align-items: center;
}
.options-container .save-container .i {
  color: blue !important;
}
.options-container .remove-container .i {
  color: red !important;
}
.options-container .edit-container .i {
  color: green !important;
}
.add_player_container {
  width: 75%;
  margin: auto;
  padding-top: 5%;
  padding-bottom: 5%;
}
.new-player-postion-container {
  width: 45%;
  display: flex;
  align-items: center;
}
.new-player-label {
  font-family: "Poppins";
  letter-spacing: 1.5px;
  font-size: 20px;

  margin-right: 2%;
}
.new-player-postion-container select {
  width: 40%;
  font-family: "SourceSans";
  font-size: 18px;
  font-weight: lighter;
  letter-spacing: 1px;
  outline: none;
  border: 1px solid rgba(0, 0, 0, 0.109);
  padding-top: 0.5%;
  padding-bottom: 0.5%;
}
.new-player-fullname-container {
  display: flex;
  align-items: center;
  margin-top: 3%;
}
.new-player-lastname-label {
  font-family: "Poppins";
  letter-spacing: 1.5px;
  font-size: 20px;

  margin-right: 2%;
  margin-left: 5%;
}
.new-player-fullname-container input[type="text"] {
  background-color: gainsboro;
  width: 20%;
  height: 30px;
  border: 1px solid rgba(0, 0, 0, 0.109);
  padding: 0.5%;
  font-family: "SourceSans";
  font-size: 18px;
}
.new-player-team-container {
  width: 45%;
  display: flex;
  align-items: center;
  margin-top: 3%;
}
.new-player-options-container {
  margin-top: 5%;

  width: 35%;
  margin-left: auto;
  margin-right: 5%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.new-player-options-container button {
  width: 40%;
  background-color: #9c27b0;
  padding-top: 1.5%;
  padding-bottom: 1.5%;
  padding-left: 2%;
  padding-right: 2%;
  border: 0 !important;
  outline: none !important;
  font-family: "Poppins";
  font-size: 18px;
  color: gainsboro;
}
</style>

<script>
let path = "http://localhost:5000/admin";
import axios from "axios";
export default {
  data() {
    return {
      all_teams: [],
      selected_team: "",
      selected_team_name: "Select Team",
      loader: 0,
      all_players: "",
      editing: false,
      showDetails: true,
      new_player_position: "",
      new_player_fname: "",
      new_player_lname: "",
      new_player_team: "",
    };
  },
  async mounted() {
    // Get all teams for drop down
    await this.get_all_teams();
  },
  methods: {
    // Function to get access token
    get_access_token: function () {
      // Get Token from Local Storage
      let access_token = sessionStorage.getItem("token");

      // Prepare a header config
      let config = {
        headers: {
          Authorization: `Bearer ${access_token}`,
        },
      };
      return config;
    },
    work: function () {
      this.loader = 1;
      this.get_selected_team_name();
      this.get_players();
    },
    get_selected_team_name: function () {
      for (let i = 0; i < this.all_teams.length; i++) {
        if (this.all_teams[i].id == this.selected_team) {
          this.selected_team_name = this.all_teams[i].team_name;
        }
      }
    },
     handle_error: function (err) {
      // 401 UnAuthorized or 
      // Tampered with JWT
      if (err.response.status == 401 || err.response.status == 422)   {
        sessionStorage.clear()
        location.reload()
      }
    
      // Non Admin Access
      else if (err.response.status == 403) {
        sessionStorage.clear()
        location.reload()
        this.flashMessage.warning({message:"Error You is not an Admin"})
      } else {
        console.log(err)
      }
    },
    // Get all teams for drop down
    get_all_teams: function () {
      let config = this.get_access_token();
      axios
        .get(`${path}/teams`, config)
        .then((response) => {
          this.all_teams = response.data;
        })
        .catch((err) => {
          this.handle_error(err);
        });
    },
    // Get Players By department
    get_players: function () {
      let config = this.get_access_token();
      axios
        .get(`${path}/players/${this.selected_team}`, config)
        .then((response) => {
          this.all_players = response.data.response_data;
          this.loader = 0;
        })
        .catch((err) => {
          this.handle_error(err);
        });
    },

    // Add Player
    add_new_player: function () {
      this.showDetails = false;
    },

    // Get ID of clicked Player
    get_id: function (e) {
      let element = e.target;
      while (!element.classList.contains("players-main-container")) {
        element = element.parentElement;
      }
      return element;
    },
    // Remove Player
    delete_player: function (e) {
      let player_id = this.get_id(e).getAttribute("player-id");
      let config = this.get_access_token();
      axios
        .delete(`${path}/players/${player_id}`, config)
        .then(() => {
          this.flashMessage.warning({
            message: "Player Removed",
          });

          this.get_players();
        })
        .catch((err) => {
          this.handle_error(err);
        });
    },
    // Edit Player Info
    save_player: function (e) {
      let player_id = this.get_id(e).getAttribute("player-id");
      this.editing = !this.editing;
      let current_player_container = this.get_id(e);
      let current_player_id =
        current_player_container.getAttribute("player-id");
      let current_player_position = current_player_container.children[0].value;
      let current_player_full_name =
        current_player_container.children[1].children[0].value;
      let current_player_fname = current_player_full_name.split(" ")[0];
      let current_player_lname = current_player_full_name.split(" ")[1];
      let updated_player_data = {
        id: current_player_id,
        position: current_player_position,
        fname: current_player_fname,
        lname: current_player_lname,
      };
      let config = this.get_access_token();
      axios
        .patch(`${path}/players/${player_id}`, { updated_player_data }, config)
        .then(() => {
          this.flashMessage.success({
            message: "Player Inforamtion Updated Successfully!",
          });
          this.get_players();
        })
        .catch((err) => {
          this.handle_error(err);
        });
    },
    edit_player: function () {
      this.editing = !this.editing;
    },
    save_new_player: function () {
      let new_player = {
        position: this.new_player_position,
        fname: this.new_player_fname,
        lname: this.new_player_lname,
        team: this.new_player_team,
      };
      let config = this.get_access_token();

      axios
        .post(`${path}/players/1`, { new_player }, config)
        .then((response) => {
          // If Duplicate Resource
          if (response.status == 209) {
            this.flashMessage.error({ message: response.data["message"] });
          } else {
            this.showDetails = !this.showDetails;
            this.flashMessage.success({ message: "Player Added" });
            this.get_players();
            this.new_player_position = "";
            this.new_player_fname = "";
            this.new_player_lname = "";
            this.new_player_team = "";
          }
        })
        .catch((err) => {
          this.handle_error(err);
        });
    },
    cancel_new_player: function () {
      this.showDetails = !this.showDetails;
      this.flashMessage.warning({
        message: "Canceled Adding New Player",
      });
    },
  },
};
</script>
