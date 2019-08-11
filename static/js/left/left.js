$(function () {
    var urlstr = location.href;　　　　//获取浏览器的url
    var urlstatus = false;　　　　　　　　//标记
    //遍历导航div
    var url_method=urlstr.split('/')[3];
    $(".page-sidebar-menu li").each(function () {
//判断导航里面的rel和url地址是否相等
        if ($(this).parent().hasClass("sub-menu")) {
              if ($(this).attr('rel')&&$(this).attr('rel').indexOf(url_method) > -1 && $(this).attr('rel') != '') {
                  $(this).parent().parent().addClass('active');
                   $(this).addClass('active');
              }else{
                   $(this).removeClass('active');
              }
        } else {
            if ($(this).attr('rel')&&$(this).attr('rel').indexOf(url_method) > -1 && $(this).attr('rel') != '') {
                $(this).addClass('active');
                urlstatus = true;
            } else {
                $(this).removeClass('active');
            }
        }
    });
//当前样式保持
//     if (!urlstatus) {
//         $("#menu a").eq(0).addClass('active');
//     }
})