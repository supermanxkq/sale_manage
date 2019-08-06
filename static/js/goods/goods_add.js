/**
 * Created by xukaiqiang on 2019/7/4.
 */
$(function () {
    function queryGoodsTypeList() {
        var data = {};
        var result_data;
        $.ajax({
            type: "POST",
            url: "/query_goodstype_list/",
            data: data,
            dataType: "json",
            success: function (result) {
                result_data = result;
                console.log(result[0].fields.name)
                $.each(result, function (i, item) {
                    $("#select_goodsType_list").append("<option value=" + item.pk + ">" + item.fields.name + "</option>");
                })
                // $("#merchants_name_name").val(result[0].fields.name)
            }
        })
    }

    $("#save_goods").click(function () {
        var addFormData = $(".add_goods_form").find("form")[0];
        var formData = new FormData(addFormData);
        $.ajax({
            url: '/add_goods/',
            type: 'POST',
            data: formData,
            cache: false,
            async: false,
            contentType: false,
            processData: false,
            success: function (res) {
                window.location.href = '/goods_list_page/';
            }
        });
    })


    queryGoodsTypeList();

})