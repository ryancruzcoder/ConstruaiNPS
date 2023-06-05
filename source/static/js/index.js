function load() {
    var container = document.getElementsByClassName("container")[0];
    var loader = document.getElementsByClassName("loader")[0]; 
    var img = document.getElementsByClassName("construai")[0];

   container.style.display = "none";
   loader.style.display = "block";
   img.style.top = "33vh";

}

function close_window() {
    window.close();
}