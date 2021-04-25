<template>
    <div>
        <Header />
        <div class="container menu">
            <h1>Меню</h1>
            <div class="row">
                <div class="col-xl-3 col-lg-3 col-md-6 col-sm-12 col-12" v-for="(post, index) in posts" :key="index">
                    <div class="items border">
                        <h2>{{ post.name }}</h2>
                        <h5>Ingridients: <span class="info">{{ post.structure }}</span></h5>
                        <h5>Time of preparation: <span class="info">{{ post.time }}</span></h5>
                        <div class="row">
                            <div class="col-6">
                                <h4>Price: <span class="info">{{ post.price }}</span></h4>
                            </div>
                            <div class="col-6">
                                <button type="button" class="btn btn-success" @click.prevent="submit(post.name, post.structure, post.time)">Заказать</button>
                            </div>
                        </div>                      
                    </div>
                </div>
            </div>
        </div>
        <Footer />
    </div>
</template>
<script>
import axios from 'axios';
import Header from './header'
import Footer from './footer'
export default {
    data(){
        return{
            posts: {},
            meals: this.$route.params.id,
            order: {
                meal_name: "",
                structure: "",
                time: "",
                count: "1",      
            }
        }
    },
    components:{
        Header,
        Footer
    },
    mounted(){
        var self = this;
        axios.get(`http://127.0.0.1:8000/api/cafes/${self.meals}/meals/`)
        .then(response => (self.posts = response.data
        ))
        .catch(function(error){
            console.log(error);
        })
    },
    methods:{
        submit($event, $event2, $event3){
            var self = this;
            this.order.meal_name = $event;
            this.order.structure = $event2;
            this.order.time = $event3;
                const headers = {  "Authorization": "token " + localStorage.getItem("token") };
                axios.post('http://127.0.0.1:8000/api/orders/', self.order, { headers })
                .then(res => console.log(res))
                .catch(error => console.log(error))
        }
        
    }
}
</script>
<style scoped>
.menu{
    margin-top: 300px;
    margin-bottom: 100px;
}
.menu h1{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 64px;
    line-height: 77px;
    text-align: center;
    color: #7D9A2C;
}
.menu .items{
    padding: 10px 5px 5px 10px;
    margin: 10px 0px 10px 0px;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
.menu h2{
    font-family: Circular Std;
    font-style: normal;
    font-weight: normal;
    font-size: 25px;
    line-height: 23px;
    color: #000000;
}
.menu h5, .menu h4, .menu h6{
    font-family: Circulat Std;
    font-style: normal;
    font-weight: 600;
    font-size: 15px;
    line-height: 23px;
    color: #000000;
}
.menu .info{
    font-weight: 500;
}
.menu p{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    font-style: normal;
    font-weight: normal;
    font-size: 15px;
    line-height: 14px;
    color: #4d4e49;;
}
.menu button{
    background: #7D9A2C;
    border-radius: 10px;
    margin-bottom: 10px;
    height: 25px;
    padding: 0px 5px 0px 5px;
}
</style>