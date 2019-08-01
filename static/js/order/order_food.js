/**
 * Created by xukaiqiang on 2019/7/7.
 */
$(function () {
        $("body").addClass("page-sidebar-closed");
        $(".order_food").click(function () {
            $(".goods_num").val('');
            $("#goods_id").val($(this).data("id"));
            $(".goods_name").val($(this).data("name"));
            $(".sale_price").val($(this).data("salePrice"))
        })

        $(".addShopCart").click(function () {
            //防止重复提交
            $(".addShopCart").attr({ disabled: "disabled" });;
            var myModal = $("#orderFood");
            var form_data = $(".addShopCartForm").serialize();
            $.ajax({
                url: '/addShopCart/',
                type: 'POST',
                data: form_data,
                async:false,
                dataType: 'json',
                success: function (res) {
                    if (res.stauts == 1) {
                        myModal.modal('hide');
                    }
                }
            })
        })

      $("#orderFood").on('show.bs.model',function () {
           $(".addShopCart").removeAttr("disabled")
      });

        $(document).on('click', ".query_cart_list", function () {
            var form_data = {};
            $.ajax({
                url: '/query_cart_list/',
                type: 'POST',
                data: form_data,
                dataType: 'json',
                success: function (res) {
                    $(".cart_list_data").html('');
                    $.each(res, function (i, item) {
                        $(".cart_list_data").append('<tr><td>' + item.fields.goods_id + '</td><td>' + item.fields.goods_name + '</td><td>' + item.fields.num + '</td> <td>' + item.fields.sale_price + '</td><td>' + parseFloat(item.fields.sale_price) * parseFloat(item.fields.num) + '</td><td class="center hidden-480">   <a class="delete_cart" data-pk="' + item.pk + '" href="javascript:void(0);"><i class="icon-trash" style="font-size: 17px;"></i></a></td> </tr>')

                    })
                }
            })
        })

        $(document).on('click', ".delete_cart", function () {
            var form_data = {};
            $.ajax({
                url: '/delete_cart/'+$(this).data('pk'),
                type: 'POST',
                data: form_data,
                dataType: 'json',
                success: function (res) {
                    if (res.status == 1) {
                        var form_data = {};
                        $.ajax({
                            url: '/query_cart_list/',
                            type: 'POST',
                            data: form_data,
                            dataType: 'json',
                            success: function (res) {
                                $(".cart_list_data").html('');
                                $.each(res, function (i, item) {
                                    $(".cart_list_data").append('<tr><td>' + item.fields.goods_id + '</td><td>' + item.fields.goods_name + '</td><td>' + item.fields.num + '</td> <td>' + item.fields.sale_price + '</td><td>' + parseFloat(item.fields.sale_price) * parseFloat(item.fields.num) + '</td><td class="center hidden-480">   <a class="delete_cart" data-pk="' + item.pk + '" href="javascript:void(0);"><i class="icon-trash" style="font-size: 17px;"></i></a></td> </tr>')

                                })
                            }
                        })
                    }
                }
            })
        })
    }
)