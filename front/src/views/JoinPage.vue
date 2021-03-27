<template>
  <div style="height: 100%">
    <v-container>
      <v-card
          elevation="2"
          outlined
          shaped
          dark
          class="pa-6 d-flex justify-center align-center flex-column"
      >
        <v-card-title>
          Join to quiz
        </v-card-title>
        <v-card-actions>
          <v-text-field
            outlined
            color="success"
            label="Room ID"
            class="mr-2"
          />
          <v-text-field
            outlined
            color="warning"
            label="Your name"
          />
        </v-card-actions>
        <v-card-actions class="d-flex justify-end" style="width: 100%">
          <v-btn>Join</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "JoinPage"
}
</script>

<style scoped>

</style>
