$(document).ready(function () {
    $.ajax({
        type: "GET",
        url: "/getwordcloud",
        // data: "name=John&location=Boston",
        success: function (msg) {
            var obj1 = JSON.parse(msg)
            if (obj1.status == 201) {
                this.erro(xhr = obj1)
                return
            }
            var data = obj1.data.split(/[,\. ]+/g)
                .reduce(function (arr, word) {
                    var obj = arr.find(function (obj) {
                        return obj.name === word;
                    });
                    if (obj) {
                        obj.weight += 1;
                    } else {
                        obj = {
                            name: word,
                            weight: 1
                        };
                        arr.push(obj);
                    }
                    return arr;
                }, []);
            Highcharts.chart('word_cloud', {
                chart: {
                    backgroundColor: 'rgba(0,0,0,0)'
                },
                series: [{
                    type: 'wordcloud',
                    data: data
                }],
                title: {
                    text: '企业福利词云图'
                }
            });
        },
        erro: function (xhr, type, errorThrown) {
            alert(xhr.data)
        }
    });
});
