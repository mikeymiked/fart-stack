let get_people = () => {
    fetch('/proof', {method: 'GET'})
        .then(response => response.json())
        .then(data => callback(data))
        .catch(error => console.log(error));
};
let callback = (data) => {
    console.log(data);
    document.getElementById('root').innerHTML
        = ` <p>First Name: ${data.firstname}</p>
            <p>Last Name: ${data.lastname}</p>`
};

get_people();
