$(document).ready(function () {
    $.ajax({
        url: '/getorder',
        type: 'GET',
        datatype: 'json',
        success: function (data) {
            var obj = JSON.parse(data);
            if (obj.status == 201){
                this.error(xhr=obj);
                return
            }
            $(function () {
                // var obj1 = JSON.parse(data);
                $("#J_TbData").empty();
                for (var i = 0; i < obj.data.length; i++) {
                    //动态创建一个tr行标签,并且转换成jQuery对象
                    var $trTemp = $("<tr></tr>");
                    //往行里面追加 td单元格
                    $trTemp.append("<td class='order'>" + obj.data[i].id + "</td>");
                    $trTemp.append("<td class='order'>" + obj.data[i].name + "</td>");
                    $trTemp.append("<td class='order'>" + obj.data[i].num + "</td>");
                    // $("#J_TbData").append($trTemp);
                    $trTemp.appendTo("#J_TbData");
                }
            });
        }, error: function (xhr, type, errorThrown) {
            alert(xhr.data)
        }
    })
})