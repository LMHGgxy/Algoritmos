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