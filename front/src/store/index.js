import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    roomID: null,
    name: null
  },
  mutations: {
    setRoomID(state, payload) {
      state.roomID = payload
    },
    setName(state, payload) {
      state.name = payload
    }
  },
  actions: {
    async join({ commit }, payload) {
      commit('setRoomID', payload.roomID)
      commit('setName', payload.name)
      await localStorage.setItem('name', payload.name)
      await localStorage.setItem('roomID', payload.roomID)
    }
  },
  getters: {
    getRoomID(state) {
      return state.roomID
    },
    getName(state) {
      return state.name
    }
  },
  modules: {
  }
})
