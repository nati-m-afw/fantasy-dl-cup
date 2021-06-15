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
            <th @click="sortTable(2)" id="Pts" title="Total Points">Pts</th>
            <th @click="sortTable(3)" id="Pl" title="Games Played">Pl</th>
            <th @click="sortTable(4)" id="W" title="Won">W</th>
            <th @click="sortTable(5)" id="D" title="Drawn">D</th>
            <th @click="sortTable(6)" id="L" title="Lost">L</th>
            <th @click="sortTable(7)"><abbr title="Goals for">GF</abbr></th>
            <th @click="sortTable(8)"><abbr title="Goals against">GA</abbr></th>
            <th @click="sortTable(9)">
              <abbr title="Goal Difference">GD</abbr>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="team in table" :key="team">
            <td>{{ team.teamName }}<i class="fas fa-minus"></i></td>
            <td>
              <span v-for="(result, index) in team.last5" :key="result + index">
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
        team1: [],
        team2: [],
        team3: [],
        team4: [],
        team5: [],
        team6: [],
      },
    };
  },
  components: {
    navigation: Navigation,
  },
  methods: {
    // Function to get access token
    get_access_token: function () {
      // Get Token from Local Storage
      let access_token = localStorage.getItem("token");

      // Prepare a header config
      let config = {
        headers: {
          Authorization: `Bearer ${access_token}`,
        },
      };
      return config;
    },

    getTableData() {
      let config = this.get_access_token();
      axios.get("http://127.0.0.1:5000/gettable", config).then((res) => {
        let i = 1;
        for (let team in this.table) {
          this.table[team] = res.data[i++];
        }
      });
    },
    sortTable(n) {
      let table,
        rows,
        switching,
        i,
        x,
        y,
        shouldSwitch,
        dir,
        switchcount = 0;

      table = document.querySelector("table");
      switching = true;

      dir = "desc";

      while (switching) {
        switching = false;
        rows = table.rows;

        for (i = 1; i < rows.length - 1; i++) {
          shouldSwitch = false;

          x = rows[i].getElementsByTagName("td")[n];
          y = rows[i + 1].getElementsByTagName("td")[n];

          if (dir == "asc") {
            if (+x.innerHTML > +y.innerHTML) {
              shouldSwitch = true;
              break;
            }
          } else if (dir == "desc") {
            if (+x.innerHTML < +y.innerHTML) {
              shouldSwitch = true;
              break;
            }
          }
        }
        if (shouldSwitch) {
          rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
          switching = true;

          switchcount++;
        } else {
          if (switchcount == 0 && dir == "desc") {
            dir = "asc";
            switching = true;
          }
        }
      }
    },
  },
  created() {
    this.getTableData();
  },
  updated() {
    this.sortTable(2);
  },
};
</script>
<style scoped>
@import "../assets/css/styles.css";
@import "../assets/css/table.css";

th {
  cursor: pointer;
}
</style>
