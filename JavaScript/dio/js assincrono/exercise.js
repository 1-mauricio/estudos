const BASE_URL = "https://thatcopy.pw/catpi/rest/";

const getCats = async () => {
    try {

        const data = await fetch(BASE_URL);
        const json = await data.json();
    } catch (e) {
        console.log(e.message)
    }
        
    return json.webpurl
};
