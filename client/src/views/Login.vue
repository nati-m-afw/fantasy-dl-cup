<template>
  <div class="body">
    <!-- Allows for Message Flashing -->
    <div class="form-container">
      <FlashMessage></FlashMessage>

      <h1 class="header">
        Welcome <br />
        Back
      </h1>

      <!-- Email Input -->
      <div class="email-area">
        <label for="email" class="label">Email</label>
        <div class="email-input-container">
          <!-- <fa class="i" icon="user" size="1x" ref="username_icon" /> -->
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
        <a href="/reset" class="forgot-password">Forgot Password?</a>
        <button @click="email_login" class="login-button">Login</button>
      </div>

      <!-- Alert -->
      <div style="position:relative;">
        <alert :msg="alertMsg" v-if="showMsg" />
      </div>

      <div class="sso-container">
        <button @click="google_login" class="google-login"></button>

        <button @click="github_login" class="github-login"></button>

        <button @click="facebook_login" class="facebook-login"></button>
      </div>
      <!-- <fa icon="facebook" class="i" size="7x" /> -->
      <div class="form-footer">
        <span class="redirect-info">Don't have an account yet?</span>

        <router-link to="/register">
          <a class="redirect-link">Register Here.</a></router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
import firebase from "firebase";
import Alert from "../components/Alert.vue";
import "firebase/auth";

// Random Word Generator
import randomWords from "random-words";
import axios from "axios";
let path = "http://localhost:5000/auth";

export default {
  name: "Login",

  data() {
    return {
      email: "",
      password: "",
      providerName: "",

      alertMsg: "",

      showMsg: false,
    };
  },

  components: {
    alert: Alert,
  },

  methods: {
    // For Email Live
    validate_email_live: function (e) {
      if (
        /^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})*$/.test(this.email)
      ) {
        e.target.classList.remove("error");
        e.target.classList.add("success");
        this.$refs.username_icon.style.color = "#37FD12";
      } else {
        e.target.classList.remove("success");
        e.target.classList.remove("error");
        e.target.classList.add("error");

        this.$refs.username_icon.style.color = "#FF0800";
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
        this.$refs.password_icon.style.color = "#37FD12";
      } else {
        e.target.classList.remove("success");
        e.target.classList.remove("error");
        e.target.classList.add("error");

        this.$refs.password_icon.style.color = "#FF0800";
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
    update_api: function (user_info) {
      axios
        .post(`${path}/signuser`, { user_info })
        .then(() => {})
        .catch((err) => {
          // this.flashMessage.error({
          //   message: err.message,
          // });
          this.alertMsg = err.message;
          this.showMsg = false;
          this.$nextTick (() => {
          // add my-component component in DOM
            this.showMsg = true;
          });
        });
    },

    // Function to get id from firebase_id
    get_user_id: function () {
      axios
        .post(`${path}/getUserID/${this.firebase_id}`)
        .then(async (response) => {
          this.user_id = await response.data.id;
          this.team_name = await response.data.team_name;

          // Check if valid user_id returned
          if (this.user_id) {
            // Update store state
            this.$store.commit("setCurrentUserID", this.user_id);
            this.$store.commit("setMyTeamName", this.team_name);
            sessionStorage.setItem("token", response.data.token);
            // this.$store.dispatch("getActiveGameweek");
          }

          this.$router.push("/myteam");
        })
        .catch((err) => {
          // this.flashMessage.error({
          //   message: err.message,
          // });
          this.alertMsg = err.message;
          this.showMsg = false;
          this.$nextTick (() => {
          // add my-component component in DOM
            this.showMsg = true;
          });
        });
    },

    // Function for firebase Login with email and password
    email_login: function () {
      // If Data is valid
      if (
        this.validate_email()
        // && this.validate_password()
      ) {
        // Call Firebase API
        firebase
          .auth()
          .signInWithEmailAndPassword(this.email, this.password)
          .then(
            async () => {
              // Get Current User
              let user = firebase.auth().currentUser;
              this.firebase_id = user.uid;
              // Function to call api route for adding to db (Incase the call during registration was inturrepted)
              this.update_api({
                firebase_id: this.firebase_id,
                fname: "Full",
                lname: "Name",
                team_name: randomWords(),
              });

              // GET USER ID
              // Redirect to MyTeam Component in get_user_id
              this.get_user_id(this.firebase_id);

              // Flash Success Message at Login
            },
            // If User email is already in use in firebase
            (err) => {
              // this.flashMessage.error({
              //   message: `${err.message}`,
              // });
              this.alertMsg = err.message;
              this.showMsg = false;
              this.$nextTick (() => {
              // add my-component component in DOM
                this.showMsg = true;
              });
            }
          );
      } else {
        // this.flashMessage.error({
        //   message: "Please check your input.",
        // });
        this.alertMsg = "Please check your input.";
        this.showMsg = false;
        this.$nextTick (() => {
        // add my-component component in DOM
          this.showMsg = true;
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
                // this.flashMessage.error({
                //   message: err.message,
                // });
                this.alertMsg = err.message;
                this.showMsg = false;
                this.$nextTick (() => {
                // add my-component component in DOM
                  this.showMsg = true;
                });
              });
          },
          () => {
            // Call Error Handler Function
            // this.flashMessage.error({
            //   message: `Email ${this.email} with a different Provider`,
            // });
            this.alertMsg = `Email ${this.email} with a different Provider`;
            this.showMsg = false;
            this.$nextTick (() => {
            // add my-component component in DOM
              this.showMsg = true;
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

.header {
  position: relative;
}

.header > img {
  position: absolute;
  right: 0;
  bottom: -25%;
  width: 10vmax;
  animation: rotate 4s infinite ease-in-out;
}

@keyframes rotate {
  0% {
    transform: rotate(0deg);
  }
  80% {
    transform: rotate(360deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

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
