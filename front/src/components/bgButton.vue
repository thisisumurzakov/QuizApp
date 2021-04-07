<template>
  <v-col
      md="12"
      sm="12"
      class="justify-center d-flex"
  >
    <v-btn
        class="bg-btn display-1 button-custom-class white--text"
        height="50px"
        width="220px"
        :color="color"
        :to="address"
        style="font-size: 20px !important; font-weight: bold;"
    >
        {{ title }}
    </v-btn>
  </v-col>
</template>

<script>
export default {
  props: ['color', 'title', 'address'],
  name: "bgButton"
}
</script>

<style scoped>

</style>
