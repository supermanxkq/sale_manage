$(function () {
    $("#name").keyup(function () {
         var name=$("#name").val();
    var data_param={'name': name};
    $.ajax({
        url:'/queryNameCharacter/',
        data:data_param,
        type:'post',
        dataType:'json',
        success:function (result) {
            $("#lblResult").val(result.result);
        }
    })
    });
})