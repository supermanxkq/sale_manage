/**
 * Created by xukaiqiang on 2019/6/23.
 */
$(function () {
    //登录
    $("#signUp").click(function () {
        var addFormData = $(".signUpForm").find("form")[0];
        var formData = new FormData(addFormData);
        $.ajax({
            type: "POST",
            url: "/signUp/",
            data:formData,
            cache: false,
            async: false,
            contentType: false,
            processData: false,
            success:function(res) {
                window.location.href="/loginPage/"
                // $("#searchResult").html(res.message);
            }
        });
    })
})