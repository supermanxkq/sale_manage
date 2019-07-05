/**
 * Created by xukaiqiang on 2019/7/4.
 */
$(function () {
    $(".updatePwd").click(function () {
        var form_data = $(".update_pwd_form").serialize();
        $.ajax({
            url:'/updatePwd/',
            type:'POST',
            dataType: "json",
            data:form_data,
            success:function (res) {
                if(res==-1){
                    $("#info").html('旧密码错误！')
                }else if(res==-2){
                    $("#info").html('没有权限！')
                }else{
                    window.location.href="/logout"
                }

            }
        })
    });
})