<template>
    <div>
        <Header />
        <div class="orders">
            <div class="container">
            <h1>My Orders</h1>
            <div class="order">
                <div class="items border border-warning">
                    <h4>Order name</h4>
                    <p>(orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the) </p>
                    <div class="row">
                            <div class="col-6">
                                <h4>Price: 100$</h4>
                            </div>
                            <div class="col-6">
                                <button type="button" class="btn btn-success">Accept</button>
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
           
            formData:{
                username: 'saltok',
                password: '12'
            }
        }       
    },
    methods:{
        
    },
    mounted(){
        
    },
    created(){
        const headers = {  "Authorization": "token 9ccc7b63e73bb0881fb00b63727598eaee78cab" };
        axios.get(`http://127.0.0.1:8000/api/orders/`, 
        {
            headers
        }
        )
        .then(res => console.log(res))
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
    padding: 10px 5px 5px 10px;
    margin: 10px 0px 10px 0px;
}
.orders h4{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 30px;
    line-height: 22px;
    color: black;
}
.orders p{
    font-family: Open Sans;
    font-style: normal;
    font-weight: normal;
    font-size: 20px;
    line-height: 20px;
    color: #7D9A2C;
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