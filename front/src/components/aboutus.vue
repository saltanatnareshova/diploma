<template>
    <div>
        <Header />
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
        <Footer />
    </div>
</template>
<script>
import Header from './header'
import Footer from './footer'
export default {
    components:{
        Header,
        Footer
    }
}
</script>
<style scoped>
.about{
    padding-top: 100px;
    padding-bottom: 100px;
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
    margin-top: 100px;
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
</style>