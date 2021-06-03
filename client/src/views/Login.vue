<template>
  <div class="body">
    <!-- Allows for Message Flashing -->
    <FlashMessage :position="'top'"></FlashMessage>
    <div class="form-container">
      <h1 class="header">Login</h1>

      <!-- Email Input -->
      <div class="email-area">
        <label for="email" class="label">Email</label>
        <div class="email-input-container">
          <fa class="i" icon="user" size="1x" ref="username_icon" />
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
          <fa class="i" icon="unlock" size="1x" ref="password_icon" />
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
      <div>
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
    url("../../public/fonts/Poppins-Regular.ttf") format("truetype");
}
@font-face {
  font-family: "SourceSans";
  src: local("SourceSans"),
    url("../../public/fonts/SourceSansPro-Regular.ttf") format("truetype");
}
/* Styling for dynamic stuff */
.flash-message {
  margin-left: auto;
  margin-right: auto;
  background-color: green !important;
}
.error {
  border-bottom: red 2px solid !important;
}
.success {
  border-bottom: green 2px solid !important;
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
  width: 100%;
  padding-botton: 5%;

  /* background: linear-gradient(to right, rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.45)),
    url("../../public/img/5273776.jpg"); */
  background: linear-gradient(to right, rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.45)),
    url("../../public/img/4799045.jpg");
  /* background-image: url("../../public/img/5295526.jpg"); */
  color: black;
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  display: flex;
  z-index: -1;
}
.form-container {
  width: 500px;
  min-height: 640px;
  /* background-color: rgba(255, 255, 255, 0.7);
   */
  background-color: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);

  margin-left: auto;
  margin-right: auto;
  margin-top: 3%;
  padding: 5%;
  margin-bottom: 3%;
}
.header {
  font-family: "Poppins";
  letter-spacing: 2px;
  font-weight: 400;
  margin-bottom: 10%;
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
  background-color: rgba(255, 255, 255, 0);

  outline: none;
  border-inline-color: none;

  border: none;
  border-bottom: 1px solid black;
  width: 100%;
  height: 32px;
  font-size: 18px;
  font-family: "SourceSans";
  font-weight: 100;
  padding-left: 0%;
  padding-right: 2%;
  margin-left: 2.5%;
}
.email-input {
  font-style: italic;
}
.submit-container {
  display: flex;
  flex-direction: column;
}
.forgot-password {
  width: 94%;
  text-align: right;

  margin-left: 6%;
  font-family: "Poppins";
  font-size: 14px;
  letter-spacing: 0.5px;
  opacity: 0.9;
  margin-bottom: 10%;
}
.login-button {
  background-color: rgba(255, 255, 255, 0);
  backdrop-filter: blur(5px);
  font-family: "Poppins";
  font-size: 20px;
  letter-spacing: 0.8px;
  width: 80%;
  margin-right: auto;
  margin-left: auto;
  padding-top: 2%;
  padding-bottom: 2%;
  border-radius: 15px;
  border: 1px solid black;
  margin-bottom: 10%;
  transition: 0.85s all;
}
.login-button:hover {
  transform: scale(1.1);
  background-color: teal;
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
  background-image: url("../../public/icons/icons8-google.svg");
}
.github-login {
  background-image: url("../../public/icons/icons8-github.svg");
}
.facebook-login {
  background-image: url("../../public/icons/icons8-facebook (1).svg");
}
.redirect-info,
.redirect-link {
  font-family: "Poppins";
  font-size: 14px;
}
.redirect-info {
  text-decoration: none;
  color: black;
  margin-right: 1%;
}
.redirect-link {
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
          this.team_name = await response.data.team_name

          // Add User ID to local storage or cookies
          // Update store state
          if (this.user_id){
            this.$store.commit("setCurrentUserID", this.user_id);
            this.$store.commit("setMyTeamName", this.team_name);
          }

          // Redirect to myTeam
          // console.log(this.$store.state.userId);
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
