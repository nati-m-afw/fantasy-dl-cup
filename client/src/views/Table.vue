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
          <tr>
            <td id="IT"><span></span><i class="fas fa-minus"></i></td>
            <td>
              <i class="fas fa-check-circle"></i
              ><i class="fas fa-check-circle"></i
              ><i class="fas fa-check-circle"></i
              ><i class="fas fa-check-circle"></i
              ><i class="fas fa-check-circle"></i>
            </td>
            <td>15</td>
            <td>5</td>
            <td>5</td>
            <td>0</td>
            <td>0</td>
            <td>23</td>
            <td>7</td>
            <td>16</td>
          </tr>
          <tr>
            <td id="Bio"><span></span> <i class="fas fa-caret-up"></i></td>
            <td>
              <i class="fas fa-check-circle"></i
              ><i class="fas fa-times-circle"></i
              ><i class="fas fa-times-circle"></i
              ><i class="fas fa-check-circle"></i
              ><i class="fas fa-check-circle"></i>
            </td>
            <td>12</td>
            <td>6</td>
            <td>4</td>
            <td>0</td>
            <td>2</td>
            <td>23</td>
            <td>10</td>
            <td>13</td>
          </tr>
          <tr>
            <td id="ElecC"><span></span> <i class="fas fa-caret-down"></i></td>
            <td>
              <i class="fas fa-minus-circle"></i
              ><i class="fas fa-check-circle"></i
              ><i class="fas fa-times-circle"></i
              ><i class="fas fa-check-circle"></i
              ><i class="fas fa-check-circle"></i>
            </td>
            <td>10</td>
            <td>5</td>
            <td>3</td>
            <td>1</td>
            <td>1</td>
            <td>13</td>
            <td>8</td>
            <td>5</td>
          </tr>
          <tr>
            <td id="Che"><span></span> <i class="fas fa-caret-down"></i></td>
            <td>
              <i class="fas fa-times-circle"></i
              ><i class="fas fa-check-circle"></i
              ><i class="fas fa-check-circle"></i
              ><i class="fas fa-minus-circle"></i>
              <i class="fas fa-times-circle"></i>
            </td>
            <td>10</td>
            <td>6</td>
            <td>3</td>
            <td>1</td>
            <td>2</td>
            <td>16</td>
            <td>16</td>
            <td>0</td>
          </tr>
          <tr>
            <td id="Soft"><span></span> <i class="fas fa-minus"></i></td>
            <td>
              <i class="fas fa-times-circle"></i
              ><i class="fas fa-check-circle"></i
              ><i class="fas fa-check-circle"></i
              ><i class="fas fa-check-circle"></i
              ><i class="fas fa-times-circle"></i>
            </td>
            <td>9</td>
            <td>5</td>
            <td>3</td>
            <td>0</td>
            <td>2</td>
            <td>17</td>
            <td>7</td>
            <td>10</td>
          </tr>
          <tr>
            <td id="Mech"><span></span> <i class="fas fa-minus"></i></td>
            <td>
              <i class="fas fa-minus-circle"></i
              ><i class="fas fa-check-circle"></i
              ><i class="fas fa-check-circle"></i
              ><i class="fas fa-minus-circle"></i
              ><i class="fas fa-times-circle"></i>
            </td>
            <td>8</td>
            <td>5</td>
            <td>2</td>
            <td>2</td>
            <td>1</td>
            <td>11</td>
            <td>7</td>
            <td>4</td>
          </tr>
          <tr>
            <td id="Civ"><span></span> <i class="fas fa-minus"></i></td>
            <td>
              <i class="fas fa-times-circle"></i
              ><i class="fas fa-times-circle"></i
              ><i class="fas fa-times-circle"></i
              ><i class="fas fa-check-circle"></i
              ><i class="fas fa-check-circle"></i>
            </td>
            <td>6</td>
            <td>5</td>
            <td>2</td>
            <td>0</td>
            <td>3</td>
            <td>11</td>
            <td>15</td>
            <td>-4</td>
          </tr>
          <tr>
            <td id="ElecB1"><span></span> <i class="fas fa-minus"></i></td>
            <td>
              <i class="fas fa-times-circle"></i
              ><i class="fas fa-times-circle"></i
              ><i class="fas fa-times-circle"></i
              ><i class="fas fa-check-circle"></i
              ><i class="fas fa-times-circle"></i>
            </td>
            <td>3</td>
            <td>5</td>
            <td>1</td>
            <td>0</td>
            <td>4</td>
            <td>15</td>
            <td>28</td>
            <td>-13</td>
          </tr>
          <tr>
            <td id="ElecB2"><span></span> <i class="fas fa-minus"></i></td>
            <td>
              <i class="fas fa-times-circle"></i
              ><i class="fas fa-times-circle"></i
              ><i class="fas fa-times-circle"></i
              ><i class="fas fa-times-circle"></i>
            </td>
            <td>0</td>
            <td>4</td>
            <td>0</td>
            <td>0</td>
            <td>4</td>
            <td>2</td>
            <td>17</td>
            <td>-15</td>
          </tr>
          <tr>
            <td id="ElecA"><span></span> <i class="fas fa-minus"></i></td>
            <td>
              <i class="fas fa-times-circle"></i
              ><i class="fas fa-times-circle"></i
              ><i class="fas fa-times-circle"></i
              ><i class="fas fa-times-circle"></i>
            </td>
            <td>0</td>
            <td>4</td>
            <td>0</td>
            <td>0</td>
            <td>4</td>
            <td>5</td>
            <td>21</td>
            <td>-16</td>
          </tr>
        </tbody>
        <tfoot></tfoot>
      </table>
    </section>
  </div>
</template>
<script>
// import axios from "axios";
import Navigation from "../components/Navigation.vue";

export default {
  components: {
    navigation: Navigation,
  },
};
</script>
<style scoped>
@import "../assets/css/styles.css";
@import "../assets/css/table.css";
</style>
