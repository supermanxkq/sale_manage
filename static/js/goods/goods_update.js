/**
 * Created by xukaiqiang on 2019/7/4.
 */
$(function () {

    $("#update_goods").click(function () {
        var updateFormData = $(".update_goods_form").find("form")[0];
        var formData = new FormData(updateFormData);
        $.ajax({
            url: '/goods_update/',
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

})