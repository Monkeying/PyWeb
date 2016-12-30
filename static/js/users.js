/**
* Created by buptjsjlzn on 2016/12/24.
*/
var userId = null;
var devicesArray = new Array();//each element is information of a device in json

function xmlHttpSend(urlWanted) {
    var xmlhttp;
    if (window.XMLHttpRequest) {// code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    }
    else {// code for IE6, IE5
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    var time = new Date();
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            time = new Date();
            document.getElementById("myDiv").innerHTML = time.getSeconds() + xmlhttp.response;
            console.log(time.getSeconds());
        }
    };
    urlWanted = "/db/search/?" + document.getElementById("input").value;
    console.log(urlWanted);
    xmlhttp.open("GET", urlWanted, true);
    xmlhttp.send();
}
function ajaxGET(urlWanted,header,dataJSON){
    console.log("enter ajaxGET");
    console.log("dataJson:" + JSON.stringify(dataJSON));
    if ( !isJson(dataJSON)){
        console.log("not a json");
        return false;
    }
    $.ajax({
        url:urlWanted,
        xhrFields:{
            withCredentials: true
        },
        beforesend:function (){
            console.log("wiating to send");
        },
        Method:"GET",
        data:JSON.stringify(dataJSON),
        header:header,
        success:function (response){
            console.log("isJSON:" + isJson(response));
            console.log(response);
            return response;
        },
        error:function (msg,status){
            console.log("message:"+JSON.stringify(msg));
            console.log("status:"+status);
            return false;
        },
        statusCode:{
            404:function (msg){
                console.log("page not found " + msg);
            }
        }
    }).done(function (data){
        console.log("done ajaxGET");
        console.log(data);
    });
}
function ajaxPOST(urlWanted,header,dataJSON){
    console.log("enter ajaxPOST");
    console.log(header);
    if ( !isJson(dataJSON) ){
        console.log("not a json");
        return false;
    }
    $.ajax({
        url:urlWanted,
        xhrFields:{
            withCredentials: true
        },
        Method:"POST",
        data:JSON.stringify(dataJSON),
        header:header,
        success:function (response){
            console.log("isJSON:" + isJson(response));
            console.log(response);
            return response;
        },
        error:function (msg,status){
            console.log("message:"+msg);
            console.log("status:"+status);
            return false;
        },
        statusCode:{
            404:function (msg){
                console.log("page not found " + msg);
            }
        }
    }).done(function (data){
        console.log("done ajaxPOST");
        console.log(data);
    });
}
function isJson(obj){
    var isjson = typeof(obj) == "object" && Object.prototype.toString.call(obj).toLowerCase() == "[object object]" && !obj.length;
    return isjson;  //boolaen
}
function Devadd2List(data){
    var tr = "<tr><td>" +  data.SN + "</td><td>" + data.Name + "</td><td>" + data.lastUpdate;
    tr += "</td><td>" + data.delete + "</td><td><input type='checkbox'/></td></tr>";

    if (data.length != 0){
        $(data).appendTo("devTableTbody");
    }
}
function Login() {
    //var userLoginInfo = document.getElementById("userName").value + ":" + document.getElementById("userPassword").value;
    var urlWanted = "/user/";
    var dataJson = {
        operation:"userLogin",
        userName:document.getElementById("userName").value,
        userPassword:document.getElementById("userPassword").value
    };
    var response =  JSON.parse( ajaxPOST(urlWanted,"{}",dataJson) );
    if (response["result"] == true) {
        userId = response["userId"];
        keepUpdate();
    }
    else{
        console.log("validation failed");
        return false;
    }
}
function SignUp(){
    var urlWanted = "/user/auth";
    var dataJson = {
        operation:"userSignUp",
        userName:document.getElementById("userName").value,
        userPassword:document.getElementById("userPassword").value
    };
    var response =  JSON.parse( ajaxPOST(urlWanted,"{}",dataJson) );
    if (response["result"] == true){
        userId = response["userId"];
        keepUpdate();
    }
    else{
        console.log("validation failed");
        return false;
    }
}
function Logout(){
    ajaxGet("/");
}
function keepUpdate(){
    console.log("enter keepUpdate");
    var urlWanted = "/user/";
    $.ajax({
        url:urlWanted,
        xhrFields:{
            withCredentials: true
        },
        data:{
            userId:userId
        },
        Method:"GET",
        success:function (response){
            console.log("isJSON:" + isJson(response));
            console.log(response);
            listUpdate(response);//response is ought to be a list of infomation in json about one by one device{'list':[{'deviceId':1,'SN':12},{'deviceId':2,'SN':13}]}
        },
        error:function (msg,status){
            console.log("message:"+msg);
            console.log("status:"+status);
        },
        statusCode:{
            404:function (msg){
                console.log("page not found " + msg);
            }
        }
    }).done(function (data){
        console.log("done keepUpdate");
        console.log(data);
        keepUpdate(urlWanted);
    });
}
function addUser(){
    var dataJSON = {
        operation:'userSignUp',
        userName:'Alex',
        userPassword:'password'
    };
    console.log(JSON.stringify(dataJSON));
    var urlWanted = "/db/user/";
    ajaxPOST(urlWanted,"{'fuck':asd}",dataJSON);
}
function addDev(){
    var dataJSON = {
        operation:'deviceSignUp',
        deviceName:document.getElementById("deviceName").val,
        SN:document.getElementById("SN").val,

    };
    console.log(JSON.stringify(dataJSON));
    var urlWanted = "/db/user/";
    ajaxPOST(urlWanted,"{'fuck':asd}",dataJSON);
}
function delDev(){
    var dataJson = {
        operation:"delDev"
    }
}
function listUpdate(response){//response is ought to be a list of infomation in json about one by one device{'list':[{'deviceId':1,'SN':12},{'deviceId':2,'SN':13}]}
    var dataJson = JSON.parse(response);
    var list = dataJson["list"]
    for (deviceJson in list){
        for (key in deviceJson){
            document.getElementById("deviceId"+deviceJson["deviceId"]+key).val = devicejson[key];//if doesnot exit,new one and append to html
        }
    }
}