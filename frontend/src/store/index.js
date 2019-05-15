import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const enhanceAccessToken = () => {
  const {accessToken} = localStorage
  if (!accessToken) return
  axios.defaults.headers.common['Authorization'] = `Bearer ${accessToken}`
}
enhanceAccessToken()
export default new Vuex.Store({
  state: {
    accessToken: null
  },
  getters: {

  },
  mutations: {
    LOGIN (state, {accessToken}) {
      state.accessToken = accessToken
      localStorage.accessToken = accessToken
    },
    LOGOUT (state) {
      state.accessToken = null
      delete localStorage.accessToken
    }
  },
  actions: {
    LOGIN ({commit}, {username, password}) {
      return axios.post(`/api/login`, {username: username, password: password})
        .then((res) => {
          let data = res.data
          if (res.status == '200') {
            alert("로그인 되었습니다.")
            commit('LOGIN', data)
            axios.defaults.headers.common['Authorization'] = `Bearer ${data.accessToken}`
          } else if (res.status == '203') {
            alert("올바르지 않은 비밀번호 입니다.")
          } else if (res.status == "204") {
            alert("올바르지 않은 아이디 입니다.")
          }
        })
    },
    LOGOUT ({commit}) {
      axios.defaults.headers.common['Authorization'] = undefined
      commit('LOGOUT')
    },
    CHECK () {
      if (localStorage.accessToken != null) {
        return true
      } else {
        return false
      }
    }
  }
})
