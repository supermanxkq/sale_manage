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
})