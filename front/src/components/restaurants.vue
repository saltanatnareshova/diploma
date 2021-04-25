<template>
    <div>
        <Header />
        <div class="container restaurants">
            <h1>Рестораны</h1>
            <div class="list border" v-for="(restaurant, index) in posts" :key="index">
                <b-row>
                    <b-col lg="2" md="2" sm="12">
                        <img :src="restaurant.image_url">
                    </b-col>
                    <b-col lg="8" md="8" sm="12" style="padding-left: 40px;">
                        <router-link :to="{path: `/restaurants/${restaurant.id}`}"><h4>{{ restaurant.name }}</h4></router-link>
                        <h6>Наш адрес: {{ restaurant.address }}</h6>
                        <p>Наши контакты:{{ restaurant.contact }}</p>
                        <p>Средний чек: {{ restaurant.avg_cost }}</p>
                        <p>{{ restaurant.info }}</p>
                    </b-col>
                    <b-col lg="2" md="2" sm="12">
                       <router-link :to="{path: `/restaurants/${restaurant.id}/meals/`}"><button type="button" class="btn btn-warning"><p>Перейти в меню</p></button></router-link>          
                    </b-col>
                </b-row>
                
            </div>
        </div>
        <Footer />
    </div>
</template>
<script>
import axios from 'axios'
import Header from './header'
import Footer from './footer'
export default {
    components:{
        Header,
        Footer
    },
    data(){
        return{
            posts: {}
        }
    },
    mounted(){
        var self= this;
        axios.get(`http://127.0.0.1:8000/api/restaurants/`)
        .then(response => (self.posts = response.data))
        .catch(function(eroor){
            console.log(error)
        })
    },
}
</script>
<style scoped>
.restaurants{
    margin-top: 300px;
    margin-bottom: 100px;
}
.restaurants h1{
    font-family: Circular Std;
    font-style: normal;
    font-weight: normal;
    font-size: 64px;
    line-height: 77px;
    text-align: center;
    color: #7D9A2C;
}
.restaurants .list{
    margin: 20px 0px 20px 0px;
    padding: 20px 20px 20px 20px;
    border-radius: 5px;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    }
.restaurants .list img{
    width: 180px;
    height: 171px;
    border-radius: 5px;
}
.restaurants .list h4{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 36px;
    line-height: 43px;
    color: #7D9A2C;
}
.restaurants .list h6{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 13px;
    line-height: 16px;
    color: #000000;
}
.restaurants .list p{
    font-family: Open Sans;
    font-style: normal;
    font-weight: normal;
    font-size: 13px;
    line-height: 18px;
    color: rgba(85, 84, 84, 0.75);
}
.restaurants .list .media-body{
    margin-left: 49px;
}
.restaurants .list button{
    margin-top: 30px;
    background: #F39E03;
    mix-blend-mode: normal;
    border: 2px solid #F39E03;
    border-radius: 25px;
}
.restaurants .list button p{
    padding-top: 10px;
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 17px !important;
    line-height: 13px;
    text-align: center;
    color: #D4DDCA;
}
</style>