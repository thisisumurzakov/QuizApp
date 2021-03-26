<template>
  <v-app style="background: #424242">
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
.pageTransition-enter {
  opacity: 0;
}
.pageTransition-enter-active {
  transition: opacity 0.2s;
}
.pageTransition-leave-active {
  transition: opacity 0.2s;
}
.pageTransition-leave-to {
  opacity: 0;
}
</style>
