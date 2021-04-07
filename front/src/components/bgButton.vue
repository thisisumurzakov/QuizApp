<template>
    <v-btn
        :class="{
          'bg-btn display-1 button-custom-class':true,
          'black--text': textColor,
          'white--text': !textColor
        }"
        height="50px"
        width="220px"
        :color="color"
        :to="address"
        style="font-size: 20px !important; font-weight: bold;"
        v-ripple="{class: 'white--text'}"
    >
        {{ title }}
    </v-btn>
</template>

<script>
export default {
  props: ['color', 'title', 'address', 'textColor'],
  name: "bgButton"
}
</script>

<style scoped>
.button-custom-class.theme--light.v-btn--active:hover::before, .button-custom-class.theme--light.v-btn--active::before {
  opacity: 0; /* button background color glitch solution */
}
</style>
