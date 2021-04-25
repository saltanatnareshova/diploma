<template>
<div>
    <Header />
    <div class="main">
        <div class="slider">    
            <div class="row">
                <b-col xl="6" lg="6" md="6" sm="12">
                    <carousel :per-page="1" :paginationEnabled="false" :autoplay="true">
                        <slide>
                            <img class="img" src="../images/slider1.jpg">
                       </slide>
                       <slide>
                            <img class="img" src="../images/slider1.jpg">
                       </slide>
                       <slide>
                            <img class="img" src="../images/slider1.jpg">
                       </slide>
                        <slide>
                            <img class="img" src="../images/slider1.jpg">
                       </slide>
                        <slide>
                            <img class="img" src="../images/slider1.jpg">
                       </slide>
                        <slide>
                            <img class="img" src="../images/slider1.jpg">
                       </slide>
                        <slide>
                            <img class="img" src="../images/slider1.jpg">
                       </slide>
                    </carousel>
                </b-col>
                <b-col xl="6" lg="6" md="6" sm="12">
                    <div class="title">
                        <h2>Мы готовы сэкономить твое время, используй его с умом!</h2>
                        <br>
                        <p class="welcome">Добро пожаловать в PeaceOfCake!</p>
                        <div><button class="btn btn-warning">Забрать с собой</button></div>
                    </div>
                </b-col>
            </div>
        </div>
        <div class="about container">
            <b-row>
                <b-col lg="6" md="12" sm="12" class="row-images">
                    <img class="row-img" src="../images/about_1.jpeg">
                    <img class="row-img2" src="../images/about_2.jpeg">
                    <img class="row-img3" src="../images/about_3.jpeg">
                </b-col>
                <b-col lg="6" md="12" sm="12">
                    <h1 style="padding-top: 100px;">О нас</h1>
                <p>У вас когда-нибудь былоб что Вам приходилось стоят в очереди чтобы забрать свой заказ или чтобы сесть за оссвободившейся стол в заведениях общественного питания?</p>
                <p>Вам больше не нужно тратить время на ожидание блюд и счета — заказ будет на столе или упакован с собой точно ко времени визита.</p>
                <p>A Pieace of Cake - уникальный веб-сайт для предзаказа еды в заведениях.</p>
                </b-col>
            </b-row>
            <div class="container justify-content-center">                
                <div class="information" style="background: #FAE5B0;">
                    <h1>Как это сделать?</h1>
                    <b-container>
                        <b-row class="text-center">
                            <b-col xl="6" lg="5" md="12" sm="12">
                                <img class="img" src="../images/slider1.jpg">
                            </b-col> 
                            <b-col xl="6" lg="5" md="12" sm="12">
                                <img class="stepImg" src="../images/fastfood.png">
                                <img class="stepImg" src="../images/sign.png">
                                <img class="stepImg" src="../images/flag.png">
                                <img class="stepImg" src="../images/sign.png">
                                <img class="stepImg" src="../images/smile.png">
                                <b-row>
                                    <b-col xl="4" lg="4" md="4" sm="4" xs="4" class="steps">
                                        1.Выберите ресторан и сделайте предзаказ блюд к удобному времени
                                    </b-col>
                                    <b-col xl="4" lg="4" md="4" sm="4" xs="4" class="steps">
                                        2.Оплатите после подтверждения
                                    </b-col>
                                    <b-col xl="4" lg="4" md="4" sm="4" xs="4" class="steps">
                                        4.Ко времени вашего визита блюда будут на столе или упакованы навынос
                                    </b-col>
                                </b-row>
                            </b-col> 
                        </b-row>
                    </b-container>
                </div>
            </div>
        </div>
        <div class="container best_places">
            <h1>Лучшие заведения</h1>
            <div class="row">
                <div class="col-xl-3 col-lg-3 col-md-6 col-sm-12 text-center border border-warning">
                    <img class="images" src="../images/paul.jpg">
                    <hr>
                    <h2>Paul</h2>
                    <p>Tole Bi, 50</p>
                </div>
                <div class="col-xl-3 col-lg-3 col-md-6 col-sm-12 text-center border border-warning">
                    <img class="images" src="../images/about_1.jpeg">
                    <hr>
                    <h2>Coffee Boom</h2>
                    <p>Tole Bi, 150</p>
                </div>
                <div class="col-xl-3 col-lg-3 col-md-6 col-sm-12 text-center border border-warning">
                    <img class="images" src="../images/about_2.jpeg">
                    <hr>
                    <h2>Navat</h2>
                    <p>Rozybakiyeva, 50</p>
                </div>
                <div class="col-xl-3 col-lg-3 col-md-6 col-sm-12 text-center border border-warning">
                    <img class="images" src="../images/about_3.jpeg">
                    <hr>
                    <h2>KFC</h2>
                    <p>Tole Bi, 22</p>
                </div>
            </div>
        </div>
    </div>
    <Footer/>
</div>
</template>
<script>
import { Carousel, Slide } from 'vue-carousel'
import Header from './header';
import Footer from './footer';
export default {
    name: 'Main',
    components: {
        Header,
        Footer,
        Carousel,
        Slide
    },
    data(){
        return{
            
        }
    },
    mounted(){
    }
}
</script>
<style scoped>
.slider{
    position: absolute;
    width: 100%;
    min-height: 765px;
    left: 0px;
    background: #7D9A2C;
}
.slider .img{
    background-repeat: no-repeat;
    width: 100%;
    height: 765px;
}
@media screen and (max-width: 768px){
    .slider .img{
        display: none !important;
    }
}
.slider .welcome{
    font-weight: 500;
}
.slider .title{
    font-family: Pacifico;
    font-size: 25px;
    line-height: 41px;
    color: #D4DDCA;
    margin: 350px 0px 0px 45px;
}
.slider h2{
    font-family: Alegreya;
    font-weight: 1000;
    font-size: 55px;
    line-height: 41px;
    color: #D4DDCA;
}
.slider .btn{
    border: 2px solid #F39E03;
    border-radius: 50px;
    margin-top: 63px;
    margin-right: 136px;
    font-family: Circlular Std;
    color: white;
    width: 180px;
    height: 50px;
}
.about{
    padding-top: 765px;
}
.about .row-img, .about .row-img2, .about .row-img3{
    width: 200px;
    position: absolute;
}
.about .row-img{
    top: 110px;
}
.about .row-img2{
    top: 260px;
    left: 100px;
}
.about .row-img3{
    width: 230px;
    top: 170px;
    left: 300px;
}
@media screen and (max-width: 1190px) {
    .about .row-images{
        display: none !important;
    }
}
.about h1{
    font-family: Supermercado;
    font-size: 48px;
    line-height: 57px;
    color: #7D9A2C;
    text-align: center;
}
.about p{
    font-family: Circular Std;
    font-size: 24px;
    line-height: 29px;
    color: black;
}
.about .img{
    background-repeat: no-repeat;
    width: 100%;
    height: 333px;
    padding: 20px 26px 96px 26px;
}
.about .information{
    margin-top: 200px;
}
.about .stepImg{
    width: 70px;
}
.about .steps{
    margin-top: 20px;
    font-family: Supermercado;
    font-size: 20px;
    line-height: 24px;
    color: #7D9A2C;
}
.best_places{
    margin-top: 100px;
    margin-bottom: 100px;
}
.best_places h1{
    font-family: Supermercado;
    font-size: 48px;
    line-height: 57px;
    color: #7D9A2C;
    text-align: center;
}
.best_places .images{
    width: 226.14px;
    height: 330px;
    text-align: center;
    padding: 20px 0px 20px 0px;
}
.best_places h2{
    font-family: Supermercado;
    font-size: 36px;
    line-height: 43px;
    text-align: center;
    color: #7D9A2C;
}
.best_places p{
    font-family: Supermercado;
    font-size: 13px;
    line-height: 16px;
    text-align: center;
    color: #596C23;
}
.best_places .row{
    margin-top: 80px;
}
.best_places hr{
    background: #ffc107;
}
.contacts{
    margin-top: 100px;
    margin-bottom: 100px;
}
.contacts h1{
    font-family: Supermercado;
    font-size: 48px;
    line-height: 57px;
    color: #7D9A2C;
    text-align: center;
}
.contacts p{
    font-family: Supermercado;
    font-size: 20px;
    line-height: 36px;
    color: #7D9A2C;
}
</style>