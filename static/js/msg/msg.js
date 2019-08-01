/**
 * Created by xukaiqiang on 2019/7/12.
 */
$(function () {
    var datas = {};
    $.ajax({
        url: '/queryMsgList/',
        type: 'post',
        data: datas,
        dataType: 'json',
        success: function (res) {
            if(res.length>0){
                $(".no_notice").hide();
                 $(".noticeNum").html(res.length).show();
            }else{
                $(".notice_num").hide();
                $(".no_notice").show();
            }
            $.each(res, function (i, item) {
                $(".notification li:eq(0)").append('<li><a href="#"><span class="label label-important"><i class="icon-bolt"></i></span>【' + item.fields.goods_name + '】不足' + item.fields.num + '个!  <span class="time">' + getDateDiff(new Date(item.fields.create_time).getTime()) + '</span></a></li>');
            })
        }
    });
    //计算时差  dateTimeStamp为时间戳
    function getDateDiff(dateTimeStamp) {
        var minute = 1000 * 60;
        var hour = minute * 60;
        var day = hour * 24;
        var halfamonth = day * 15;
        var month = day * 30;
        var now = new Date().getTime();
        var diffValue = now - dateTimeStamp;
        if (diffValue < 0) {
            //若日期不符则弹窗口告之,结束日期不能小于开始日期！
        }
        var monthC = diffValue / month;
        var weekC = diffValue / (7 * day);
        var dayC = diffValue / day;
        var hourC = diffValue / hour;
        var minC = diffValue / minute;
        if (monthC >= 1) {
            result = parseInt(monthC) + "个月前";
        }
        else if (weekC >= 1) {
            result = parseInt(weekC) + "周前";
        }
        else if (dayC >= 1) {
            result = parseInt(dayC) + "天前";
        }
        else if (hourC >= 1) {
            result = parseInt(hourC) + "个小时前";
        }
        else if (minC >= 1) {
            result = parseInt(minC) + "分钟前";
        } else
            result = "刚刚";
        return result;
    }
})