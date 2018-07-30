<template>
	<div>
		<h3>所有注册用户</h3>
		<ul>
			<li v-for="item in list">
				{{item}}
			</li>
		</ul>
		<a href="/" v-on:click="quit">注销登入</a>
	</div>
</template>

<script>
    import {getCookie, setCookie, delCookie} from '../../assets/js/cookie.js'
	export default{
		data(){
			return{
				list:""
			}
		},
		mounted(){
            //this.username = getCookie("username")
            //this.token = getCookie("token")
            //setCookie("username",this.username,1000*60)
            //setCookie("token",this.token,1000*60)  
            console.log(this.token)
			this.axios.get("http://127.0.0.1:5000/main",{headers: {'token':'123' }}).then(
				(res)=>{
					this.list = res.data
					console.log(res)
					console.log(res.data)
				}
			)
          
             
		},
		methods:{
			quit(){
				delCookie("username")
			}
		}
	}
</script>

<style>
	ul{padding: 0;}
	ul li{list-style: none;}
</style>
