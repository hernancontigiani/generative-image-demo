const boton = document.querySelector("#generate")

boton.onclick = async () => {
    const caption = document.querySelector("#caption").value;
    const data = {
        text: caption,
    }
    const url = `/api/v1.0/predict`

    const resp = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    if(resp.ok) {
        const data = await resp.json();
        console.log(data);
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