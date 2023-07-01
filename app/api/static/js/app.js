

const boton = document.querySelector("#generate")
const imageOutput = document.getElementById("imageOutput");

boton.onclick = async () => {
    // Clean image
    imageOutput.src = "";
    
    const caption = document.querySelector("#caption").value;
    if(caption == "") {   
        alert("Please describe what iamge you would like to generate");
        return;
    }

    // Loading image...
    imageOutput.src = "/static/images/loading.jpg";
    
    const url = `/api/v1.0/predict/${caption}`;
    const resp = await fetch(url);
    if(resp.ok) {
        const data = await resp.blob();
        const imagenURL = URL.createObjectURL(data);
        imageOutput.src = imagenURL;
    } else {
        // Request fail
        const data = await resp.json();
        alert(data["detail"]);
    }
}

document.querySelector("#caption").onkeypress = (e) => {
    // if user press enter, trigger button click
    if (e.key === "Enter") {
        e.preventDefault();
        document.querySelector("#generate").click();
      }   
};