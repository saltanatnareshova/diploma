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
                                    <a href="#" class="information">+7(777)-777-77-77</a>
                                </div>
                            </div>
                        </li>
                        <li class="d-flex nav-item before">
                            <div class="media info">
                                <img class="phone" src="../images/email.png" style="padding-top: 3px;">
                                <div class="body">
                                    <a href="#" class="email">pieceofcake@mail.ru</a>
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
    padding: 10px 56px 10px 56px;
    background: #7D9A2C;
}
.footer .logo{
    width: 50px;
}
.footer .phone{
    width: 20px;
}
.footer .information, .footer .email{
    font-family: Circular Std;
    font-size: 15px;
    line-height: 24px;
    color: #FFFFFF;
}
.footer .media .body{
    padding-left: 20px;
}
.footer .info{
    padding-left: 50px;
}
.footer .nav{
    padding-top: 20px;
}
@media screen and (max-width: 453px){
  .before::before{display: none !important;}
  .footer .info{
    padding-left: 0px;
}
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