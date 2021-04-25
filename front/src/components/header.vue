<template>
    <div class="fixed-top">
        <div class="top-header">
                <div class="row">
                    <div class="col-lg-6 col-md-12 col-sm-12 col-12 column">
                        <div class="row">
                            <div class="col-lg-3 col-md-3 col-sm-12 col-12">
                                <div class="media" style="padding-top: 1px;">
                                    <img class="top-header-icon" src="../images/phone.png">
                                    <div class="body">
                                        <a  href="#" class="information">+7(777)-777-77-77</a>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-3 col-md-3 col-sm-6 col-12">
                                <div class="media">
                                    <img class="top-header-icon" src="../images/email.png">
                                    <div class="body">
                                        <a href="#" class="information">pieceofcake@mail.ru</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6 col-md-12 col-sm-12 col-12">
                        <div class="float-right">    
                            <router-link to="/request"><button class="btn btn-warning column">Для ресторанов</button></router-link>
                            <router-link to="/login" v-if="!isAuth"><button class="btn btn-outline-warning column">Войти</button></router-link>
                            <router-link to="/signup" v-if="!isAuth"><button class="btn btn-outline-warning column">Регистрация</button></router-link>
                            <router-link to="/orders" v-if="isAuth"><button class="btn btn-warning column">Мои заказы</button></router-link>
                            <button class="btn btn-outline-warning column" @click="logout" v-if="isAuth">Выйти</button>
                        </div>
                    </div>
                </div>
        </div>
        <div class="nav-header">
            <b-navbar class="navbar" toggleable="lg" type="dark">
                <div class="media">
                <img src="../images/logo.png">
                <div class="media-body">
                    <p class="logo">Peace Of Cake</p>
                </div>
                </div>
                <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
                <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav class="ml-auto">
                    <ul class="navbar-nav ml-auto mt-2 mt-lg-0">
                            <li class="nav-item">
                            <router-link class="nav-link active" to="/">Главная </router-link>
                            </li>
                            <li class="nav-item">
                            <router-link class="nav-link" to="/about_us">О нас</router-link>
                            </li>
                            <li class="nav-item">
                            <router-link class="nav-link" to="#">ТОП рейтинг</router-link>
                            </li>
                            <li class="nav-item">
                                <router-link class="nav-link" to="/restaurants">Рестораны</router-link>
                            </li>
                            <li class="nav-item">
                                <router-link class="nav-link" to="/cafees">Кафе</router-link>
                            </li>
                            <li class="nav-item">
                                <router-link class="nav-link" to="/canteens">Фаст Фуд</router-link>
                            </li>
                        </ul>
                </b-navbar-nav>
                </b-collapse>
            </b-navbar>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Header',
    computed:{
        isAuth(){
            return this.$store.getters.isAuth
        }
    },
    methods:{
        logout(){
            this.$store.commit('logout');
            console.log("Hello");
        }
    }
}
</script>
<style scoped>
.header-logo{
    margin: 16px 0px 15px 50px;
}
.nav-header{
    background: #7D9A2C;
    padding: 10px 46px;
}
.nav-header .media .media-body .logo{
    font-family: Pacifico;
    font-size: 25px;
    line-height: 41px;
    color: #D4DDCA;
    padding: 10px;
}
.nav-header .nav-link{
    font-family: Alegreya;
    font-size: 22px;
    line-height: 25px;
    text-align: center;
    color: #D5D1BD;
}
.top-header{
    padding: 10px 56px 10px 56px;
    background: #8ba248;
}
.top-header .column{
    margin: 5px 0px 5px 0px;
}
.top-header .column .media{
    margin-left: 10px;    
}
.top-header .information{
    font-family: Circular Std;
    font-size: 15px;
    line-height: 24px;
    color: #FFFFFF;
}
.top-header .top-header-icon{
    width: 15px;
    padding-top: 5px;
}
.top-header .media .body{
    padding-left: 20px;
}
.top-header .btn{
    font-family: Circular Std;
    border-radius: 30px;
    color: white;
    padding-top: 2px;
    margin-left: 10px;
}
</style>