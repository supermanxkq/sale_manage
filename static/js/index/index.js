/**
 * Created by xukaiqiang on 2019/7/4.
 */
$(function () {
    var datas = {};
    $.ajax({
        url: '/queryMsgList/',
        type: 'post',
        data: datas,
        dataType: 'json',
        success: function (res) {
            //  $("#msg_content").html('<tr><td>' + item.fields.name +
            // '</td><td>' + item.fields.create_time + '</td></tr>');
            $.each(res,function (i,item) {
                 $("#msg_content").append('<tr><td class="text-danger" colspan="4">'+(i+1)+'.' + item.fields.name +':'+item.fields.goods_name+'不足'+item.fields.num+'个!</td></tr>');
            })
        }
    });
})