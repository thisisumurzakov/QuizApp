<template>
  <v-container>
    <v-card class="pa-2" dark>
      <v-stepper @change="emm" color="primary" non-linear v-model="stepper">
        <v-stepper-items>
          <v-stepper-content :step="i" v-for="i in quiz.length" :key="i">
            <v-card class="pa-10 d-flex flex-column justify-start">
              <div class="title">{{ quiz[i-1].title }}</div>
              <div v-for="answers in quiz[i-1].answers" :key="answers.id">
                <v-radio-group v-model="quiz[i-1].choosenAnswer">
                  <v-radio
                    color="primary"
                    v-for="answer in answers"
                    :label="answer"
                    :key="answer.index"
                    :value="answer.index"
                  ></v-radio>
                </v-radio-group>
              </div>
              <v-container class="d-flex justify-space-around">
                <v-btn @click="prevQuestion">Previous question</v-btn>
                <v-btn @click="nextQuestion">Next question</v-btn>
              </v-container>
            </v-card>
          </v-stepper-content>
        </v-stepper-items>
        <v-stepper-header style="height: 100%">
          <v-stepper-step color="primary" editable :step="i" v-for="i in quiz.length" :key="i">
          </v-stepper-step>
        </v-stepper-header>
      </v-stepper>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "QuizStart",
  data: () => ({
    stepper: 1,
    question: 'Nmadur',
    quiz: [
      {
        title: 'Nmadur',
        answers: [
          [
            'A',
            'B',
            'C',
            'D'
          ]
        ],
        choosenAnswer: 0
      },
      {
        title: 'Rudamn',
        answers: [
          [
            'E',
            'F',
            'G',
            'H'
          ]
        ],
        choosenAnswer: 0
      }
    ]
  }),
  methods: {
    nextQuestion() {
      this.stepper === this.quiz.length ? this.stepper = 1 : this.stepper++
    },
    prevQuestion() {
      this.stepper === 1 ? this.stepper = this.quiz.length : this.stepper--
    },
    emm() {
      console.log(this.stepper)
    }
  }
}
</script>

<style>
.v-application--is-ltr .v-stepper__step__step {
  margin-right: 4px!important;
  margin-left: 4px!important;
}
</style>
