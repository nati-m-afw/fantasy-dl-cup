<template>
  <div>
    <div id="info"></div>
    <div id="team_selection">
      <div id="transfer_field">
        <div class="goalkeepers">
          <i></i>
          <fa class="i" icon="user" size="7x" />
          <fa class="i" icon="user" size="7x" />
          <i></i>
        </div>
        <div class="defenders">
          <fa class="i" icon="user" size="7x" />
          <fa class="i" icon="user" size="7x" />
          <fa class="i" icon="user" size="7x" />
        </div>
        <div class="midfielders">
          <fa class="i" icon="user" size="7x" />
          <fa class="i" icon="user" size="7x" />
          <fa class="i" icon="user" size="7x" />
        </div>
        <div class="strikers">
          <i></i>
          <fa class="i" icon="user" size="7x" />
          <fa class="i" icon="user" size="7x" />
          <i></i>
        </div>
      </div>
      <div id="transfer_sidebar"></div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
* {
  box-sizing: border-box;
}

body {
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

#transfer_field {
  background-color: black;
  display: grid;

  grid-template-rows: repeat(4, 1fr);
}

#transfer_field > div {
  display: flex;

  justify-content: space-around;
  align-items: center;
}

.i {
  color: white;
  cursor: pointer;
}

#transfer_sidebar {
  background-color: white;
}
</style>