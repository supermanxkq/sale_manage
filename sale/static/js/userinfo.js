/**
 * Created by xukaiqiang on 2019/6/23.
 */
$(function () {
    var data={}
        $.ajax({
            type: "GET",
            url: "/getUserInfo/",
            dataType: "json",
            data:data,
            success:function(res) {
                $(".userinfo").deserializeObject(res)
            }
        });
})