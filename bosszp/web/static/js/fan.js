$(document).ready(function () {
    $.ajax({
        url: '/geteducationnum',
        type: 'GET',
        datatype: 'json',
        success: function (data) {
            var obj3 = JSON.parse(data)
            if (obj3.status == 201){
                this.error(xhr=obj3)
            }
            var chart = Highcharts.chart('fan', {
                chart: {
                    backgroundColor: 'rgba(0,0,0,0)'
                },
                title: {
                    text: '学历<br>占比',
                    align: 'center',
                    verticalAlign: 'middle',
                    y: 50
                },
                tooltip: {
                    headerFormat: '{series.name}<br>',
                    pointFormat: '{point.name}: <b>{point.percentage:.1f}%</b>'
                },
                plotOptions: {
                    pie: {
                        dataLabels: {
                            enabled: true,
                            distance: -50,
                            style: {
                                fontWeight: 'bold',
                                color: 'white',
                                textShadow: '0px 1px 2px black'
                            }
                        },
                        startAngle: -90, // 圆环的开始角度
                        endAngle: 90,    // 圆环的结束角度
                        center: ['50%', '75%']
                    }
                },
                series: [{
                    type: 'pie',
                    name: '学历占比',
                    innerSize: '50%',
                    data: obj3.data
                }]
            });
        },
        error: function (xhr, type, errorThrown) {
            alert(xhr.data)
        }
    })
})