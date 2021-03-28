<template>
    <div>
        <Header />
        <div class="container login">
            <div class="row">
                <div class="col-xl-8 col-lg-8 col-md-12 col-sm-12">
                    <h1>Уже зарегестрированы </h1>
                    <form>
                        <div class="form-group">
                            <label class="emailLabel" for="exampleInputEmail1">E-mail</label>
                            <input type="email" class="form-control email" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
                        </div>
                        <div class="form-group">
                            <label class="passwordLabel" for="exampleInputPassword1">Пароль</label>
                            <input type="password" class="form-control email" id="exampleInputPassword1" placeholder="Password">
                        </div>
                        <button type="submit" class="btn btn-warning"><p>Submit</p></button>
                    </form>
                </div>
                <div class="col-xl-4 col-lg-4 col-md-12 col-sm-12 column2 text-center">
                    <h2>Впервые на Pieceofcake?</h2>
                    <h6 style="margin-top: 30px;">Зарегестрируйтесь у нас </h6>
                    <router-link to="/signup"><button class="btn btn-warning" style="margin-top: 40px;"><p>Регистрация</p></button></router-link>
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
.login{
    margin-top: 200px;
    margin-bottom: 100px;
}
.login h1{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 64px;
    line-height: 77px;
    color: #7D9A2C;
}
.login .emailLabel{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 30px;
    line-height: 36px;
    color: #D4DDCA;
}
.login .passwordLabel{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 30px;
    line-height: 36px;
    color: #D4DDCA;
}
.login .email{
    max-width: 626px;
    border-radius: 10px;
}
.login button{
    background: #F39E03;
    border: 1px solid #D4DDCA;
    box-sizing: border-box;
    border-radius: 10px;
}
.login button p{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 20px;
    line-height: 25px;
    text-align: center;
    color: #D4DDCA;
    margin: 5px 5px 5px 5px;
}
.login .column2{
    background: #D4DDCA;
    margin-top: 30px;
}
.login .column2 h2{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 40px;
    line-height: 50px;
    text-align: center;
    color: #7D9A2C;
}
.login .column2 h6{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 30px;
    line-height: 36px;
    text-align: center;
    color: rgba(0, 0, 0, 0.25);
}
</style>