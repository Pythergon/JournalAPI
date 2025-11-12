async function fetchJsonData(filePath) {
    try {
        const response = await fetch(filePath);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        var data = await response.json(); // Parses the JSON response into a JavaScript object
        console.log(data);
        return data;
    } catch (error) {
        console.error("Error fetching JSON:", error);
    }
}

async function initialize() {
    const js_data = await fetchJsonData('./jsondata.json');

    if (js_data) {
        const myElement = document.getElementById("text-output");
        myElement.innerHTML = `Reference: <strong>${js_data.ref}</strong>`;
        console.log(js_data.ref);
    }
}

initialize();