        function ajaxSend(urlWanted) {
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
        }/**
 * Created by buptjsjlzn on 2016/12/24.
 */
