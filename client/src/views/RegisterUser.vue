<template>
  <div class="body">
    <div class="form-container">
      <FlashMessage :position="'top'"></FlashMessage>

      <h1 class="header">Create Your <br />Team</h1>

      <!-- Team Name -->
      <div class="email-area">
        <label for="team-name" class="label">Team name</label>
        <div class="email-input-container">
          <!-- <fa class="i" icon="users" size="1x" ref="team_icon" /> -->
          <input
            class="email-input"
            type="text"
            name="team-name"
            v-model="team_name"
            @keyup="validate_team_live"
          />
        </div>
      </div>

      <!-- Full Name -->
      <div class="email-area">
        <label for="full-name" class="label">Fullname</label>
        <div class="email-input-container">
          <!-- <fa class="i" icon="user" size="1x" ref="name_icon" /> -->
          <input
            class="email-input"
            type="text"
            name="full-name"
            v-model="full_name"
            @keyup="validate_name_live"
          />
        </div>
      </div>

      <!-- Email Input -->
      <div class="email-area">
        <label for="email" class="label">Email</label>
        <div class="email-input-container">
          <!-- <fa class="i" icon="envelope" size="1x" ref="username_icon" /> -->
          <input
            class="email-input"
            type="text"
            name="email"
            v-model="email"
            @keyup="validate_email_live"
          />
        </div>
      </div>

      <!-- Password Input -->
      <div class="password-area">
        <label for="password" class="label">Password</label>
        <div class="password-input-container">
          <!-- <fa class="i" icon="unlock" size="1x" ref="password_icon" /> -->
          <input
            class="password-input"
            type="password"
            name="password"
            v-model="password"
            @keyup="validate_password_live"
          />
        </div>
      </div>

      <!-- Submit Button -->
      <div class="submit-container">
        <button @click="register_with_email" class="login-button">
          Register
        </button>
      </div>

      <div class="sso-container">
        <button @click="google_login" class="google-login"></button>

        <button @click="github_login" class="github-login"></button>

        <button @click="facebook_login" class="facebook-login"></button>
      </div>
      <!-- <fa icon="facebook" class="i" size="7x" /> -->
      <div>
        <span class="redirect-info">Already have an account?</span>

        <router-link to="/login">
          <a class="redirect-link">Login Here.</a></router-link
        >
      </div>
    </div>

    <!-- Email Input -->
  </div>
</template>

<script>
// Firebase Library
import firebase from "firebase/app";
import "firebase/auth";
import axios from "axios";

// Random Words Library
import randomWords from "random-words";
let path = "http://localhost:5000/auth";

export default {
  name: "Register",
  data() {
    return {
      email: "",
      password: "",
      providerName: "",
      firebase_id: "",
      team_name: "",
      full_name: "",
    };
  },
  methods: {
    // Validation Functions

    // For Team Name Live
    validate_team_live: function (e) {
      if (
        /^(?!.*\.\.)(?!.*\.$)[^\W][\w.]{0,29}$/.test(this.team_name) &&
        this.team_name.length >= 5
      ) {
        e.target.classList.remove("error");
        e.target.classList.add("success");
        this.$refs.team_icon.style.color = "green";
      } else {
        e.target.classList.remove("success");
        e.target.classList.remove("error");
        e.target.classList.add("error");
        this.$refs.team_icon.style.color = "red";
      }
    },
    // For Team Name Final
    validate_team: function () {
      if (
        /^(?!.*\.\.)(?!.*\.$)[^\W][\w.]{0,29}$/.test(this.team_name) &&
        this.team_name.length >= 5
      ) {
        return true;
      }
      return false;
    },

    // For Full Name Live
    validate_name_live: function (e) {
      if (/^[a-zA-Z\s]*$/.test(this.full_name) && this.full_name.length >= 5) {
        e.target.classList.remove("error");
        e.target.classList.add("success");
        this.$refs.name_icon.style.color = "green";
      } else {
        e.target.classList.remove("success");
        e.target.classList.remove("error");
        e.target.classList.add("error");
        this.$refs.name_icon.style.color = "red";
      }
    },
    // For Full Name Final
    validate_name: function () {
      if (/^[a-zA-Z\s]*$/.test(this.full_name) && this.full_name.length >= 5) {
        return true;
      }
      return false;
    },

    // For Email Live
    validate_email_live: function (e) {
      if (
        /^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})*$/.test(this.email)
      ) {
        e.target.classList.remove("error");
        e.target.classList.add("success");
        this.$refs.username_icon.style.color = "green";
      } else {
        e.target.classList.remove("success");
        e.target.classList.remove("error");
        e.target.classList.add("error");

        this.$refs.username_icon.style.color = "red";
      }
    },

    // For Email Final
    validate_email: function () {
      if (
        /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(
          this.email
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
        this.$refs.password_icon.style.color = "green";
      } else {
        e.target.classList.remove("success");
        e.target.classList.remove("error");
        e.target.classList.add("error");

        this.$refs.password_icon.style.color = "red";
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

    // Function to update db with firebase id
    update_api: async function (user_info) {
      axios
        .post(`${path}/signuser`, { user_info })
        .then(() => {})
        .catch((err) => {
          this.flashMessage.error({
            title: "Oops!",
            message: err.message,
          });
        });
    },

    // Function to get id from firebase_id
    get_user_id: function () {
      axios
        .post(`${path}/getUserID/${this.firebase_id}`)
        .then(async (response) => {
          this.user_id = await response.data.id;

          // Add User ID to vue store
          this.$store.commit("setCurrentUserID", this.user_id);
        })
        .catch((err) => {
          this.flashMessage.error({
            title: "Oops!",
            message: err.message,
          });
        });
    },

    // Function for firebase register with email and password
    register_with_email: function () {
      // If Data is valid
      if (
        this.validate_email() &&
        this.validate_team() &&
        this.validate_name()
        && this.validate_password()
      ) {
        // Call Firebase API
        firebase
          .auth()
          .createUserWithEmailAndPassword(this.email, this.password)
          .then(
            async () => {
              // Get Current User
              let user = firebase.auth().currentUser;
              this.firebase_id = user.uid;
              // Function to call api route for adding to db
              this.update_api({
                firebase_id: this.firebase_id,
                fname: this.full_name.split(" ")[0],
                lname: this.full_name.split(" ")[1],
                team_name: this.team_name,
              });
              // Redirect to login route
              this.$router.push({ name: "Login" });
              // GET USER ID
              this.get_user_id(this.firebase_id);
              // Flash Success Message at Login
              this.flashMessage.success({
                title: "Successfully Registered",
                message:
                  "Your Account has been created successfully. Please Sign in to continue",
              });
            },
            // If User email is already in use in firebase
            (err) => {
              this.flashMessage.error({
                title: "Oops!",
                message: `${err.message}`,
              });
            }
          );
      } else {
        this.flashMessage.error({
          title: "Invalid Credentials",
          message: "Please check you inputs",
          blockClass: "test",
          wrapperClass: "test",
          contentClass: "test",
        });
      }
    },

    // Function to handle SSO for all methods
    handle_sso: function () {
      // Find out the selected provider
      let provider;
      if (this.providerName == "Google") {
        provider = new firebase.auth.GoogleAuthProvider();
      } else if (this.providerName == "Github") {
        provider = new firebase.auth.GithubAuthProvider();
      } else if (this.providerName == "Facebook") {
        provider = new firebase.auth.FacebookAuthProvider();
      }

      // Call to firebase api
      firebase
        .auth()
        .signInWithPopup(provider)
        .then(
          async () => {
            // Get Current User
            let user = firebase.auth().currentUser;
            // Get Firebase_id
            this.firebase_id = user.uid;
            // If API displays Full Name
            if (user.displayName) {
              this.full_name = user.displayName;
            } else {
              this.full_name = "Full Name";
            }
            // Request for id with firebase_id
            axios
              .get(`${path}/getuser/${user.uid}`)
              .then((response) => {
                // If firebase_id in database
                if (response.data.code == "Error") {
                  // Redirect to Pick Team Component
                  this.$router.push({ name: "PickTeam" });

                  // Call Function to HANDLE ID SHARING
                  this.get_user_id(this.firebase_id);
                }
                // If new firebase_id
                else if (response.data.code == "Success") {
                  // Add firebase_id to DB
                  this.update_api({
                    firebase_id: this.firebase_id,
                    fname: this.full_name.split(" ")[0],
                    lname: this.full_name.split(" ")[1],
                    team_name: randomWords(),
                  });

                  // Redirect to Pick Team Component
                  this.$router.push({ name: "PickTeam" });
                  // GET ID of user
                  this.get_user_id(this.firebase_id);
                }
              })
              .catch((err) => {
                this.flashMessage.error({
                  title: "Oops!",
                  message: err.message,
                });
              });
          },
          () => {
            // Call Error Handler Function
            this.flashMessage.error({
              title: "Email already Associated with an account",
              message: "Registered with a different Provider",
            });
          }
        );
    },

    google_login: function () {
      this.providerName = "Google";
      this.handle_sso();
    },

    github_login: function () {
      this.providerName = "Github";

      this.handle_sso();
    },

    facebook_login: function () {
      this.providerName = "Facebook";

      this.handle_sso();
    },
  },
};
</script>

<style scoped>
@import "../assets/css/form-styles.css";

.body {
  min-height: 100vh;

  background: url("../assets/img/epic_waves.jpg");

  background-repeat: no-repeat;
  background-size: 150%;
  background-position: 10% 0;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}
</style>
