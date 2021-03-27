<template>
  <div class="main-section">
    <v-container>
      <v-btn class="ma-3" color="success" to="/join">Join quiz</v-btn>
      <v-btn color="warning">Create quiz</v-btn>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style>
.v-main__wrap{
    display: flex;
    align-items: center;
    justify-content: center;
  }
.main-section .container .v-btn{
  width: 300px;
  height: 300px !important;
  border-radius: 50%;
}
.main-section .container .v-btn span{
  font-size: 20px;
}
.main-section .container .v-btn:first-child{
  margin-right: 50px !important;
}
</style>
