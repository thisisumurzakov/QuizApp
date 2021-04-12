<template>
  <v-app style="background: #212121">
    <v-main>
      <transition name="pageTransition" mode="out-in">
        <router-view/>
      </transition>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>

<style scoped>
</style>
