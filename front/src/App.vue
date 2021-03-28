<template>
  <div>
    <router-view/>
  </div>
</template>

<script>
import Header from './components/header.vue';
import Footer from './components/footer.vue';
import Main from './components/main.vue';

export default {
  components: {
    Header,
    Footer,
    Main
    },
}
</script>
<style>

</style>
