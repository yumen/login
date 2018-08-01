<template>
	<div>
        <p>用户名：{{username}}</p>
		<h3>所有订单</h3>
		<ul>
			<li v-for="item in list">
				订单号：{{item.num}}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                订单金额：{{item.amount}}
			</li>
		</ul>
		<v-pagination :total="total" :current-page='current' @pagechange="pagechange"></v-pagination>
	</div>
</template>

<script>
    import {getCookie, delCookie} from '../../assets/js/cookie.js'
    import pagination from './pagination'
	export default{
		data(){
			return{
                username:"",
				list:"",
                total:100,
                display:10,
                current:1
			}
		},
        methods:{
            pagechange:function(currentPage) {
                console.log(currentPage)
                this.axios.get("http://127.0.0.1:5000/order/" + currentPage).then(
                    (res)=>{
                        this.list = res.data.list
                        this.total = res.data.total
                        console.log(res)
                        console.log(res.data)
                    }
                )
            }
        
        },
        mounted:function(){
            this.pagechange(1)
            this.username = getCookie("username")
        },        
        components: {
              'v-pagination': pagination,
            }     
	}
</script>

<style>
	ul{padding: 0;}
	ul li{list-style: none;}
</style>
