<template>
    <div>
        <Header />
        <div class="container signup">
            <h1>Зарегестрироваться на A Pieace of Cake </h1>
            <p>уже есть акканут? <router-link to="login">Вход</router-link></p>
            <form>
                <div class="row" style="margin-bottom: 30px;">
                    <div class="col-xl-6 col-lg-6 col-md-12 col-sm-12">
                        <input type="text" class="form-control" v-model="formData.username"  aria-describedby="emailHelp" placeholder="Имя пользователя">
                    </div>
                    <div class="col-xl-6 col-lg-6 col-md-12 col-sm-12">
                        <input type="text" class="form-control" v-model="formData.first_name"  aria-describedby="emailHelp" placeholder="Имя">
                    </div>
                </div>
                <div class="form-group">
                    <input type="email" class="form-control" v-model="formData.email"  placeholder="e-mail">
                </div>
               <input type="password" class="form-control" v-model="formData.password" aria-describedby="emailHelp" placeholder="Пароль">
                <div class="form-check" style="margin-top: 30px;">
                    <input type="checkbox" class="form-check-input" id="exampleCheck1" required="true">
                    <label class="form-check-label" for="exampleCheck1">Я ознакомлен(а) с Политикой конфиденциальности и даю согласие на обработку моих персональных данных. Я принимаю условия  
Пользовательского соглашения
 </label>
                </div>
                <button type="submit" class="btn btn-warning" @click.prevent="submit"><p>Регистрация</p></button>
            </form>
        </div>
        <Footer />
    </div>
</template>
<script>
import Header from './header'
import Footer from './footer'
export default {
    data(){
        return{
            formData:{
                email: '',
                username: '',
                password: '',
                first_name: ''
            }
        }
    },
    components:{
        Header,
        Footer
    },
    methods:{
        submit(){
            this.$store.dispatch('signup', this.formData);
            console.log(this.formData);
        }
    }
}
</script>
<style scoped>
.signup{
    margin-top: 200px;
    margin-bottom: 100px;
}
.signup h1{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 36px;
    line-height: 43px;
    text-align: center;
    color: #F39E03;
}
.signup p{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 30px;
    line-height: 36px;
    text-align: center;
    color: rgba(0, 0, 0, 0.25);
}
.signup .form-check-label{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 22px;
    color: #D4DDCA;
}
@media screen and (max-width: 992px) {
    .form-control{
        margin-top: 20px;
    }
}
.signup button p{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 20px;
    line-height: 20px;
    text-align: center;
    color: #D4DDCA;
}
.signup button{
    margin-top: 30px;
    padding: 10px 5px 0px 5px;
}
</style>