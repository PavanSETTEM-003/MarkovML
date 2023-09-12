function postData() {
    const form = document.querySelector('#myForm');
    const formData = new FormData(form);

    // sending data to the localhosted python api
    fetch('http://127.0.0.1:5000/trigger_model', {
        method: 'POST',
        body: formData
    })

    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// function postData() {
//     const form = document.querySelector('#myForm');
//     const formData = new FormData(form);

//     // sending data to the localhosted python api
//     fetch('http://127.0.0.1:5000/home', {
//         method: 'POST',
//         body: formData
//     })

//     .then(response => {
//         if (response.ok) {
//             return response.json();
//         } else {
//             throw new Error('Network response was not ok');
//         }
//     })
//     .then(data => {
//         console.log(data); // Log the response from the API
//         if (data && data.success) {
//             document.querySelector('.result').textContent = "Experiment initiated";
//         } else {
//             document.querySelector('.result').textContent = "Failed";
//         }
//     })
//     .catch(error => {
//         console.error('Error:', error);
//         document.querySelector('.result').textContent = "Failed"; // Handle errors by displaying "Failed"
//     });
    
// }



var Epochs_slider = document.getElementById("Epochs_input");
var Epochs_slider_output = document.getElementById("Epochs_slider");
Epochs_slider_output.innerHTML = Epochs_slider.value; // Display the default slider value
Epochs_slider.oninput = function() {
    Epochs_slider_output.innerHTML = this.value;
}

var Batch_size_slider = document.getElementById("Batch_size_input");
var Batch_size_slider_output = document.getElementById("Batch_size_slider");
Batch_size_slider_output.innerHTML = Batch_size_slider.value; // Display the default slider value
Batch_size_slider.oninput = function() {
    Batch_size_slider_output.innerHTML = this.value;
}


