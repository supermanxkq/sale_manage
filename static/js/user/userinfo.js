/**
 * Created by xukaiqiang on 2019/6/23.
 */
$(function () {
    $("#updateUserInfoBtn").click(function () {
        var addFormData = $(".updateUserInfoDiv").find("form")[0];
        var formData = new FormData(addFormData);
        $.ajax({
            type: "POST",
            url: "/updateUserInfo/",
            data: formData,
            cache: false,
            async: false,
            contentType: false,
            processData: false,
            success: function (res) {
                window.location.href = "/"
            }
        });
    })
})
//=
// })