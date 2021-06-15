<template>
  <div class="spinner-container">
    <div class="d1"></div>
    <div class="d2"></div>
    <div class="d3"></div>
    <div class="d4"></div>
    <div class="d5"></div>
  </div>
</template>

<style>
.spinner-container {
  height: fit-content;
  width: 100px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.spinner-container div {
  background-color: greenyellow;
  border-radius: 30px;
  animation: wave 600ms forwards;
  animation-iteration-count: infinite;
}

:root {
  --animation-delay: 200ms;
}

div.d2,
div.d4 {
  animation-delay: calc(var(--animation-delay) * 2);
}

div.d3 {
  animation-delay: var(--animation-delay);
}

@keyframes wave {
  0% {
    height: 100px;
    width: 10px;
  }

  50% {
    height: 50px;
  }

  100% {
    height: 100px;
    width: 10px;
  }
}
</style>
