let popupBlock = document.querySelector(".popupBlock");
let on = false;
let popupImg = document.querySelector(".popupimage")

function showPopup(block){
    let blockPicture = block.src;
    popupImg.src = blockPicture;
    popupImg.style.maxWidth = "100%";
    popupImg.style.maxHeigth = "100%";
    on = !on;
    if (on){
        popupBlock.style.cssText = "display:block;";
    } else {
        popupBlock.style.cssText = "display:none;";
    }
    
}


function closePopup(){
    on = false
    popupBlock.style.cssText = "display:none;"
}