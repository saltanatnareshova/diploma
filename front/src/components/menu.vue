<template>
    <div>
        <Header />
        <div class="container menu">
            <h1>Меню</h1>
            <div class="row">
                <div class="col-xl-3 col-lg-3 col-md-6 col-sm-12 col-12">
                    <div class="items border border-warning">
                        <h4>Croissants</h4>
                        <p>(orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the) </p>
                        <div class="row">
                            <div class="col-6">
                                <h4>Price: 700 $</h4>
                            </div>
                            <div class="col-6">
                                <button type="button" class="btn btn-success">Заказать</button>
                            </div>
                        </div>                      
                    </div>
                </div>
                <div class="col-xl-3 col-lg-3 col-md-6 col-sm-12 col-12">
                    <div class="items border border-warning">
                        <h4>Croissants</h4>
                        <p>(orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the) </p>
                        <div class="row">
                            <div class="col-6">
                                <h4>Price: 700 $</h4>
                            </div>
                            <div class="col-6">
                                <button type="button" class="btn btn-success">Заказать</button>
                            </div>
                        </div>                      
                    </div>
                </div>
                <div class="col-xl-3 col-lg-3 col-md-6 col-sm-12 col-12">
                    <div class="items border border-warning">
                        <h4>Croissants</h4>
                        <p>(orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the) </p>
                        <div class="row">
                            <div class="col-6">
                                <h4>Price: 700 $</h4>
                            </div>
                            <div class="col-6">
                                <button type="button" class="btn btn-success">Заказать</button>
                            </div>
                        </div>                      
                    </div>
                </div>
                <div class="col-xl-3 col-lg-3 col-md-6 col-sm-12 col-12">
                    <div class="items border border-warning">
                        <h4>Croissants</h4>
                        <p>(orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the) </p>
                        <div class="row">
                            <div class="col-6">
                                <h4>Price: 700 $</h4>
                            </div>
                            <div class="col-6">
                                <button type="button" class="btn btn-success">Заказать</button>
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
.menu{
    margin-top: 200px;
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
}
.menu h4{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 22px;
    text-align: center;
    color: #7D9A2C;
}

.menu p{
    font-family: Open Sans;
    font-style: normal;
    font-weight: normal;
    font-size: 10px;
    line-height: 14px;
    color: #7D9A2C;
}
.menu button{
    background: #7D9A2C;
    border-radius: 10px;
    margin-bottom: 10px;
    height: 25px;
    padding: 0px 5px 0px 5px;
}
</style>