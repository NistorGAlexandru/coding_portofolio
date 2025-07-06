console.log("Merge..")

function apasa_patrat(e) {
    console.log("Un patrat a fost apasat", e)
    e.innerHTML = "X"

    var request = new XMLHttpRequest();
    request.open("GET", "http://127.0.0.1:8000/game/insertx/")
    request.onreadystatechange = function () {
       
        if (this.status == 200 && this.readyState == 4){
            console.log("ready state change")
            console.log(this.responseText)
            response =  JSON.parse(this.responseText)

            casute_x = response["x"]
            casute_0 = response["0"]

            for (let i = 0; i < patratele.length; i++) {
                const element = patratele[i];
                const id_el = element.id.substring(1)
                console.log('id_el', id_el, casute_x, casute_0)
                if (casute_x.includes(id_el) ) {
                    element.innerHTML = "X"
                }
                if (casute_0.includes(id_el) ) {
                    element.innerHTML = "0"
                }

            }


        }
    }
    request.send();
}

patratele = document.getElementsByClassName("square")


for (let i = 0; i < patratele.length; i++) {
    const element = patratele[i];
    element.onclick = function () {
        apasa_patrat(element)  
    } 
}