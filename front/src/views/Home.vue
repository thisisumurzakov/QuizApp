<template>
  <div class="d-flex align-center" style="height: 100%; width: 100%;">
    <v-container class="justify-center d-flex">
      <v-btn
          class="bg-btn mr-3 title rounded-circle custom-class"
          height="300px"
          width="300px"
          color="success"
          to="/join"
      >
        <span class="button-text">Join quiz</span>
        <span class="button-icon"><v-icon

            color="white"
        >
      mdi-play
    </v-icon></span>
      </v-btn>
      <v-btn
          class="bg-btn ml-3 title rounded-circle custom-class"
          height="300px"
          width="300px"
          color="warning"
      >
        <span class="button-text">Create quiz</span>
        <span class="button-icon"> <v-icon

            color="white"
        >
      mdi-plus
    </v-icon></span>
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

.custom-class{
  transition: 0.5s;

}
.custom-class:hover{
  transform: rotate(360deg);
}

.custom-class:hover .button-icon{
  display: block;
}

.custom-class:hover .button-text{
  display: none;
}

.custom-class .button-icon{
  display: none;
}

.custom-class .button-icon i {
  color: #fff;
  font-size: 150px;
}


.custom-class span{
  font-size: 20px !important;
  transition: 0.5s;
}

.custom-class span{
  font-size: 30px !important;
}
</style>
