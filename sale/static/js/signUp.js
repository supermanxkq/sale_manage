/**
 * Created by xukaiqiang on 2019/6/23.
 */
$(function () {
    //登录
    $("#signUp").click(function () {
        var loginData = $(".signUpForm").serialize();
        $.ajax({
            type: "POST",
            url: "/signUp/",
            data:loginData,
            dataType: "json",
            success:function(res) {
                // if (res.status==1001) {
                //     window.location='/index';
                // } else {
                $("#searchResult").html(res.message);
                // }
            }
        });
    })
})