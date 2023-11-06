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