<template>
  <div class="body">
    <nav>
      <h1>DL Cup Fantasy</h1>
    </nav>
    <navigation :activePage="'Table'" />
    <section id="table_container">
      <table>
        <thead>
          <tr>
            <th></th>
            <th>Last 5</th>
            <th id="Pts" title="Total Points">Pts</th>
            <th id="Pl" title="Games Played">Pl</th>
            <th id="W" title="Won">W</th>
            <th id="D" title="Drawn">D</th>
            <th id="L" title="Lost">L</th>
            <th><abbr title="Goals for">GF</abbr></th>
            <th><abbr title="Goals against">GA</abbr></th>
            <th><abbr title="Goal Difference">GD</abbr></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="team in table" :key="team">
            <td>{{ team.teamName }}<i class="fas fa-minus"></i></td>
            <td>
              <span v-for="result in team.last5" :key="result">
                <fa v-if="result == 'W'" class="i fas" icon="check-circle" />
                <fa
                  v-else-if="result == 'L'"
                  class="i fas"
                  icon="times-circle"
                />
                <fa v-else class="i fas" icon="minus-circle" />
              </span>
            </td>
            <td>{{ team.won * 3 + team.drawn }}</td>
            <td>{{ team.played }}</td>
            <td>{{ team.won }}</td>
            <td>{{ team.drawn }}</td>
            <td>{{ team.lost }}</td>
            <td>{{ team.GF }}</td>
            <td>{{ team.GA }}</td>
            <td>{{ team.GF - team.GA }}</td>
          </tr>
        </tbody>
        <tfoot></tfoot>
      </table>
    </section>
  </div>
</template>
<script>
import axios from "axios";
import Navigation from "../components/Navigation.vue";

export default {
  data() {
    return {
      table: {
        Biomed: [],
        Chemical: [],
        Elec: [],
        IT: [],
        Mech: [],
        SE: [],
      },
    };
  },
  components: {
    navigation: Navigation,
  },
  methods: {
    getTableData() {
      axios.get("http://127.0.0.1:5000/gettable").then((res) => {
        let i = 1;
        for (let team in this.table) {
          this.table[team] = res.data[i++];
        }
      });
    },
  },
  created() {
    this.getTableData();
  },
};
</script>
<style scoped>
@import "../assets/css/styles.css";
@import "../assets/css/table.css";
</style>
