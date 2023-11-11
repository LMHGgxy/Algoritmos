const data = async () => {
    try {
        const response = await fetch("/lugares");
        const datos = await response.json();
        console.log(datos);
    } catch (error) {
        console.error("Error fetching data:", error);
    }
};
data();

const getElementApi = async () => {
    try {
        const response = await fetch("/dibujar_lugares");
        const datos = await response.json()
        console.log(datos)
        const canva = document.getElementById("routes")
        canva.innerHTML = `<img src="data:image/png;base64,${datos.code_image}" class="rutas">`
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}
getElementApi()

const getBusqueda = async () => {
    const inicio_ruta = document.getElementById("inicio").value;
    const final_ruta = document.getElementById("final").value;

    const response = await fetch("/buscar", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            inicio: inicio_ruta,
            final: final_ruta
        })
    });

    const busqueda = await response.json();

    const respuesta_html = document.getElementById("respuesta");
    respuesta_html.innerText = JSON.stringify(busqueda);
}
