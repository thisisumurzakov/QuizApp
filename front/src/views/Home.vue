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

.custom-class {
  transition: 0.5s;
}

.custom-class:hover {
  transform: rotate(360deg);
}

.custom-class:hover .button-icon {
  display: block;
}


.custom-class:hover .button-text {
  display: none;
}

.custom-class .button-icon {
  display: none;
}

.custom-class .button-icon i {
  color: #fff;
  font-size: 150px;
}


.custom-class span {
  font-size: 20px !important;
  transition: 0.5s;
}

.custom-class span {
  font-size: 30px !important;
}
</style>
