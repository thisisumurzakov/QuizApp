<template>
    <div
        class="d-flex align-center"
        style="height: 100%; width: 100%;"
    >
      <v-container>
        <v-row align-content="center">
          <bg-button
              title="Create quiz"
              color="warning"
              inner-icon="mdi-plus"
              address="/"
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
