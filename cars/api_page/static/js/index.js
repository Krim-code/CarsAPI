function drawList(array){
    let list = document.createElement('ul')
    array.forEach((elem)=>{
        let li = document.createElement('li')
        let ul = document.createElement('ul')
        elem.name === undefined ? li.innerHTML = elem.author_email: li.innerHTML = elem.name
        for(key in elem){
            if (key !== "id" && key !=="name" && key !== 'author_email'){
                let secondli = document.createElement('li')
                secondli.innerHTML = `${key}:${elem[key]}`
                ul.appendChild(secondli)
            }

        }

        li.appendChild(ul)
        list.appendChild(li)})
    document.body.appendChild(list)
}
addEventListener("DOMContentLoaded", async () => {
    const array = ['countries','manufacturers','cars','comments']
    for (const elem of array) {
        let heading = document.createElement('h3')
        heading.innerHTML = `${elem}`
        document.body.appendChild(heading)
        const response = await fetch(`/api/${elem}`)
        .then(data => data.json())
        .then(data => drawList(data));
    }


})


