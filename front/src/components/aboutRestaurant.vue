<template>
    <div>
        <Header />
        <div class="container restaurants">
            <h1>{{ restaurant.name }}</h1>
             <b-card :title="restaurant.name" :img-src="restaurant.image_url" img-top>
                <b-card-text>
                    <p>{{ restaurant.address }}</p>
                    <p>{{ restaurant.contact }}</p>
                    <p>{{ restaurant.avg_cost }}</p>
                </b-card-text>
                <b-card-text class="small text-muted">
                    <p>{{ restaurant.info }}</p>
                </b-card-text>
            </b-card>
            <div>
                <h2>Отзывы o {{ restaurant.name }}</h2>
                <div>
                    <input type="text" v-model="texts">
                    <button type="button" @click.prevent="submit">Добавить комментарии</button> 
                </div>
                <b-row>
                    <b-col class="reviews" lg="4" md="6" sm="12" v-for="(review, index) in reviews" :key="index">
                        <div class="cardReview border border-warning">
                            <p>{{ review.user.username }}</p>
                            <p>{{ review.text }}</p>
                        </div>
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
    data(){
        return{
            texts: "",
            restaurant: {
                name: "Paul",  
            },
            reviews: {

            },
            id: this.$route.params.id,
        }
    },
    components:{
        Header,
        Footer
    },
    mounted(){
        var self = this;
        axios.get(`http://127.0.0.1:8000/api/restaurants/${self.id}/`)
        .then(response => (self.restaurant = response.data
        ))
        .catch(function(error){
            console.log(error);
        }),
        axios.get(`http://127.0.0.1:8000/api/restaurants/${self.id}/reviews/`)
        .then(response => (self.reviews = response.data
        ))
        .catch(function(error){
            console.log(error);
        })
    },
    methods:{
        submit(){
            var self = this;
            const headers = {  "Authorization": "token " + localStorage.getItem("token") };
            axios.post(`http://127.0.0.1:8000/api/restaurants/${self.id}/reviews/`, self.text, { headers })
                .then(res => console.log(res))
                .catch(error => console.log(error))
        }
    }
}
</script>

<style scoped>
.restaurants{
    margin-top: 300px;
    margin-bottom: 100px;
}
@media  screen and (max-width: 540px) {
    .restaurants{
        margin-top: 400px;
    }
}
.restaurants h1{
    font-family: Sircular Std;
    font-style: normal;
    font-weight: normal;
    font-size: 64px;
    line-height: 77px;
    text-align: center;
    color: #7D9A2C;
}
.restaurants h2{
    font-family: Sircular Std;
    font-style: normal;
    font-weight: normal;
    font-size: 45px;
    line-height: 77px;
    text-align: center;
    color: #7D9A2C;
}
.restaurants .reviews{
    margin-top: 20px;
}
.restaurants .card{
    width: 90%;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    background: rgba(209, 209, 209, 0.25);
    border-radius: 30px;
}
.restaurants .cardReview{
    width: 90%;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    background: rgba(255, 255, 255, 0.25);
    padding: 20px;
}
.restaurants .card-img-top{
    border-radius: 30px;
}
.restaurants p, .restaurants .card-title{
    font-family: Supermercado;
    font-size: 22px;
    line-height: 20px;
    color: black;
}
.restaurants .card-title{
    font-weight: bold;
    font-size: 40px;
    line-height: 30px;
}
</style>
