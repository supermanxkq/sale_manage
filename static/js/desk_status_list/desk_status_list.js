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
                 $(".order_goods_list").html(html);
                $.each(res,function (i,item) {
                    html+='<tr class="odd gradeX"><td>'+item.fields.goods_id+'</td><td class="hidden-480">'+item.fields.goods_name+'</td><td class="hidden-480">'+item.fields.num+'</td><td class="hidden-480">'+item.fields.sale_price+'</td><td class="hidden-480">'+item.fields.order_id+'</td></tr>';
                })

                $(".order_goods_list").html(html);
                $(".confirmSettleOrder").data('deskId',desk_id)
                console.log(res)
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