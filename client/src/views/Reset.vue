<template>
  <div class="body">
    <!-- Allows for Message Flashing -->
    <FlashMessage :position="'top'"></FlashMessage>
    <div class="form-container">
      <h1 class="header">Reset Password</h1>

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

      <!-- Submit Button -->
      <div class="submit-container">
        <button @click="reset_password" class="login-button">Reset</button>
      </div>

      <div>
        <span class="redirect-info">Don't want to be here?</span>

        <router-link to="/login">
          <a class="redirect-link">Go Back.</a></router-link
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
  height: 100vh;
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
  height: 500px;
  background-color: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  margin-left: auto;
  margin-right: auto;
  margin-top: 12%;
  padding: 5%;
}
.header {
  font-family: "Poppins";
  letter-spacing: 2px;
  font-weight: 400;
  margin-bottom: 10%;
}

.email-area {
  margin-bottom: 5%;
  margin-top: 12%;
  padding: 1%;
  display: flex;
  flex-direction: column;
}

.label {
  font-family: "Poppins";
  font-size: 16px;
  margin-bottom: 2%;
}
.email-input-container {
  display: flex;
  align-items: center;
}
.i {
  margin-top: 2%;
  color: gray;
  opacity: 60%;
}
.email-input {
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
  margin-top: 12%;
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
  font-size: 18px;
}
</style>

<script>
import firebase from "firebase";
import "firebase/auth";
export default {
  name: "Reset",
  data() {
    return {
      email: "",
    };
  },
  methods: {
    //   Function for live validation

    // For Email
    validate_email_live: function (e) {
      if (
        /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(
          this.email
        )
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

    // For Password
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
        if (!e.target.classList.contains("error"))
          e.target.classList.toggle("error");
        this.$refs.password_icon.style.color = "red";
      }
    },

    // Final Validation For Email
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

    // Function to send reset verification
    reset_password: function () {
      if (this.validate_email() && this.email != "") {
        firebase
          .auth()
          .sendPasswordResetEmail(this.email)
          .then(() => {
            // Show Success Message
            this.flashMessage.success({
              message: `Reset link has been sent to ${this.email}`,
            });

            // Redirect to Login Page
            this.$router.push({ name: "Login" });
          })
          .catch((err) => {
            this.flashMessage.error({
              message: err.message,
            });
          });
      } else {
        this.flashMessage.error({
          message: "Invalid credentials",
        });
      }
    },
  },
};
</script>
