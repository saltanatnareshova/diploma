<template>
    <div class="fixed-top">
        <div class="top-header">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-lg-4 col-md-6 col-sm-6 col-12">
                        <div class="row">
                            <div class="col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="media" style="padding-top: 1px;">
                                    <img class="phone" src="../images/phone.png">
                                    <div class="body">
                                        <a  href="#" class="information">+7(777)-777-77-77</a>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="media">
                                    <img class="phone" src="../images/email.png" style="padding-top: 3px;">
                                    <div class="body">
                                        <a href="#" class="information">pieceofcake@mail.ru</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6 col-md-6 col-sm-6 col-12">
                        <div class="float-right">
                            <router-link to="/request"><button class="btn btn-outline-warning" style="margin-right: 10px;">Ресторанам</button></router-link>
                            <router-link to="/login" v-if="!isAuth"><button class="btn btn-outline-warning">Login</button></router-link>
                            <router-link to="/signup" v-if="!isAuth"><button class="btn btn-outline-warning">Sign up</button></router-link>
                            <button class="btn btn-outline-warning" @click="logout" v-if="isAuth">Log out</button>
                            <router-link to="/orders" v-if="isAuth"><button class="btn btn-outline-warning">Orders</button></router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="nav-header">
            <div class="container">
            <b-navbar class="navbar" toggleable="lg" type="dark">
                <img src="../images/logo.png">
                <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
                <b-collapse id="nav-collapse" is-nav>
                <!-- Right aligned nav items -->
                <b-navbar-nav class="ml-auto">
                    <ul class="navbar-nav ml-auto mt-2 mt-lg-0">
                            <li class="nav-item">
                            <router-link class="nav-link active" to="/">Main </router-link>
                            </li>
                            <li class="nav-item">
                            <router-link class="nav-link" to="/about_us">About us</router-link>
                            </li>
                            <li class="nav-item">
                            <router-link class="nav-link" to="#">Best places</router-link>
                            </li>
                            <li class="nav-item">
                                <router-link class="nav-link" to="/restaurants">Restaurants</router-link>
                            </li>
                            <li class="nav-item">
                                <router-link class="nav-link" to="/cafees">Cafe</router-link>
                            </li>
                            <li class="nav-item">
                                <router-link class="nav-link" to="/canteens">Canteens</router-link>
                            </li>
                        </ul>
                </b-navbar-nav>
                </b-collapse>
            </b-navbar>
            </div>
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
}
ul{
    margin-top: 30px;
    margin-bottom: 30px;
}
ul li{
    padding-right: 30px;
}
.nav-header .nav-link{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 22px;
    text-align: center;
    color: #D5D1BD;
}
.top-header{
    background: #8ba248;
}
.top-header .row{
    padding-top: 10px;
    padding-left: 30px;
}
.top-header .information{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 15px;
    line-height: 24px;
    color: #FFFFFF;
}
.top-header .phone{
    width: 20px;
}
.top-header .media .body{
    padding-left: 20px;
}
</style>