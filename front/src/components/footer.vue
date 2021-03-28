<template>
    <div>
        <div class="footer">
            <div class="row">
                <div class="col-lg-12 col-md-12 col-sm-12">
                    <img class="logo" src="../images/logo.png">
                </div>
                <div class="col-lg-12 col-md-12 col-sm-12">
                     <ul class="nav justify-content-left">
                        <li class="nav-item">
                            <div class="media" style="padding-top: 1px;">
                                <img class="phone" src="../images/phone.png">
                                <div class="body">
                                    <p class="information">+7(777)-777-77-77</p>
                                </div>
                            </div>
                        </li>
                        <li class="d-flex nav-item before">
                            <div class="media">
                                <img class="phone" src="../images/email.png" style="padding-top: 3px;">
                                <div class="body">
                                    <p class="information">pieceofcake@mail.ru</p>
                                </div>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'Footer'
}
</script>
<style scoped>
.footer{
    background: #7D9A2C;
}
.footer .logo{
    margin: 16px 0px 15px 50px;
}
.footer .phone{
    width: 20px;
}
.footer .information{
    font-family: Supermercado;
    font-style: normal;
    font-weight: normal;
    font-size: 15px;
    line-height: 24px;
    color: #FFFFFF;
}
.footer .media .body{
    padding-left: 20px;
}
.footer .media{
    padding-left: 50px;
}
@media screen and (max-width: 453px){
  .before::before{display: none !important;}
}
.before::before{
  display: inline-block;
  color: white;
  content: "|";
  display: flex;
  align-items: center;
  height: 20px;
  padding-left: 25px;
}
</style>