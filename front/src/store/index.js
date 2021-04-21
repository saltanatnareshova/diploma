import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    username: "",
    token: localStorage.getItem("token")
  },
  getters:{
    isAuth(state){
      if(state.token){
        return true
      }else{
        return false
      }
    }
  },
  mutations: {
    auth(state, authData){
      state.username = authData.name;
      state.token = authData.token;
    },
    logout(state){
      state.username = null;
      state.token = null;
      localStorage.removeItem("username");
      localStorage.removeItem("token");
    }
  },
  actions: {
    
    signup({ commit }, payload){
      axios.post('http://127.0.0.1:8000/api/register/', {
        ...payload,
      })
      .then(response => {
        console.log(response);
        commit("auth", response.data);
      })
      .catch(err => console.log(err));
    },
    signin({ commit }, payload){
      axios.post('http://127.0.0.1:8000/api/login/', {
        ...payload,
      })
      .then(authData => {
         commit("auth", authData.data);
         localStorage.setItem("username", authData.data.name);
         localStorage.setItem("token", authData.data.token);
         console.log(authData.data.token);
       })
      .catch(error = console.log(error));
    }
  },
  modules: {
  }
})
