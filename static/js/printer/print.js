/**
 * Created by xukaiqiang on 2019/7/19.
 */
$(function () {
    var LODOP; //声明为全局变量
   // var url='';
   // $.ajax({
   //     url:'',
   //     type:'post',
   //     dataType:'json',
   //     data:dataParam,
   //     success:function (res) {
   //  CreatePrintPage(res);
   //     }
   // })

    function CreatePrintPage(){
		//json 创建模拟服务器响应的订单信息对象
		var json = {"title":"小野点餐系统", "name":"张三", "phone": "138123456789", "orderTime": "2012-10-11 15:30:15",
		"orderNo": "20122157481315", "shop":"XX连锁", "total":25.10,"totalCount":6,
		"goodsList":[
		{"name":"菜心(无公害食品)", "price":5.00, "count":2, "total":10.08},
		{"name":"菜心(无公害食品)", "price":5.00, "count":2, "total":10.02},
		{"name":"旺菜", "price":4.50, "count":1, "total":4.50},
		{"name":"黄心番薯(有机食品)", "price":4.50, "count":1, "total":4.50}
		]
		}
		var hPos=10,//小票上边距
		pageWidth=580,//小票宽度
		rowHeight=15,//小票行距
		//获取控件对象
		LODOP=getLodop(document.getElementById('LODOP_OB'),document.getElementById('LODOP_EM'));
		//初始化
		LODOP.PRINT_INIT("打印控件功能演示_Lodop功能_名片");
		//添加小票标题文本
		LODOP.ADD_PRINT_TEXT(hPos,30,pageWidth,rowHeight,"小野点餐系统");
		//上边距往下移
		hPos+=rowHeight;

		LODOP.ADD_PRINT_TEXT(hPos,1,pageWidth,rowHeight,"姓名:");
		LODOP.ADD_PRINT_TEXT(hPos,30,pageWidth,rowHeight,json.name);
		//hPos+=rowHeight; //电话不换行
		LODOP.ADD_PRINT_TEXT(hPos,70,pageWidth,rowHeight,"电话:");
		LODOP.ADD_PRINT_TEXT(hPos,100,pageWidth,rowHeight,json.phone);
		hPos+=rowHeight;
		LODOP.ADD_PRINT_TEXT(hPos,1,pageWidth,rowHeight,"下单时间:");
		LODOP.ADD_PRINT_TEXT(hPos,60,pageWidth,rowHeight,json.orderTime);
		hPos+=rowHeight;
		LODOP.ADD_PRINT_TEXT(hPos,1,pageWidth,rowHeight,"订单编号:");
		LODOP.ADD_PRINT_TEXT(hPos,60,pageWidth,rowHeight,json.orderNo);
		hPos+=rowHeight;
		LODOP.ADD_PRINT_TEXT(hPos,1,pageWidth,rowHeight,"取货门店:");
		LODOP.ADD_PRINT_TEXT(hPos,60,pageWidth,rowHeight,json.shop);
		hPos+=rowHeight;
		LODOP.ADD_PRINT_LINE(hPos,2, hPos, pageWidth,2, 1);
		hPos+=5;
		LODOP.ADD_PRINT_TEXT(hPos,1,pageWidth,rowHeight,"品名");
		LODOP.ADD_PRINT_TEXT(hPos,70,pageWidth,rowHeight,"单价");
		LODOP.ADD_PRINT_TEXT(hPos,110,pageWidth,rowHeight,"数量");
		LODOP.ADD_PRINT_TEXT(hPos,140,pageWidth,rowHeight,"小计");
		hPos+=rowHeight;
		//遍历json的商品数组
		for(var i=0;i<json.goodsList.length;i++){

			if(json.goodsList[i].name.length<4){
				LODOP.ADD_PRINT_TEXT(hPos,1,pageWidth,rowHeight,json.goodsList[i].name);
			}else {
				//商品名字过长,其他字段需要换行
				LODOP.ADD_PRINT_TEXT(hPos,1,pageWidth,rowHeight,json.goodsList[i].name);
				hPos+=rowHeight;
			}
			LODOP.ADD_PRINT_TEXT(hPos,70,pageWidth,rowHeight,json.goodsList[i].price);
			LODOP.ADD_PRINT_TEXT(hPos,115,pageWidth,rowHeight,json.goodsList[i].count);
			LODOP.ADD_PRINT_TEXT(hPos,140,pageWidth,rowHeight,json.goodsList[i].total);
			hPos+=rowHeight;
			}
		//商品遍历打印完毕,空一行
		hPos+=rowHeight;
		//合计
		LODOP.ADD_PRINT_TEXT(hPos,80,pageWidth,rowHeight,"合计:"+json.totalCount);
		LODOP.ADD_PRINT_TEXT(hPos,130,pageWidth,rowHeight,"￥"+json.total);

		hPos+=rowHeight;
		LODOP.ADD_PRINT_TEXT(hPos,2,pageWidth,rowHeight,(new Date()).toLocaleDateString()+" "+(new Date()).toLocaleTimeString())
		hPos+=rowHeight;
		LODOP.ADD_PRINT_TEXT(hPos,25,pageWidth,rowHeight,"谢谢惠顾,欢迎下次光临!");
		//初始化打印页的规格
		LODOP.SET_PRINT_PAGESIZE(3,pageWidth,45,"XXXXX订单信息");
LODOP.PRINT();
	};
})