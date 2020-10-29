function get_time() {
  var req = new XMLHttpRequest();
  var result = document.getElementById('timeResult');
  req.onreadystatechange = function()
  {
    if(this.readyState == 4 && this.status == 200) {
      result.innerHTML = this.responseText;
    }
  }

  req.open('POST', '/ctime', true);
  req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
  req.send();
}

function get_carInfo() {
  var req = new XMLHttpRequest();
  var result = document.getElementById('gas');
  var result = document.getElementById('speed');
  var result = document.getElementById('RPM');
  var result = document.getElementById('load');
  req.onreadystatechange = function()
  {
    if(this.readyState == 4 && this.status == 200) {
      gas.innerHTML = this.responseText.split("##")[0];
      speed.innerHTML = this.responseText.split("##")[1];
      RPM.innerHTML = this.responseText.split("##")[2];
      load.innerHTML = this.responseText.split("##")[3];
    }
  }
  req.open('POST', '/carInfo', true);
  req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
  req.send();
}


function get_sysInfo() {
  var req = new XMLHttpRequest();
  var result = document.getElementById('sysResult');
  req.onreadystatechange = function()
  {
    if(this.readyState == 4 && this.status == 200) {
      result.innerHTML = this.responseText;
    }
  }

  req.open('POST', '/sysInfo', true);
  req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
  req.send();
}

var carTimer = setInterval(get_carInfo, 25000);
var timeTimer = setInterval(get_time, 30000);
var sysTimer = setInterval(get_sysInfo, 20000);













