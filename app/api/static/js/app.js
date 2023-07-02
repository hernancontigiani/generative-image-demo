

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

    const params = {
        caption: caption,
    };
    const query = Object.keys(params)
                    .map(k => encodeURIComponent(k) + '=' + encodeURIComponent(params[k]))
                    .join('&');
    
    const url = "/api/v1.0/predict";
    const resp = await fetch(url + "?" + query);
    if(resp.ok) {
        const data = await resp.blob();
        const imagenURL = URL.createObjectURL(data);
        imageOutput.src = imagenURL;
    } else {
        // Request fail
        // Clean image
        imageOutput.src = "";
        // Output error message
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