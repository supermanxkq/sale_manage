/**
 * Created by xukaiqiang on 2019/8/11.
 */
$(function () {
    //开台
    $(".open_desk").click(function () {
        var desk_id = $(this).data('deskId');
        var data_param = {'desk_id': desk_id};
        $.ajax({
            url: '/open_desk/',
            type: 'post',
            data: data_param,
            dataType: 'json',
            success: function (res) {
                if (res.status == 'ok') {
                    window.location.href = "/to_desk_status_list/";
                }
            }
        });
    });
    //点餐
    $(".to_order_food").click(function () {
         var desk_id = $(this).data('deskId');
        var data_param = {'desk_id': desk_id};
        $.ajax({
            url: '/to_order_food/',
            type: 'post',
            data: data_param,
            dataType: 'json',
            success: function (res) {
                    window.location.href = "/OrderFood/";
            }
        });
    });
    //结账查询数据
      $(".settleOrder").click(function () {
        var desk_id = $(this).data('deskId');
        var data_param = {'desk_id': desk_id};
        $.ajax({
            url: '/querySettleOrderData/',
            type: 'post',
            data: data_param,
            dataType: 'json',
            success: function (res) {
                var html="";
                $.each(res.order.order_details,function (i,item) {
                   html+='<tr><td>'+i+'</td><td>'+item.goods_name+'</td><td>'+item.num+'</td><td>'+item.sale_price+'</td><td>'+item.sale_price*item.num+'</td></tr>';
                });
                $(".order_goods_list").html(html);
                $(".order_info").html('<p>桌号：'+res.order.desk_id+'</p><p>订单号：'+res.order.order_code+'</p><p>业务日期：'+res.order.bussinessDate+'</p><p>订单总额：'+res.order.total_price+'</p>');
                $(".confirmSettleOrder").data('deskId',desk_id)
            }
        });
    });
      //确认结账
    $(".confirmSettleOrder").click(function () {
        var desk_id = $(this).data('deskId');
        var data_param = {'desk_id': desk_id};
        var myModal = $("#settleOrder");
        $.ajax({
            url: '/confirmSettleOrder/',
            type: 'post',
            data: data_param,
            dataType: 'json',
            success: function (res) {
                myModal.modal('hide');
                window.location.href = "/to_desk_status_list/";
            }
        });
    });
})