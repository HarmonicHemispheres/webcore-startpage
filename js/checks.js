function launchTerm(cmd){

    if (cmd.value == "color"){
        var obj = document.getElementById("colpic");
        if (obj.style.display == "none"){
            obj.style.display = "block";
        } else {
            obj.style.display = "none";
        }
    }
    else if (cmd.value == "help"){
        var obj = document.getElementById("help");
        if (obj.style.display == "none"){
            obj.style.display = "block";
            document.getElementById("webterm").placeholder = "web terminal (type help again)";
        } else {
            obj.style.display = "none";
            document.getElementById("webterm").placeholder = "web terminal (type help)";
        }
    }
    else if (cmd.value == "cal"){
        var obj = document.getElementById("caleandar");
        if (obj.style.display == "none"){
            obj.style.display = "block";
        } else {
            obj.style.display = "none";
        }
    }
    cmd.value = "";
}