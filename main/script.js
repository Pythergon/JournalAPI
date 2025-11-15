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
    const titleOut = document.getElementById("title");
    const verseOut = document.getElementById("verse-output");

    if (js_data) {
        console.log(js_data);
        titleOut.innerHTML = `${js_data.ref.split("/")[0].charAt(0).toUpperCase() + js_data.ref.split("/")[0].slice(1)} ${js_data.chapter}`;
        verseOut.innerHTML = "verse-output";
    }
}

initialize();