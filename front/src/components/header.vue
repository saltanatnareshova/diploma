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
                                        <p class="information">+7(777)-777-77-77</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-6 col-md-6 col-sm-6 col-12">
                                <div class="media">
                                    <img class="phone" src="../images/email.png" style="padding-top: 3px;">
                                    <div class="body">
                                        <p class="information">pieceofcake@mail.ru</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6 col-md-6 col-sm-6 col-12">
                        <div class="float-right">
                            <router-link to="/login"><button class="btn btn-outline-warning">Пользователям</button></router-link>
                            <router-link to="/request"><button class="btn btn-outline-warning" style="margin-left: 10px;">Ресторанам</button></router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="nav-header">
        <div class="container">
            <nav class="navbar navbar-expand-lg navbar-light">
                <img src="../images/logo.png">
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
                </button>
            
                <div class="collapse navbar-collapse text-right" id="navbarTogglerDemo02">
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
                </div>
            </nav>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Header'
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