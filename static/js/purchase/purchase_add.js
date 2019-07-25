/**
 * Created by xukaiqiang on 2019/7/3.
 */
$(function () {
    /**获取数据库中的商品信息**/
    var data = {};
    var result_data;
    $.ajax({
        type: "POST",
        url: "/queryGoodsNameList/",
        data: data,
        dataType: "json",
        success: function (result) {
            result_data = result;
            // res = $.parseJSON(result);
            // objStr = result["data"];
            // console.log(result["fields"][0]["goods_name"]);
            console.log(result[0].fields.name)
            $.each(result, function (i, item) {
                $("#select_goods_list").append("<option value=" + item.pk + ">" + item.fields.name + "</option>");
            })
            $("#goods_name").val(result[0].fields.name)
            $("#single_price").val(result[0].fields.single_price)
        }
    })
    $("#select_goods_list").change(function () {
        $("#num").val("");
        $("#total_price").val("");
        $("#goods_name").val($("#select_goods_list option:selected").text());
        $.each(result_data, function (i, item) {
            if (item.pk == $("#select_goods_list").val()) {
                $("#single_price").val(item.fields.single_price)
            }
        })
    })
    $("#num").blur(function () {
        $("#total_price").val($("#num").val() * $("#single_price").val())
    })
})