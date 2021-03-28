<template>
    <div>
        <Header />
        <div class="container restaurants">
            <h1>Cafe</h1>
            <div class="list border border-warning">
                <div class="media">
                    <img src="../images/slider2.webp">
                    <div class="media-body">
                        <div class="row">
                            <div class="col-xl-8 col-lg-8 col-md-8 col-sm-12 col--12">
                                <router-link to="/restaurants/:id"><h4>Paul</h4></router-link>
                                <h6>Адрес: Толе Би, 59</h6>
                                <p>О ресторане: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the indsed in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
                            </div>
                            <div class="col-xl-4 col-lg-4 col-md-4 col-sm-12 col--12 text-center">
                                <router-link to="/restaurants/:id"><button type="button" class="btn btn-warning"><p>Перейти в меню</p></button></router-link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="list border border-warning">
                <div class="media">
                    <img src="../images/slider2.webp">
                    <div class="media-body">
                        <div class="row">
                            <div class="col-xl-8 col-lg-8 col-md-8 col-sm-12 col--12">
                                <router-link to="/restaurants/:id"><h4>Paul</h4></router-link>
                                <h6>Адрес: Толе Би, 59</h6>
                                <p>О ресторане: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the indsed in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
                            </div>
                            <div class="col-xl-4 col-lg-4 col-md-4 col-sm-12 col--12 text-center">
                                <button type="button" class="btn btn-warning"><p>Перейти в меню</p></button>
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
.restaurants{
    margin-top: 200px;
    margin-bottom: 100px;
}
.restaurants h1{
    font-family: Supermercado;
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
    color: rgba(0, 0, 0, 0.75);
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