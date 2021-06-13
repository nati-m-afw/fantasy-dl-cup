<template>
  <div class="spinner">
    <div class="ball ball-1"></div>
    <div class="ball ball-2"></div>
    <div class="ball ball-3"></div>
    <div class="ball ball-4"></div>
  </div>
</template>
<style scoped>
.spinner {
  width: 150px;
  height: 30px;
  margin: 100px auto;
}
.ball {
  height: 30px;
  width: 30px;
  float: left;

  border-radius: 50%;
  margin-right: 10px;
}
.ball-1 {
  animation: jump3 1.8s infinite ease-out;
  background: rgba(0, 255, 0, 0.5);
}
.ball-2 {
  animation: jump2 1.8s infinite ease-out;
  background: rgba(255, 94, 0, 0.5);
}
.ball-3 {
  animation: jump1 1.8s infinite ease-out;
  background: rgba(0, 225, 255, 0.5);
}
.ball-4 {
  margin-right: 0;
  animation: wipe 1.8s infinite cubic-bezier(0.5, 0, 0.5, 1);
  background: rgba(255, 0, 0, 0.5);
}
@keyframes jump1 {
  12% {
    transform: translate(20px, -40px);
    animation-timing-function: ease-in;
  }
  24% {
    transform: translate(40px, 0);
  }
  100% {
    transform: translate(40px, 0);
  }
}
@keyframes jump2 {
  12% {
    transform: translate(0, 0);
  }
  24% {
    transform: translate(20px, -40px);
    animation-timing-function: ease-in;
  }
  36% {
    transform: translate(40px, 0);
  }
  100% {
    transform: translate(40px, 0);
  }
}
@keyframes jump3 {
  24% {
    transform: translate(0, 0);
  }
  36% {
    transform: translate(20px, -40px);
    animation-timing-function: ease-in;
  }
  48% {
    transform: translate(40px, 0);
  }
  100% {
    transform: translate(40px, 0);
  }
}
@keyframes wipe {
  48% {
    transform: translateX(-120px);
  }
  100% {
    transform: translateX(-120px);
  }
}
</style>

