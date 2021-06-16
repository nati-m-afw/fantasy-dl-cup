<template>
  <div class="body">
    <!-- Allows for Message Flashing -->
    <div class="form-container">
      <FlashMessage></FlashMessage>

      <h1 class="header">
        Welcome <br />
        Back
        <img class="cool-text" src="../assets/img/cool-text.png" alt="">
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

<style scoped>
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
.flash-message {
  margin-left: auto;
  margin-right: auto;
  background-color: #37fd12 !important;
}
.error {
  border-bottom: #ff0800 2px solid !important;
}
.success {
  border-bottom: #37fd12 2px solid !important;
}
input:focus {
  outline: none;
}

/* Main Styles */
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
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

.form-container {
  width: 500px;
  min-height: 640px;
  background: radial-gradient(circle, #009bde1c, #926fd66c, #003087ac 115%);
  backdrop-filter: blur(8px);
  /* background: var(--secondary-color); */
  color: var(--secondary-color);
  padding: 5% 3%;
}

.header {
  font-family: Poppins;
  font-size: 2rem;
  letter-spacing: 2px;
  font-weight: bold;
  line-height: 1.2;
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

.email-area,
.password-area {
  margin-bottom: 5%;
  margin-top: 5%;
  padding: 1%;
  display: flex;
  flex-direction: column;
}

.label {
  font-family: "Poppins";
  font-size: 16px;
  margin-bottom: 2%;
}

.email-input-container,
.password-input-container {
  display: flex;
  align-items: center;
}

.i {
  margin-top: 2%;
  color: gray;
  opacity: 60%;
  width: 18px !important;
  height: auto;
}

.email-input,
.password-input {
  outline: none;
  border: none;
  border-bottom: 1px solid black;
  width: 100%;
  font-size: 18px;
  font-family: "SourceSans";
  padding: 2%;
  border-radius: 0 0 10px 10px;
}

.submit-container {
  display: flex;
  flex-direction: column;
}

.forgot-password {
  align-self: flex-end;

  font-family: "Poppins";
  width: fit-content;
  margin-bottom: 30px;
}

.login-button {
  font-family: "Poppins";
  font-size: 20px;
  letter-spacing: 0.8px;
  width: 100%;
  padding: 2% 0;
  margin-bottom: 10%;
  position: relative;
  border: 1px solid black;
  border-radius: 0 0 5px 5px;
  background: var(--primary-color);
  color: var(--secondary-color);
}

.login-button:after {
  content: "";
  width: 100%;
  height: 5px;
  background: linear-gradient(
    40deg,
    #dc143c,
    #e22f72,
    #c071c7,
    #8d9fed,
    #78b0f6,
    #5ffbf1
  );
  background-size: 400%;
  position: absolute;
  z-index: -1;
  top: 99%;
  left: 0;
  border-radius: inherit;
  animation: glimmer 20s infinite alternate;
}

.login-button:active {
  transform: translateY(5px);
}

.login-button:active:after {
  width: 0;
}

@keyframes glimmer {
  0% {
    background-position: 0;
  }
  100% {
    background-position: 100%;
  }
}

.form-container a {
  color: hsl(348, 100%, 60%);
  text-decoration: none;
  font-weight: bold;
}

.sso-container {
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  margin-bottom: 10%;
}

.google-login,
.github-login,
.facebook-login {
  width: 55px;
  height: 55px;
  border-radius: 50%;
  border: none;
  padding: 0px !important;
  margin: 0px;
  transition: 1s all;
  background-color: rgba(255, 255, 255, 0);
}

.google-login,
.github-login,
.facebook-login {
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center;
}

.google-login:hover,
.github-login:hover,
.facebook-login:hover {
  transform: scale(1.2);
}
.google-login {
  background-image: url("../assets/icons/Google_Icon.svg");
}
.github-login {
  background-image: url("../assets/icons/Github_Icon.svg");
}
.facebook-login {
  background-image: url("../assets/icons/Facebook_Icon.svg");
}

.form-footer {
  text-align: center;
}

.redirect-info,
.redirect-link {
  font-family: "Poppins";
  font-size: 1rem;
}
.redirect-info {
  margin-right: 1%;
}
</style>

<script>
import firebase from "firebase";
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
    };
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
          this.flashMessage.error({
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
          this.flashMessage.error({
            message: err.message,
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
              this.flashMessage.error({
                message: `${err.message}`,
              });
            }
          );
      } else {
        this.flashMessage.error({
          message: "Please check your input.",
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
                this.flashMessage.error({
                  message: err.message,
                });
              });
          },
          () => {
            // Call Error Handler Function
            this.flashMessage.error({
              message: `Email ${this.email} with a different Provider`,
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
