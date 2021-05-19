<template>
  <div>Pick Team</div>
  <div id="info"></div>
  <div id="team_selection">
      <div id="transfer_field">
          <div class="goalkeepers">
              <i></i>
              <i class="fas fa-user fa-7x"></i>
              <i class="fas fa-user fa-7x"></i>
              <i></i>
          </div>
          <div class="defenders">
              <i class="fas fa-user fa-7x"></i>
              <i class="fas fa-user fa-7x"></i>
              <i class="fas fa-user fa-7x"></i>
          </div>
          <div class="midfielders">
              <i class="fas fa-user fa-7x"></i>
              <i class="fas fa-user fa-7x"></i>
              <i class="fas fa-user fa-7x"></i>
          </div>
          <div class="strikers">
              <i></i>
              <i class="fas fa-user fa-7x"></i>
              <i class="fas fa-user fa-7x"></i>
              <i></i>
          </div>
      </div>
      <div id="transfer_sidebar"></div>
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

  #transfer_field>div {
      display: flex;

      justify-content: space-around;
      align-items: center;
  }

  i {
      color: white;
  }

  #transfer_sidebar {
      background-color: white;
  }
</style>