fetch("http://51.21.222.225:5000/student-details")
    .then(res => res.json())
    .then(data => {
        document.getElementById("name").innerText = "Name: " + data.name;
        document.getElementById("roll").innerText = "Roll: " + data.roll_number;
        document.getElementById("reg").innerText = "Register: " + data.register_number;
    });