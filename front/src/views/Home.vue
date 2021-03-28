<template>
  <div class="d-flex align-center" style="height: 100%; width: 100%;">
    <v-container class="justify-center d-flex">
      <v-btn
          class="bg-btn mr-3 title rounded-circle"
          height="300px"
          width="300px"
          color="success"
          to="/join"
      >
        Join quiz
      </v-btn>
      <v-btn
          class="bg-btn ml-3 title rounded-circle"
          height="300px"
          width="300px"
          color="warning"
      >
        Create quiz
      </v-btn>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
</style>
