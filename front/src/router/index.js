import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '../components/main.vue';
import AboutUs from '../components/aboutus.vue';
import Restaurants from '../components/restaurants.vue';
import Cafe from '../components/cafe.vue';
import Canteens from '../components/canteens.vue';
import Menu from '../components/menu.vue';
import Login from '../components/login.vue';
import Signup from '../components/signup.vue';
import Request from '../components/forrestaurants.vue';
import Orders from '../components/orders.vue';
import store from '../store/index.js';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'main',
    component: Main
  },
  {
    path: '/about_us',
    name: 'aboutUs',
    component: AboutUs
  },
  {
    path: '/restaurants',
    name: 'restaurants',
    component: Restaurants,
  },
  {
    path: '/restaurants/:id/meals/',
    name: 'menu',
    component: Menu,
  },
  {
    path: '/cafees',
    name: 'cafees',
    component: Cafe
  },
  {
    path: '/canteens',
    name: 'canteens',
    component: Canteens
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    beforeEnter: (to, from, next) => {
      if(store.state.token){
        next('/')
      }else{
        next()
      }
    }
  },
  {
    path: '/signup',
    name: 'signup',
    component: Signup
  },
  {
    path: '/request',
    name: 'reguest',
    component: Request
  },
  {
    path: '/orders',
    name: 'orders',
    component: Orders,
    beforeEnter: (to, from, next) => {
      if(store.state.token){
        next()
      }else{
        next('/')
      }
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
