/**
 * Created by buptjsjlzn on 2016/12/30.
 */
var userId = -1;
var Socket;
function getWebSocket(userId){
    if ("WebSocket" in window) {
        console.log("yes");
        Socket = new WebSocket("ws://127.0.0.1:8000/");
        console.log("yesyes");
        console.log("readystate:"+Socket.readyState);
        Socket.onerror = function (){
            console.log("Socket error: " + Socket.readyState);
        };
        Socket.onopen = function (){
            console.log("Socket has been connected.");
            Socket.send("hello");
            return true;
        };
        Socket.onmessage = function (response){
            console.log("receiveing");
            console.log(response);
        }
    }
    else{
        alert("You browser does not support websocket, please switch to Chrom,Firefox,Safari, Mozilla or Opera");
        return false;
    }
}
function getUserIdByPath(){
    userId = document.URL.split("?")[1];
    getWebSocket(userId);
}

