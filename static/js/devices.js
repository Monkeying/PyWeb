/**
 * Created by buptjsjlzn on 2016/12/24.
 */
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
    var xmlhttp;
    if (window.XMLHttpRequest)
    {// code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    }
    else
    {// code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function()
    {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200)
        {
            console.log(xmlhttp.responseText);
        }
    };
    setInterval(function(){
        url = "/db/device/?";
        url += document.getElementById("SN").name + "=" + document.getElementById("SN").value;
        url += document.getElementById("tempreture").name + "=" + document.getElementById("tempreture").value;

        console.log(url);
        xmlhttp.open("GET",url,true);
        xmlhttp.send();
    },3000);
};
function shutDown(){
//if alarm off or somethingl ike that happends, trigger closeup
}