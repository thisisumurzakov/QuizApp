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
            success
            :rules="rules"
            label="Room ID"
            class="mr-2"
            v-model="roomID"
          />
        </v-card-actions>
        <v-card-actions class="d-flex justify-end" style="width: 100%">
          <v-btn @click="join" :disabled="!validation">Join</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "JoinPage",
  data: () => ({
    roomID: '',
    rules: [val => (val || '').length > 10 || 'This field is required']
  }),
  methods: {
    async join() {
      await this.$store.dispatch('join', {roomID: this.roomID})
      await this.$router.push(`/quiz/${this.roomID}/home`)
    }
  },
  computed: {
    validation() {
      return this.roomID.length >= 10
    }
  }
}
</script>

<style scoped>

</style>
