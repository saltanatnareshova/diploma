import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
    
  },
  actions: {
    signup({ commit }, payload){
      axios.post('http://127.0.0.1:8000/api/register/', {
        ...payload,
      })
      .then(response => console.log("Hello"))
      .catch(err => console.log(err));
    }
    // signup({commit}, payload){
    //   axios.post(`http://127.0.0.1:8000/api/register/`, {
    //     ...payload
    //   }).then(response => response.json())
    //   .catch(function(error){
    //     console.log(error);
    //   })
    // },
    // signin({commit}, payload){
    //   var self = this;
    //   axios.post(`http://127.0.0.1:8000/api/login/`, {
    //     ...payload,
    //     returnSecureToken: true
    //   }).then(response => response.json)
    //     .then(autdata => {
    //       commit('auth', autdata);
    //       localStorage.setItem("token", autdata.idToken);
    //     })
    //       .catch(function(error){
    //       console.log(error)
    //     })
    // }
  },
  modules: {
  }
})
