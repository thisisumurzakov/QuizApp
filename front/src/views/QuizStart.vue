<template>
  <v-container>
    <v-card class="pa-2" dark>
      <v-stepper @change="stepperChanging" color="primary" non-linear v-model="stepper">
        <v-stepper-header
            :class="[{'animation': !lol}, 'stepper']"
        >
          <v-stepper-step
              color="primary"
              editable
              :step="i"
              v-for="i in quiz.length"
              :key="i"
          />
        </v-stepper-header>
        <v-toolbar dense class="hidden-sm-and-up">
          <v-spacer />
          <v-app-bar-nav-icon @click="lol = !lol" />
        </v-toolbar>
        <v-stepper-items>
          <v-stepper-content :step="i" v-for="i in quiz.length" :key="i">
            <v-card class="pa-10 d-flex flex-column justify-start" v-if="quiz[i-1]">
              <div class="title">{{ quiz[i - 1].title }}</div>
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
            </v-card>
            <v-progress-circular
                :width="3"
                v-else
                color="red"
                indeterminate
            ></v-progress-circular>
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
      <v-container class="d-flex justify-space-around flex-wrap">
        <v-btn @click="prevQuestion" class="lol mb-1">Previous question</v-btn>
        <v-btn @click="nextQuestion" class="mb-1">Next question</v-btn>
      </v-container>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "QuizStart",
  data: () => ({
    lol: true,
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
      // eslint-disable-next-line
      false,
      false,
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
    stepperChanging() {
      console.log(this.stepper)
    }
  }
}
</script>

<style lang="sass">
.stepper
  height: 100% !important
  overflow: hidden
  max-height: 400px
  transition: max-height .5s
.animation
  max-height: 0

.v-application--is-ltr .v-stepper__step__step
  margin-right: 4px !important
  margin-left: 4px !important

.v-stepper__step
  padding: 12px !important

</style>
