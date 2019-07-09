/**
 * Created by xukaiqiang on 2019/6/23.
 */
$(function () {
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

    $("img").zoomify({
        scale:0.5,
    });
})