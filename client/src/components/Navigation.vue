<template>
    <div class="sticky-nav">
        <router-link to="/myteam"  :class="activePage == 'MyTeam' ? 'active' : ''">My team</router-link>
        <router-link to="" :class="this.activePage == 'myTeam' ? 'active' : ''">Points</router-link>
        <router-link to="" :class="this.activePage == 'myTeam' ? 'active' : ''">Transfers</router-link>
        <router-link to="" :class="this.activePage == 'myTeam' ? 'active' : ''">League</router-link>
        <router-link to="" :class="this.activePage == 'myTeam' ? active : ''">Table</router-link>
        <router-link to="" :class="this.activePage == 'myTeam' ? 'active' : ''">Fixtures</router-link>
        <router-link to="" :class="this.activePage == 'myTeam' ? 'active' : ''">Stats</router-link>
    </div>
</template>

<script>
    export default {
        props: ["activePage"],
    };
</script>

<style scoped>

</style>