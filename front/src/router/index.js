import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '../components/main.vue';
import AboutUs from '../components/aboutus.vue';
import Restaurants from '../components/restaurants.vue';
import restaurantInfo from '../components/aboutRestaurant.vue';
import cafeInfo from '../components/aboutCafe.vue';
import fastfoodInfo from '../components/aboutFastFood.vue';
import Cafe from '../components/cafe.vue';
import Canteens from '../components/canteens.vue';
import MenuRestaurants from '../components/menuRestaurants.vue';
import MenuCafes from '../components/menuCafes.vue';
import MenuFastFoods from '../components/menuFastFoods.vue';
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
    path: '/restaurants/:id',
    name: 'restaurantInfo',
    component: restaurantInfo,
  },
  {
    path: '/cafes/:id',
    name: 'cafeInfo',
    component: cafeInfo,
  },
  {
    path: '/fastfoods/:id',
    name: 'fastfoodInfo',
    component: fastfoodInfo,
  },
  {
    path: '/restaurants/:id/meals/',
    name: 'menuRestaurants',
    component: MenuRestaurants,
  },
  {
    path: '/cafes/:id/meals/',
    name: 'menuCafes',
    component: MenuCafes,
  },
  {
    path: '/fastfoods/:id/meals/',
    name: 'menuFastFoods',
    component: MenuFastFoods,
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
