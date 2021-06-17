<template>
  <div class="alert-body">
    <p>{{ msg }}</p>
  </div>
</template>

<script>
export default {
  props: ["msg"],
};
</script>
<style scoped>
@import "../assets/css/styles.css";

.alert-body {
  background-color: hsla(348, 73%, 47%, 0.767)!important;
  /* position: absolute; */
  color: white;
  font-family: montserrat-light;
  font-size: 1rem !important;
  margin-top: -42px;
  margin-bottom: 10px;
  border-radius: 0 0 10px 10px;
  animation: dissipate 5s forwards;
}

p {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin: 0;
}

@keyframes dissipate {
  0% {
    /* height: 100%; */
    width: 100%;
    opacity: 1;
  }
  70% {
    opacity: 1;
  }
  100% {
    /* height: 0; */
    width: 0;
    opacity: 0;
  }
}
</style>