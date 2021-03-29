<template>
  <div class="d-flex align-center" style="height: 100%; width: 100%;">
    <v-container>
      <v-row align-content="center">
        <bg-button
            title="Create quiz"
            color="warning"
            inner-icon="mdi-plus"
            address=""
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
  components: {
    bgButton
  },
  name: 'Home'
}
</script>

<style scoped>

</style>
