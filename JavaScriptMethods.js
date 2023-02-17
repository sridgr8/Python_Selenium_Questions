function btnEnable(){
    document.getElementById("btnMain").disabled = false;
    var htmlContext="";
    document.getElementById("getResult").innerHTML = htmlContext;
}

function btnDisable(){
    document.getElementById("btnMain").disabled = true;
    var htmlContext="";
    document.getElementById("getResult").innerHTML = htmlContext;
}

function btnMainClicked(){
    var htmlContext="<p>Main Button was Clicked.</p>";
    alert("I am an alert box!");
    document.getElementById("getResult").innerHTML = htmlContext;
}