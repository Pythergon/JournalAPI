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
    const fullVerseOut = document.getElementById("extra-text");

    if (js_data) {
        // console.log(js_data);
        titleOut.innerHTML = `${js_data.ref.split("/")[0].charAt(0).toUpperCase() + js_data.ref.split("/")[0].slice(1)} ${js_data.chapter}`;
        verseOut.innerHTML = `${js_data.verses[1].t}`;
        fullVerseOut.innerHTML = "";

        for (let verse of js_data.verses) {
            // console.log(`[${verse.r}]${verse.t.replace(/\*r/g, '')}`);
            fullVerseOut.innerHTML += `[${verse.r}]${verse.t.replace(/\*r/g, '')}`;
        }
    }
}

initialize();