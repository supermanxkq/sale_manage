/**
 * Created by xukaiqiang on 2019/6/23.
 */
$(function () {
    //登录
    $("#login").click(function () {
        var data = $(".loginForm").serialize();
        $.ajax({
            type: "POST",
            url: "/login/",
            data:data,
            dataType: "json",
            success:function(res) {
                if (res.status==1001) {
                    window.location='/';
                    console.log(res.msg)
                } else if(res.status==1003) {
                    $("#searchResult").html(res.error);
                }
            }
        });
    })
})