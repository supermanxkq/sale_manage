/**
 * Created by xukaiqiang on 2019/7/4.
 */
$(function () {
    var datas = {};
    $.ajax({
        url: '/queryMsgList/',
        type: 'post',
        data: datas,
        dataType: 'json',
        success: function (res) {
            //  $("#msg_content").html('<tr><td>' + item.fields.name +
            // '</td><td>' + item.fields.create_time + '</td></tr>');
            $.each(res, function (i, item) {
                $("#msg_content").append('<tr><td class="text-danger" colspan="4">' + (i + 1) + '.' + item.fields.name + ':【' + item.fields.goods_name + '】不足' + item.fields.num + '个!</td></tr>');
            })
        }
    });
    /**
     * 查询今日销售量
     */
    var queryTodayOrders = function () {
        var datas_param = {};
        $.ajax({
            url: '/queryTodayOrders/',
            type: 'post',
            data: datas_param,
            dataType: 'json',
            success: function (res) {
                $("#orderNums").html(res.count);
                $("#todayTotalAmount").html(res.todayTotalAmount);
                $("#total_amount").html(res.total_amount);
                $("#total_orders").html(res.total_orders);
            }
        });
    }
    queryTodayOrders();
    getCharts();
    /* 图表 */
    function getCharts() {
        var dataList = [];
        var nameList = [];
        var datas_statictics = {};
        $.ajax({
            url: '/queryStatisticsData/',
            type: 'POST',
            data: datas_statictics,
            dataType: 'json',
            async: false,
            success: function (res) {
                dataList = res.dataList;
                nameList = res.nameList;
                $(".case-list").html("");
                // <li>共6款金融产品</li>
                //           <li><span></span> 吉他</li>
                //           <li><span></span> 电吉他</li>
                //           <li><span></span> 吉他配件</li>
                //           <li><span></span> 鼓</li>
                //           <li><span></span> 拇指琴</li>
                //           <li><span></span> 尤克里里</li>
                $(".case-list").append('<li>共' + nameList.length + '款产品</li>');
                $.each(nameList, function (i, item) {
                    $(".case-list").append('<li><span></span> ' + item + '</li>')
                })
            }
        });


        //基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('annular'));
        var colorList = ['#FDC587', '#FFA5C5', '#CFA0FF', '#A6C7FF', '#A1DFF5', '#DBEEBE'];
        var itemStyle = {
            normal: {
                color: function (params) {
                    return colorList[params.dataIndex]
                },
            }
        };

        /*  var data:function(){
         var datalength=series.length;
         for(var i=0;i<datalength;i++){
         var thisdata=new array[datalength];
         thisdata[i]=dataList[i];
         series[i].data=thisdata;
         }
         };*/
        option = {
            title: {
                subtext: '单位:把',
                x: 'right',
                y: 40,
                textStyle: {
                    fontSize: 12,
                    color: '#666'
                },
                padding: 80
            },
            tooltip: {
                borderColor: '#1D1D26',//悬浮框颜色
            },
            color: colorList,
            /*   legend: {
             x:'right',
             y:70,
             align:'right',
             itemWidth:16,
             itemGap:20,
             orient:'vertical',
             data:['消费贷','现金贷','教育贷','循环贷','消费分期a','消费分期b']
             },*/
            calculable: false,
            grid: {
                borderWidth: 0,
                borderColor: '#1D1D26',
                y: 80,
                y2: 60
            },
            xAxis: [
                {
                    type: 'category',
                    show: false,
                    data: nameList,
                    axisTick: {
                        /* x轴相关设置*/
                        alignWithLabel: false
                    }
                }
            ],
            yAxis: [
                {
                    type: 'value',
                    axisLine: {
                        show: false,
                        onZero: true
                    },
                    axisLabel: {
                        show: true,
                        inside: false,
                        textStyle: {
                            color: '#666',
                            fontSize: 12
                        }
                    },
                    color: ['#1D1D26'],
                    show: true
                }
            ],
            series: [
                {
                    type: 'bar',
                    barWidth: '30',
                    itemStyle: itemStyle,
                    data: dataList
                }
            ]
            /*   series: [
             {
             name: '消费贷',
             type: 'bar',
             barWidth: '30',
             itemStyle: itemStyle,
             data : ['130',, ,, , ]
             },
             {
             name: '现金贷',
             type: 'bar',
             barWidth: '30',
             itemStyle: itemStyle,
             data : [, '140',,,,]
             },
             {
             name: '教育贷',
             type: 'bar',
             barWidth: '30',
             itemStyle: itemStyle,
             data : [,, '76', ,,]
             },
             {
             name: '循环贷',
             type: 'bar',
             barWidth: '30',
             itemStyle: itemStyle,
             data : [, , , '138',, ]
             },
             {
             name: '消费分期a',
             type: 'bar',
             barWidth: '30',
             itemStyle: itemStyle,
             data : [, , , , '62', ]
             },
             {
             name: '消费分期b',
             type: 'bar',
             barWidth: '30',
             itemStyle: itemStyle,
             data : [, , ,, , '100']
             }
             ]*/
        };
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.onresize = myChart.resize;
    }

})