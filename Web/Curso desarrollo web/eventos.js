document.addEventListener("keydown", function(event) {
  var img = document.getElementById("myImage");
  if (event.code === "Space") {
    if (img.src.match("pic_bulboff.gif")) {
      img.src = "pic_bulbon.gif";
    } else {
      img.src = "pic_bulboff.gif";
    }
  }
});
document.getElementById("onclick", function(event){
var img = document.getElementById("myImage");
  if(event.code === "click"){
    if(img.src.match("pic_buloff.gif")){
      img.src = "pic_bulbon.gif";
    }else{
      img.src = "pic_bulboff.gif"
    }
  }
});