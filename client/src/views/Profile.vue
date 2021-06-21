<template>
  <div class="sub-body">
    <FlashMessage :position="'top'"></FlashMessage>
    <div class="top">
      <nav>
        <h1>DL Cup Fantasy</h1>
      </nav>
      <navigation></navigation>
    </div>
    <div class="bottom">
      <div class="accordion accordion-flush" id="accordionFlushExample">
        <!-- General Information Section -->
        <div class="accordion-item">
          <h2 class="accordion-header" id="flush-headingOne">
            <!-- Accordion Button -->
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#flush-collapseOne"
              aria-expanded="false"
              aria-controls="flush-collapseOne"
            >
              General Information
            </button>
            <!-- Accordion Button -->
          </h2>
          <div
            id="flush-collapseOne"
            class="accordion-collapse collapse"
            aria-labelledby="flush-headingOne"
            data-bs-parent="#accordionFlushExample"
          >
            <div class="accordion-body">
              <spinner v-show="sendingInfo"></spinner>
              <!-- Full Name Container -->
              <div class="full-name-container">
                <!-- First Name Container -->
                <div class="first-name-container">
                  <label for="firstName">First Name :</label>
                  <input
                    type="text"
                    name="firstName"
                    v-model="firstName"
                    @keyup="validate_name_live($event, firstName)"
                  />
                </div>
                <!-- First Name Container -->

                <!-- Last Name Container -->
                <div class="last-name-container">
                  <label for="lastName">Last Name :</label>
                  <input
                    type="text"
                    name="lastName"
                    v-model="lastName"
                    @keyup="validate_name_live($event, lastName)"
                  />
                </div>
                <!-- Last Name Container -->
              </div>
              <!-- Full Name Container -->

              <!-- Team Name Container -->
              <div class="team-name-container">
                <label for="teamName">Team Name :</label>
                <input
                  type="text"
                  name="teamName"
                  v-model="teamName"
                  @keyup="validate_team_live"
                />
              </div>
              <!-- Team Name Container -->

              <!-- Save Button -->
              <div class="save-container">
                <button class="save-button" @click="save_general_info">
                  Save
                </button>
              </div>
              <!-- Save Button -->
            </div>
          </div>
        </div>
        <!-- General Information Section -->

        <!-- Email Change Section -->
        <div class="accordion-item">
          <h2 class="accordion-header" id="flush-headingTwo">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#flush-collapseTwo"
              aria-expanded="false"
              aria-controls="flush-collapseTwo"
            >
              Email Information
            </button>
          </h2>
          <div
            id="flush-collapseTwo"
            class="accordion-collapse collapse"
            aria-labelledby="flush-headingTwo"
            data-bs-parent="#accordionFlushExample"
          >
            <div class="accordion-body">
              <spinner v-show="sendingInfo"></spinner>
              <!-- Current Email Section -->
              <div class="email-container">
                <label for="currentEmail">Email :</label>
                <input
                  type="email"
                  name="currentEmail"
                  v-model="currentEmail"
                  @keyup="validate_email_live($event, currentEmail)"
                />
              </div>
              <!-- Current Email Section -->

              <!-- New Email Section -->
              <div class="new-email-container">
                <label for="newEmail">New Email :</label>
                <input
                  type="email"
                  name="newEmail"
                  v-model="newEmail"
                  @keyup="validate_email_live($event, newEmail)"
                />
              </div>
              <!-- New Email Section -->

              <!-- Password  Section -->
              <div class="password-container">
                <label for="password">Password :</label>
                <input
                  type="password"
                  name="password"
                  v-model="password"
                  @keyup="validate_password_live"
                />
              </div>
              <!-- Password Section -->

              <!-- Save Button -->
              <div class="save-container">
                <button class="save-button" @click="save_email_info">
                  Save
                </button>
              </div>
              <!-- Save Button -->
            </div>
          </div>
        </div>
        <!-- Email Change Section -->

        <!-- Password Reset -->
        <div class="accordion-item">
          <h2 class="accordion-header" id="flush-headingThree">
            <button
              class="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#flush-collapseThree"
              aria-expanded="false"
              aria-controls="flush-collapseThree"
            >
              Password Reset
            </button>
          </h2>
          <div
            id="flush-collapseThree"
            class="accordion-collapse collapse"
            aria-labelledby="flush-headingThree"
            data-bs-parent="#accordionFlushExample"
          >
            <div class="accordion-body">
              <button
                class="reset-button"
                @click="send_reset_email"
                v-show="!sendingInfo"
              >
                Send Reset Link
              </button>
              <spinner v-show="sendingInfo"></spinner>
            </div>
          </div>
        </div>
        <!-- Password Reset -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import firebase from "firebase";
import "firebase/auth";
import Spinner from "../components/Spinner.vue";
import Navigation from "../components/Navigation.vue";

const path = "https://fantasydl.pythonanywhere.com";

export default {
  data() {
    return {
      user_id: "",
      firstName: "",
      lastName: "",
      teamName: "",
      currentEmail: "yourcurrentemail@gmail.com",
      newEmail: "example@youmail.com",
      password: "password",
      sendingInfo: false,
    };
  },
  components: {
    spinner: Spinner,
    navigation: Navigation,
  },
  mounted() {
    // Get User General Information
    let user_id = sessionStorage.getItem("user-id");
    this.user_id = user_id;

    let access_token = sessionStorage.getItem("token");

    // Prepare a header config
    let config = {
      headers: {
        Authorization: `Bearer ${access_token}`,
      },
    };
    axios
      .get(`${path}/auth/profile/${user_id}`, config)
      .then((response) => {
        this.firstName = response.data.fname;
        this.lastName = response.data.lname;
        this.teamName = response.data.teamname;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  methods: {
    // Validation Functions

    // For Full Name Live
    validate_name_live: function (e, itemChecked) {
      if (itemChecked.length >= 5) {
        e.target.classList.remove("error");
        e.target.classList.add("success");
      } else {
        e.target.classList.remove("success");
        e.target.classList.remove("error");
        e.target.classList.add("error");
      }
    },
    // For Full Name Final
    validate_name: function (itemChecked) {
      if (itemChecked.length >= 5) {
        return true;
      }
      return false;
    },

    // For Team Name Live
    validate_team_live: function (e) {
      if (
        /^(?!.*\.\.)(?!.*\.$)[^\W][\w.]{0,29}$/.test(this.teamName) &&
        this.teamName.length >= 5
      ) {
        e.target.classList.remove("error");
        e.target.classList.add("success");
      } else {
        e.target.classList.remove("success");
        e.target.classList.remove("error");
        e.target.classList.add("error");
      }
    },
    // For Team Name Final
    validate_team: function () {
      if (
        /^(?!.*\.\.)(?!.*\.$)[^\W][\w.]{0,29}$/.test(this.teamName) &&
        this.teamName.length >= 5
      ) {
        return true;
      }
      return false;
    },

    // For Email Live
    validate_email_live: function (e, itemChecked) {
      if (
        /^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})*$/.test(itemChecked)
      ) {
        e.target.classList.remove("error");
        e.target.classList.add("success");
      } else {
        e.target.classList.remove("success");
        e.target.classList.remove("error");
        e.target.classList.add("error");
      }
    },

    // For Email Final
    validate_email: function (itemChecked) {
      if (
        /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(
          itemChecked
        )
      ) {
        return true;
      }
      return false;
    },

    // Live Validation For Password Live
    validate_password_live: function (e) {
      if (
        /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/.test(
          this.password
        )
      ) {
        e.target.classList.remove("error");
        e.target.classList.add("success");
      } else {
        e.target.classList.remove("success");
        e.target.classList.remove("error");
        e.target.classList.add("error");
      }
    },

    // Final Check For Password Final
    validate_password: function () {
      if (
        /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/.test(
          this.password
        )
      ) {
        return true;
      }
      return false;
    },

    // Get Access Token
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
    // Function to save general info
    save_general_info: function () {
      // Validate Inputs
      if (
        this.validate_name(this.firstName) &&
        this.validate_name(this.lastName) &&
        this.validate_team()
      ) {
        this.sendingInfo = true;
        let new_info = {
          id: this.user_id,
          fname: this.firstName,
          lname: this.lastName,
          teamname: this.teamName,
        };
        let config = this.get_access_token();
        axios
          .patch(`${path}/auth/profile/${this.user_id}`, { new_info }, config)
          .then(() => {
            this.sendingInfo = false;
            this.flashMessage.success({
              message: "Information Updated Successfully",
            });
          })
          .catch((err) => {
            this.sendingInfo = false;
            console.log(err);
          });
      } else {
        this.flashMessage.error({ message: "Invalid Inputs" });
      }
    },
    save_email_info: function () {
      // Validate Inputs
      if (
        this.validate_email(this.newEmail) &&
        this.validate_email(this.currentEmail)
        // && this.validate_email(this.password)
      ) {
        this.sendingInfo = true;
        firebase
          .auth()
          .signInWithEmailAndPassword(this.currentEmail, this.password)
          .then((userCredential) => {
            userCredential.user.updateEmail(this.newEmail);
            this.sendingInfo = false;
            this.flashMessage.success({
              message: `Email Successfully Updated to`,
            });
          })
          .catch((err) => {
            this.sendingInfo = false;
            if (
              err.code == "auth/user-not-found" ||
              err.code == "auth/wrong-password"
            ) {
              this.flashMessage.error({
                message: "Invalid username and/or password",
              });
            } else if (err.code == "auth/email-already-in-use") {
              this.flashMessage.error({ message: "Email/Auth already in use" });
            } else {
              console.log(err);
            }
          });
      } else {
        this.flashMessage.error({ message: "Invalid Inputs" });
      }
    },
    send_reset_email: function () {
      this.sendingInfo = true;
      let user_id = sessionStorage.getItem("user-id");
      let config = this.get_access_token();
      axios
        .get(`${path}/auth/profile/firebaseID/${user_id}`, config)
        .then((response) => {
          let firebase_id = response.data.firebase_id;
          axios
            .get(`${path}/auth/profile/email/${firebase_id}`, config)
            .then((response) => {
              let email = response.data.email;
              firebase
                .auth()
                .sendPasswordResetEmail(email)
                .then(() => {
                  this.sendingInfo = false;
                  this.flashMessage.success({
                    message: `Reset Email has been sent to email ${email}`,
                  });
                })
                .catch((err) => {
                  console.log(err);
                });
            })
            .catch((err) => {
              console.log(err);
            });
        })
        .catch((err) => {
          console.log(err);
        });
      // firebase
      //   .auth()
      //   .sendPasswordResetEmail("thomas2alexmech@gmail.com")
      //   .then(() => {
      //     console.log("Done");
      //   })
      //   .catch((err) => {
      //     console.log(err);
      //   });
    },
  },
};
</script>

<style scoped>
/* Dynamic Styles */
.error {
  border-bottom: red 2px solid !important;
}
.success {
  border-bottom: green 2px solid !important;
}
@font-face {
  font-family: "Futura";
  src: local("Futura"),
    url("../assets/fonts/Futura/FuturaPTMedium.otf") format("truetype");
}
.sub-body {
  width: 100%;
  height: 100vh;
}
.top {
  width: 100%;
  height: 15vh;
}
.bottom {
  width: 100%;
  margin-top: 5%;
  background-color: gainsboro;
}
.accordion-item,
.accordion-header,
.accordion-button {
  outline: none !important;
}
.accordion-item {
  background-color: gainsboro;
}
.accordion-button {
  border-bottom: 1px solid black;
}
.accordion-button {
  height: 8vh;
  font-family: "Futura";
  font-size: 24px;
  letter-spacing: 1px;
}
.accordion-collapse {
  outline: none !important;
}
.accordion-body {
  display: flex;
  flex-direction: column;
  padding-top: 2%;
  padding-left: 8%;
  padding-right: 8%;
}
.full-name-container {
  display: flex;
  justify-content: space-between;
}

.first-name-container,
.last-name-container,
.team-name-container,
.email-container,
.new-email-container,
.password-container {
  display: flex;
  flex-direction: column;
  width: 40%;
}
.team-name-container {
  margin-top: 3%;
}
label {
  font-family: "Futura";
  letter-spacing: 1.2px;
  font-size: 22px;
  margin-bottom: 1.2%;
}
input {
  height: 38px;
  outline: none !important;
  border: 0.002px solid rgb(170, 167, 167);
  background-color: gainsboro;
  border-radius: 5px;
  padding: 0% 2% 0% 2%;
  font-size: 18px;
  font-weight: lighter;
}
.save-container {
  margin-top: 5%;
  text-align: end;
}
.save-button {
  width: 9%;
  border: 0.02px solid rgba(0, 0, 0, 0.527);
  outline: none !important;
  background-color: rgba(149, 17, 149, 0.863);
  color: gainsboro;
  font-size: 20px;
}

.new-email-container,
.password-container {
  margin-top: 2%;
}
.reset-button {
  width: 30%;
  margin-left: auto;
  margin-right: auto;
  padding-top: 1%;
  padding-bottom: 1%;
  font-size: 24px;
  letter-spacing: 2px;
  outline: none;
  border: 1px solid rgba(0, 0, 0, 0.829);
}
</style>
