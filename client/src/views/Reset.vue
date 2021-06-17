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
