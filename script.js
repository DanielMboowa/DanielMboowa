let count = 1;
document.body.style.backgroundColor = "black";
document.body.style.color = "white";
function changeMode(){
  if(count % 2 ===  0){document.body.style.backgroundColor = 'black';
    document.body.style.color = "white";
    count++;
  } else{
    document.body.style.backgroundColor = 'white';
    document.body.style.color = "black";
    count++;

  }
  
};