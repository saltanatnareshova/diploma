<template>
<div>
    <Header />
    <div class="main">
        <div class="slider">    
            <b-row>
                <b-col xl="6" lg="6" md="6" sm="12">
                    <img class="img" src="../images/slider1.jpg">
                </b-col>
                <b-col xl="6" lg="6" md="6" sm="12">
                    <div class="container">
                        <p class="welcome">Welcome to PeaceOfCake!</p>
                        <h2 class="title">Закажи сейчас, используй время с умом</h2>
                        <div class="float-right"><button class="btn btn-outline-warning"><p class="btn-text">Забрать с собой</p></button></div>
                    </div>
                </b-col>
            </b-row>
        </div>
        <div class="about">
            <div class="container justify-content-center">
                <h1 style="padding-top: 100px;">О нас</h1>
                <p>У вас когда-нибудь возникала проблема......???</p>
                <p>Вам больше не нужно тратить время на ожидание блюд и счета — заказ будет на столе или упакован с собой точно ко времени визита.</p>
                <p>A Pieace of Cake - уникальный веб-сайт для предзаказа еды в заведениях.</p>
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
                    <img class="images" src="../images/paul.jpg">
                    <hr>
                    <h2>Paul</h2>
                    <p>Tole Bi, 50</p>
                </div>
                <div class="col-xl-3 col-lg-3 col-md-6 col-sm-12 text-center border border-warning">
                    <img class="images" src="../images/paul.jpg">
                    <hr>
                    <h2>Paul</h2>
                    <p>Tole Bi, 50</p>
                </div>
                <div class="col-xl-3 col-lg-3 col-md-6 col-sm-12 text-center border border-warning">
                    <img class="images" src="../images/paul.jpg">
                    <hr>
                    <h2>Paul</h2>
                    <p>Tole Bi, 50</p>
                </div>
            </div>
        </div>
        <div class="container contacts">
            <h1>Наши контакты</h1>
            <div class="row">
                <div class="col-xl-6 col-lg-6 col-md-6 col-sm-12">
                    <p>Телефон:</p>
                    <p>+7 777 77 77 777</p>
                </div>
                <div class="col-xl-6 col-lg-6 col-md-6 col-sm-12">
                    <p>E-mail:</p>
                    <p>pieaceofcake@mail.ru</p>
                </div>
            </div>
        </div>
    </div>
    <Footer/>
</div>
</template>
<script>
import Header from './header';
import Footer from './footer';
export default {
    name: 'Main',
    components: {
        Header,
        Footer
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
    font-family: Zilla Slab;
    font-style: normal;
    font-weight: 600;
    font-size: 24px;
    line-height: 29px;
    color: #E0E9E5;
    margin-top: 201px;
    margin-left: 45px;
}
.slider .title{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 34px;
    line-height: 41px;
    color: #D4DDCA;
    margin-left: 45px;
}
.slider .btn{
    mix-blend-mode: normal;
    border: 2px solid #F39E03;
    border-radius: 50px;
    margin-top: 63px;
    margin-right: 136px;
    padding-top: 12px;
}
.slider .btn-text{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 21px;
    line-height: 25px;
    color: #D4DDCA;
}
.about{
    padding-top: 765px;
}
.about h1{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 48px;
    line-height: 57px;
    color: #7D9A2C;
    text-align: center;
}
.about p{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 24px;
    line-height: 29px;
    color: #7D9A2C;
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
    font-style: normal;
    font-weight: normal;
    font-size: 20px;
    line-height: 24px;
    color: #7D9A2C;
}
.best_places{
    margin-top: 100px;
}
.best_places h1{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
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
    font-style: normal;
    font-weight: normal;
    font-size: 36px;
    line-height: 43px;
    text-align: center;
    color: #7D9A2C;
}
.best_places p{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
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
    font-style: normal;
    font-weight: normal;
    font-size: 48px;
    line-height: 57px;
    color: #7D9A2C;
    text-align: center;
}
.contacts p{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 30px;
    line-height: 36px;
    color: #7D9A2C;
}
</style>