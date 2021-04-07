<template>
  <v-container>
    <v-card dark class="elevation-10 d-flex flex-column">
      <v-card-title class="d-flex justify-space-between">
        <span class="display-3">{{ title }}</span>
        <span class="display-1">{{ joinBtn.name.toUpperCase() }}</span>
      </v-card-title>
      <v-card-subtitle class="display-1">
        {{ description }}
      </v-card-subtitle>
      <v-card class="pa-3 ma-2">
        <v-simple-table>
          <template v-slot:default>
            <thead>
            <tr>
              <th class="text-left">
                Name
              </th>
              <th class="text-left">
                {{ url }}
              </th>
            </tr>
            </thead>
            <tbody>
            <tr
                v-for="item in top"
                :key="item.name"
            >
              <td>{{ item.name }}</td>
              <td>{{ item.points }}</td>
            </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-card>
      <v-card-actions class="d-flex justify-end">
        <v-btn v-if="joinBtn.visible" :to="`/quiz/${url}/start`">Join</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "QuizMainPage",
  data: () => ({
    title: 'Quiz title',
    description: 'Quiz description',
    top: [
      {
        name: 'AAA',
        points: 12
      },
      {
        name: 'BBB',
        points: 11
      }
    ]
  }),
  computed: {
    joinBtn() {
      let name = this.$store.getters.getName
      return {name, visible: !!name}
    },
    url() {
      return this.$route.path.split('/')[2]
    }
  }
}
</script>

<style scoped>

</style>
