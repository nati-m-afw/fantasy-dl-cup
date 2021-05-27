<template>
  <div class="body">
    <div id="info"></div>
    <div id="team_selection">
      <div class="team">
        <div class="starting_team">
          <div><i class="fas fa-user"></i></div>
          <div>
            <i class="fas fa-user"></i><i class="fas fa-user"></i
            ><i class="fas fa-user"></i>
          </div>
          <div><i class="fas fa-user"></i><i class="fas fa-user"></i></div>
          <div><i class="fas fa-user"></i></div>
        </div>
        <div class="substitutes">
          <div>
            <i class="fas fa-user"></i><i class="fas fa-user"></i
            ><i class="fas fa-user"></i>
          </div>
        </div>
      </div>
      <div class="sidebar"></div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
* {
  box-sizing: border-box;
}

.body {
  margin: 0;
  min-height: 100vh;

  background-color: #696969;
  padding: 5%;
}

#info {
  width: 100%;
  display: flex;
}

#team_selection {
  display: grid;
  grid-template-columns: 65vw 20vw;
  grid-template-rows: 800px;
  grid-column-gap: 2vw;
}

.team {
  background-color: black;
  display: grid;
  color: white;

  grid-template-rows: auto 1fr;
}

.team > div > div {
  display: flex;

  justify-content: space-around;
  align-items: center;
}

.starting_team {
  display: grid;
  grid-template-rows: repeat(4, 1fr);
  grid-row-gap: 64px;
}

.substitutes {
  grid-row: -1;
}

i {
  color: white;
  cursor: pointer;

  font-size: 112px;
}

.sidebar {
  background-color: white;
  display: flex;
}
</style>