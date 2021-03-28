<template>
    <div>
        <Header />
        <div class="container request">
            <div class="row">
                <div class="col-xl-8 col-lg-8 col-md-12 col-sm-12">
                    <h1>Оставить заявку на </h1>
                    <h2>ПОДКЛЮЧЕНИЕ</h2>
                     <form>
                        <div class="row" style="margin-bottom: 30px;">
                            <div class="col-xl-6 col-lg-6 col-md-12 col-sm-12">
                                <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Your name">
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-12 col-sm-12 column2">
                                <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Your e-mail">
                            </div>
                        </div>
                        <div class="row" style="margin-bottom: 30px;">
                            <div class="col-xl-6 col-lg-6 col-md-12 col-sm-12">
                                <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Restaurant">
                            </div>
                            <div class="col-xl-6 col-lg-6 col-md-12 col-sm-12 column2">
                                <input type="number" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Your phone">
                            </div>
                        </div>
                        <div class="form-group">
                            <input type="text" class="form-control" id="exampleInputPassword1" placeholder="Your city">
                            <textarea placeholder="Comment"></textarea>
                        </div>
                       <div class="form-check" style="margin-top: 30px;">
                            <input type="checkbox" class="form-check-input" id="exampleCheck1">
                            <label class="form-check-label" for="exampleCheck1">Я ознакомлен(а) с Политикой конфиденциальности и даю согласие на обработку моих персональных данных. Я принимаю условия  
        Пользовательского соглашения
                            </label>
                        </div>
                        <button type="submit" class="btn btn-warning"><p>Регистрация</p></button>
                    </form>
                </div>
                <div class="col-xl-4 col-lg-4 col-md-12 col-sm-12" style="background: #C4C4C4;">
                    
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
.request{
    margin-top: 250px;
    margin-bottom: 100px;
}
.request h1{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 30px;
    line-height: 36px;
    color: #F39E03;
}
.request h2{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 36px;
    line-height: 43px;
    color: rgba(0, 0, 0, 0.25);
}
.request .form-check-label{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 22px;
    color: #D4DDCA;
}
.request button p{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 20px;
    line-height: 20px;
    text-align: center;
    color: #D4DDCA;
}
.request button{
    margin-top: 30px;
    padding: 10px 5px 0px 5px;
}
.request textarea{
    margin-top: 30px;
    width: 100%;
}
@media screen and (max-width: 992px) {
    .form-control{
        margin-top: 20px;
    }
}
</style>