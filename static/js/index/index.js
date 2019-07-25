/**
 * Created by xukaiqiang on 2019/7/4.
 */
$(function () {

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
                $(".today_add_order_count").html(res.today_add_order_count);
                $(".total_orders_month").html(res.total_orders_month);
                $(".total_amount_of_month").html(res.total_amount_of_month);
                $(".total_amount_of_year").html(res.total_amount_of_year);
                $(".total_profit_of_month").html(res.total_profit_of_month);
                $(".total_profit_of_year").html(res.total_profit_of_year);
            }
        });
    }
    queryTodayOrders();
    function getPieStatistics() {

    }

    getCharts();
    /* 图表 */
    function getCharts() {
        // var dataList = [];
        // var nameList = [];
        // var objList = [];
        // var datas_statictics = {};
        // $.ajax({
        //     url: '/queryStatisticsData/',
        //     type: 'POST',
        //     data: datas_statictics,
        //     dataType: 'json',
        //     async: false,
        //     success: function (res) {
        //         dataList = res.dataList;
        //         nameList = res.nameList;
        //         objList = res.objList;
        //     }
        // });


        //基于准备好的dom，初始化echarts实例
        // var myChart = echarts.init(document.getElementById('annular'));
        // var myPieChart = echarts.init(document.getElementById('pie_statistics'));

        // option_pie = {
        //     title: {
        //         text: '销售百分比',
        //         subtext: '',
        //         x: 'center'
        //     },
        //     tooltip: {
        //         trigger: 'item',
        //         formatter: "{a} <br/>{b} : {c} ({d}%)"
        //     },
        //     legend: {
        //         orient: 'vertical',
        //         left: 'right',
        //         data: nameList
        //     },
        //     series: [
        //         {
        //             name: '销售占比',
        //             type: 'pie',
        //             radius: '55%',
        //             center: ['50%', '60%'],
        //             data: objList,
        //             itemStyle: {
        //                 emphasis: {
        //                     shadowBlur: 10,
        //                     shadowOffsetX: 0,
        //                     shadowColor: 'rgba(0, 0, 0, 0.5)'
        //                 }
        //             }
        //         }
        //     ]
        // };
        // option = {
        //     title: {
        //         text: '销售数量统计',
        //         subtext: '',
        //         x: 'center'
        //     },
        //     color: ['#c23531'],
        //     tooltip: {
        //         trigger: 'axis',
        //         axisPointer: {            // 坐标轴指示器，坐标轴触发有效
        //             type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        //         }
        //     },
        //     grid: {
        //         left: '3%',
        //         right: '4%',
        //         bottom: '3%',
        //         containLabel: true
        //     },
        //     xAxis: [
        //         {
        //             type: 'category',
        //             data: nameList,
        //             axisTick: {
        //                 alignWithLabel: true
        //             }
        //         }
        //     ],
        //     yAxis: [
        //         {
        //             type: 'value'
        //         }
        //     ],
        //     series: [
        //         {
        //             name: '销售数量',
        //             type: 'bar',
        //             barWidth: '60%',
        //             data: dataList
        //         }
        //     ]
        // };


        // 使用刚指定的配置项和数据显示图表。
        // myChart.setOption(option);
        // window.onresize = myChart.resize;
        // myPieChart.setOption(option_pie);
        // window.onresize = myPieChart.resize;
    }


})