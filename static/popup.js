let popupBlock = document.querySelector(".popupBlock");
let on = false;
let popupImg = document.querySelector(".popupimage")
/*
function showPopup(block){
    let blockPicture = block.src;
    popupImg.src = blockPicture;
    on = !on;
    if (on){
        popupBlock.style.cssText = "display:block;";
    } else {
        popupBlock.style.cssText = "display:none;";
    }
    
}
*/



function showPopup(block) {
    let blockPicture = block.src;
    popupImg.src = blockPicture;
    popupImg.style.maxWidth = "100%";

    var img = new Image();
    img.onload = function() {
        var width = this.width;
        var height = this.height;
        console.log("Ширина изображения: " + width + " пикселей");
        console.log("Высота изображения: " + height + " пикселей");

        if (width < height){
            popupBlock.style.width = "28%";
            popupBlock.style.top = "80px";
            popupBlock.style.right = "35%"
        } else {
            popupBlock.style.width = "50%";
            popupBlock.style.top = "100px";
        }
    };
    img.src = blockPicture;

    

    on = !on;
    if (on) {
        popupBlock.style.display = "block";
    } else {
        popupBlock.style.display = "none";
    }
}




function closePopup(){
    on = false
    popupBlock.style.cssText = "display:none;"
}