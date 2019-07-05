/**
 * Created by xukaiqiang on 2019/7/4.
 */
$(function () {
    function queryMerchants() {
        var data = {};
        var result_data;
        $.ajax({
            type: "POST",
            url: "/queryMerchants/",
            data: data,
            dataType: "json",
            success: function (result) {
                result_data = result;
                console.log(result[0].fields.name)
                $.each(result, function (i, item) {
                    $("#select_merchants_list").append("<option value=" + item.pk + ">" + item.fields.name + "</option>");
                })
                $("#merchants_name").val(result[0].fields.name)
            }
        })
    }

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

    queryMerchants();
    queryGoodsTypeList();

})