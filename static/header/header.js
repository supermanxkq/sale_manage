/**
 * Created by xukaiqiang on 2019/7/2.
 */
$(function () {
    $(".menus li").click(function () {
        $(this).addClass("active").siblings(".active").removeClass("active");
    })
    // $(".menus li ul li").click(function () {
    //     $(this).parent().parent().addClass("active").siblings().removeClass("active");
    // })
})