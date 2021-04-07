<template>
    <div
        class="d-flex align-center"
        style="height: 100%; width: 100%;"
    >
      <particles style="width: 100vw; height: 100vh; position:absolute; background: #fff;" />
      <v-container>
        <v-row align="center" justify="center" class="flex-column">
          <img src="../assets/quiz.png" alt="">
          <bg-button
              title="Join quiz"
              color="black"
              address="/join"
              :text-color="false"
          />
          <bg-button
              :text-color="true"
              title="Create quiz"
              color="#ffd20d"
              address="/"
          />
        </v-row>
      </v-container>
  </div>
</template>

<script>
import particles from '@/components/particles';
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
    bgButton,
    particles
  },
  name: 'Home'
}
</script>

<style scoped>
</style>
