<template>
  <div style="height: 100%; position: relative;">
    <v-carousel
        :show-arrows="false"
        cycle
        interval="3000"
        hide-delimiters
        style="height: 100%;"
    >
      <v-carousel-item
          v-for="color in colors"
          :key="color"
          :style="{
            height: '100%',
            background: color + ' no-repeat fixed center',
            backgroundSize:'cover'}"
      >

      </v-carousel-item>
    </v-carousel>
    <div
        class="d-flex align-center"
        style="height: 100%; width: 100%; position: absolute;top: 0"
    >
      <v-container>
        <v-row align-content="center">
          <bg-button
              title="Create quiz"
              color="warning"
              inner-icon="mdi-plus"
              address="/blet"
          />
          <bg-button
              title="Join to quiz"
              color="success"
              inner-icon="mdi-play"
              address="/join"
          />
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
import bgButton from '@/components/bgButton';

export default {
  data: () => ({
    model: 0,
    colors: [
      'url("https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg")',
      'url("https://cdn.vuetifyjs.com/images/carousel/sky.jpg")',
      'url("https://cdn.vuetifyjs.com/images/carousel/bird.jpg")',
      'url("https://cdn.vuetifyjs.com/images/carousel/planet.jpg")'
    ],
  }),
  components: {
    bgButton
  },
  name: 'Home'
}
</script>

<style scoped>

</style>
