<template>
    <div>
        <h3>欢迎{{name}}</h3>
        <!-- 教程中href是#，但是我测试注销后不能自动跳到 -->
        <a href="/" v-on:click="quit">注销登入</a>
    </div>
</template>

<script>
import {getCookie, delCookie} from '../../assets/js/cookie.js'
export default{
  data () {
    return {
      name: ''
    }
  },
  mounted () {
    //let uname = getCookie('username')
    //this.name = uname
    //setCookie("username",this.username,1000*60)
    //setCookie("token",this.token,1000*60)  
    if (uname == '') {
      this.$router.push('/')
    }
  },
  methods: {
    quit () {
      delCookie('username')
    }
  }
}
</script>

<style>
</style>
