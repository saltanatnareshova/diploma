<template>
    <div>
        <Header />
        <div class="orders">
            <div class="container">
            <h1>Мои заказы</h1>
            <div class="order" v-for="(order, index) in formData" :key="index">
                <div class="items border">
                    <h2>{{ order.meal_name }}</h2>
                    <p>Ingridients: <span class="info">{{ order.structure }}</span> </p>
                    <p>Time of preparation: <span class="info">{{ order.time }}</span> </p>                    
                    <div class="row">
                            <div class="col-6">
                                <h4>Number: <span class="info">{{ order.count }}</span></h4>
                            </div>
                            <div class="col-6">
                                <button type="button" class="btn btn-success">Потвердить</button>
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
import Header from '../components/header.vue';
import Footer from '../components/footer.vue';

export default {
    components:{
        Header,
        Footer
    },
    data(){
        return{
            formData:{}
        }       
    },
    methods:{
        
    },
    mounted(){
        
    },
    created(){
        var self = this;
        const headers = {  "Authorization": "token " + localStorage.getItem("token") };
        axios.get(`http://127.0.0.1:8000/api/orders/`, 
        {
            headers
        }
        )
        .then(res => self.formData = res.data )
        .catch(error => console.log(error));
    }
}
</script>
<style scoped>
.orders{
    margin-top: 300px;
    margin-bottom: 100px;
}
.orders h1{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 64px;
    line-height: 77px;
    text-align: center;
    color: #7D9A2C;
}
.orders .items{
    width: 800px;
    padding: 10px 5px 5px 10px;
    margin: 10px 0px 10px 0px;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
.order h2{
    font-family: Circular Std;
    font-style: normal;
    font-weight: normal;
    font-size: 25px;
    line-height: 23px;
    color: #7D9A2C;
}
.order p, .orders h4{
    font-family: Circulat Std;
    font-style: normal;
    font-weight: 600;
    font-size: 20px;
    line-height: 23px;
    color: #7D9A2C;
}
.order .info{
    font-weight: 500;
}
.orders button{
    background: #7D9A2C;
    border-radius: 10px;
    margin-bottom: 10px;
    height: 25px;
    padding: 0px 5px 0px 5px;
}
.orders .items{
    left: 15px;
    right: 15px;
}
</style>