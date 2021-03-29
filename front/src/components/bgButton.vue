<template>
  <v-col
      md="6"
      sm="12"
      class="justify-center d-flex"
  >
    <v-btn
        class="bg-btn display-1 rounded-circle btn-transition"
        height="300px"
        width="300px"
        :color="color"
        :to="address"
    >
      <span class="button-icon">
        <v-icon
            x-large
            color="white"
        >
          {{ innerIcon }}
        </v-icon>
      </span>
      <span class="button-text">
        {{ title }}
      </span>
    </v-btn>
  </v-col>
</template>

<script>
export default {
  props: ['color', 'title', 'innerIcon', 'address'],
  name: "bgButton"
}
</script>

<style scoped>
.btn-transition {
}
.button-text {
  opacity: 0;
}
.button-icon {
  margin-bottom: 10px;
}
.btn-transition:hover .button-text {
  opacity: 1;
}
.btn-transition:hover .button-icon {
  opacity: 0;
}
.button-icon, .button-text {
  position: absolute;
  transition: .3s all;
  transform-origin: center;
}
</style>
