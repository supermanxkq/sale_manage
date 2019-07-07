/**
 * Created by xukaiqiang on 2019/7/7.
 */
$(function () {
    //获取客户列表
    var data_param = {};
    $.ajax({
        url: '/query_customer_list/',
        data: data_param,
        type: 'POST',
        dataType: 'json',
        success: function (res) {
            $.each(res, function (i, item) {
                $("#select_customers_list").append('<option value=' + item.pk + '>' + item.fields.name + '</option>')
            })

        }
    })
    $('#myModal').on('show.bs.modal', function (e) {
        var datas = {};
        $.ajax({
            url: '/queryGoodsNameList/',
            data: data_param,
            type: 'POST',
            dataType: 'json',
            success: function (res) {
                $("#goodsList").html("");
                $.each(res, function (i, item) {
                    $("#goodsList").append('<tr><td><input type="checkbox"/> </td><td><img src=' + item.fields.img + ' width="30px" height="30px"/></td><td>' + item.fields.name + '</td><td>' + item.fields.single_price + '</td><td><input type="text" class="form-control input-sm"/> </td></tr>')
                })
            }
        })
    }).on('hide.bs.modal', function (e) {
    })


    $(".input-group.date").datepicker({
        language: 'zh-CN',
        format: 'yyyy-mm-dd',
        todayBtn: true,
        autoclose: true,
        todayHighlight: true,
        orientation: 'bottom',
        // startDate:new Date(),
        // endDate:new Date(),
    })
    $(".input-group.date").datepicker("setDate", new Date());


})