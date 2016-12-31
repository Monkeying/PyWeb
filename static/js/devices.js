/**
 * Created by buptjsjlzn on 2016/12/24.
 */
var deviceId = -1;
function DataGenerateInterval(){
// to autoly generate data
    setInterval(function(){
        document.getElementById("tempreture").value = Math.random()%100;//something like that
        var time = new Date();
        document.getElementById("lastUpdateTime").value = time.getDate();
    },1000);
}
function sendInfoInterval()
{
    setInterval(function(){
        url = "/device/update/";
        var data = {
            deviceId:deviceId
        };

        $.ajax({
            url:url,
            type:'POST',
            data:data,
            success:function (response){
                console.log("Device Update success:" + deviceId );
                console.log(response);
            },
            error:function (err){
                alert(err.statusCode())
            }
        });
    },3000);
}
function shutDown(){
//if alarm off or somethingl ike that happends, trigger closeup
}