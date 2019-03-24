var flag=0;
function changeColor()
{

    var div=document.getElementById("top-div-left");
    flag = 1-flag;
    if (flag ==1){
        div.style.backgroundColor="pink";
    }
    else{
        div.style.backgroundColor="white";
    }

}
