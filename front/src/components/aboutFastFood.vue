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
            restaurant: {
                name: "Paul",
                
            },
            name: this.$route.params.id,
        }
    },
    components:{
        Header,
        Footer
    },
    mounted(){
        var self = this;
        axios.get(`http://127.0.0.1:8000/api/fastfoods/${self.name}/`)
        .then(response => (self.restaurant = response.data
        ))
        .catch(function(error){
            console.log(error);
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
    font-family: Sircular Std;
    font-style: normal;
    font-weight: normal;
    font-size: 64px;
    line-height: 77px;
    text-align: center;
    color: #7D9A2C;
}
.restaurants .card{
    width: 90%;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    background: rgba(209, 209, 209, 0.25);
    border-radius: 30px;
}
.restaurants .card-img-top{
    border-radius: 30px;
}
.restaurants .card p, .restaurants .card-title{
    font-family: Supermercado;
    font-size: 22px;
    line-height: 20px;
    color: #7D9A2C;
}
.restaurants .card-title{
    font-weight: bold;
    font-size: 40px;
    line-height: 30px;
}
</style>
