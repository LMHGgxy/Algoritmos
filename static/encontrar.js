const volver = document.getElementById("volver") 


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

    volver.style.display = "none"

    fetch('/dibujar_lugares')
        .then(response => response.json())
        .then(graph => {
            // Renderizar el gráfico en el contenedor con el ID 'graph'
            Plotly.newPlot('graph', graph.data, graph.layout);
        })
        .catch(error => console.error('Error:', error));
}
getElementApi()

const getBusqueda = async () => {

    volver.style.display = "flex"

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

    // Convertir la respuesta a formato JSON
    const busqueda = await response.json();
    const grafoObjeto = busqueda.grafo;
    
    console.log(grafoObjeto)
    
    Plotly.newPlot('graph', grafoObjeto.data, grafoObjeto.layout);
    console.log(grafoObjeto);
};
