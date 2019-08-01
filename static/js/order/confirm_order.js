/**
 * Created by xukaiqiang on 2019/7/15.
 */
$(function () {

    $("body").addClass("page-sidebar-closed");
    $(".printOrder").click(function () {
        var data_param = {};
        $.ajax({
            url: '/printOrder/',
            type: 'post',
            dataType: 'json',
            data: data_param,
            success: function (res) {
                var oldHtml=$('body').html();
                var newHtml=res.print_html;
                $('body').html(res.print_html)
                window.print();
                $('body').html(oldHtml)
            }
        })
    })
})