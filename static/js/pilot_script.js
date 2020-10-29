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
  var result = document.getElementById('carResult');
  req.onreadystatechange = function()
  {
    if(this.readyState == 4 && this.status == 200) {
      result.innerHTML = this.responseText;
    }
  }

  req.open('POST', '/carInfo', true);
  req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
  req.send();
}

function get_musInfo() {
  var req = new XMLHttpRequest();
  var title = document.getElementById('title');
  var artist = document.getElementById('artist');
  var album = document.getElementById('album');
  req.onreadystatechange = function()
  {
    if(this.readyState == 4 && this.status == 200) {
      title.innerHTML = this.responseText.split("##")[0];
      artist.innerHTML = this.responseText.split("##")[1];
      album.innerHTML = this.responseText.split("##")[2];
    }
  }

  req.open('POST', '/musInfo', true);
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

function lastTrack() {
  var req = new XMLHttpRequest();
  req.open('POST', '/lastTrack', true);
  req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
  req.send();
}

function ppTrack() {
  var req = new XMLHttpRequest();
  req.open('POST', '/ppTrack', true);
  req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
  req.send();
}

function nextTrack() {
  var req = new XMLHttpRequest();
  req.open('POST', '/nextTrack', true);
  req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
  req.send();
}

var carTimer = setInterval(get_carInfo, 60000);
var timeTimer = setInterval(get_time, 30000);
var musTimer = setInterval(get_musInfo, 1000)
var sysTimer = setInterval(get_sysInfo, 20000);













