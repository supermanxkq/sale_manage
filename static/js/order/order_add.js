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

        var selectGoods = function () {
            var selectModel = $('#myModal');
            selectModel.on('show.bs.modal', function () {
                var datas = {};
                $.ajax({
                    url: '/queryGoodsNameList/',
                    data: data_param,
                    type: 'POST',
                    dataType: 'json',
                    success: function (res) {
                        $("#goodsList").html("");
                        $.each(res, function (i, item) {
                            $("#goodsList").append('<tr><td><input data-goods-id=' + item.pk + ' type="checkbox" name="goods_id" class="check_goods"/> </td><td><img src=' + item.fields.img + ' width="30px" height="30px"/></td><td>' + item.fields.name + '</td><td>' + item.fields.single_price + '</td></tr>');
                        })
                    }
                })
            })
            $('.addGoods', selectModel).click(function () {
                var rowHtml = '';
                $('input[name="goods_id"]:checked').each(function (i, item) {
                    var datas = {'goodsId': $(this).data('goodsId')};
                    $.ajax({
                        async: false,
                        url: '/queryGoodsById/',
                        data: datas,
                        type: 'POST',
                        dataType: 'json',
                        success: function (res) {
                            rowHtml += '<tr ><td><input type="hidden" name="goods_id" value=' + res[0].pk + ' /><input type="hidden" name="goods_name" value=' + res[0].fields.name + ' /><img src=' + res[0].fields.img + ' width="30px" height="30px"/></td><td>' + res[0].fields.name + '</td><td>' + res[0].fields.single_price + '</td><td><input type="number" name="num" class="form-control input-sm"/></td></tr>';
                            console.log('rowHtml' + rowHtml)
                        }
                    });

                })
                $("#checkGoodsList").append(rowHtml);
                selectModel.modal('hide');
            })
        }
        selectGoods();


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

        $(".addOrder").click(function () {
            var formData=$(".addOrderForm").serialize();
            $.ajax({
                url: '/add_order/',
                type: 'POST',
                data: formData,
                dataType:'json',
                success: function (res) {
                    window.location.href = '/queryOrderList/';
                    return false;
                }
            });
            return false;
        })
    }
)