function submitForm(){
    var start_date = document.getElementById("start-date").value;
    var end_date = document.getElementById("end-date").value;
    var checkbox_covid = document.getElementById('covid');
    var checkbox_war = document.getElementById('war');
    var event;

    if (checkbox_covid.checked){
        if(checkbox_war.checked){
            event = 'Both';
        }
        else{
            event = "Covid 19 Pandemic"
        }
    }
    else if (checkbox_war.checked){
        event="Ukraine-Russia War";
    }
    else{
        event="None"
    }
    
    console.log(event)

    var formData = {
        'start-date': start_date,
        'end-date': end_date,
        'event': event
    };

    sendToFlask(formData)

}


function sendToFlask(data){ 
    fetch('/predictdata', {
        method: 'POST',
        headers:{
            'content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })

    .then (response => {
        if (response.ok){
            console.log('vinit')
            return response.json();
            
        }
        throw new Error('Network response was not ok.')
    })
    .then(responseData => {
        console.log('Response from Flask:', responseData)

        var plot_img_base64 = responseData.plot_img_base64;
        var img = new Image();

        img.src = 'data:image/png;base64,'+ plot_img_base64;
        
        var chartDiv = document.getElementById('graph');
        chartDiv.innerHTML = '';
        chartDiv.append(img);
    })
    .catch(error => {
        console.error('Error:', error)
    })
    // var plot_img_base64 = "data:image/png;base64, {{ plot_img_base64 }}";

    // var canvas = document.getElementById('chart-line');
    // var ctx = canvas.getContext('2d');

    // var img =new Image();
    // img.onload = function(){
    //     ctx.drawImage(img,0,0, canvas.height);
    // };
    // img.src = plot_img_base64;
    
    
}

// function sendToFlask2(data){ 
//     fetch('/predictdatacategorical', {
//         method: 'POST',
//         headers:{
//             'content-Type': 'application/json'
//         },
//         body: JSON.stringify(data)
//     })
//     .then (response => {
//         if (response.ok){
//             console.log('vinit')
//             return response.json();
            
//         }
//         throw new Error('Network response was not ok.')
//     })
//     .then(responseData => {
//         console.log('Response from Flask:', responseData)

//         var plot_img_base64 = responseData.plot_img_base64;
//         var img = new Image();

//         img.src = 'data:image/png;base64,'+ plot_img_base64;
        
//         var chartDiv = document.getElementById('graph');
//         chartDiv.innerHTML = '';
//         chartDiv.append(img);
//     })
//     .catch(error => {
//         console.error('Error:', error)
//     })
    // var plot_img_base64 = "data:image/png;base64, {{ plot_img_base64 }}";

    // var canvas = document.getElementById('chart-line');
    // var ctx = canvas.getContext('2d');

    // var img =new Image();
    // img.onload = function(){
    //     ctx.drawImage(img,0,0, canvas.height);
    // };
    // img.src = plot_img_base64;
    
    
// }



// const availableWords = [
//   "Category 1", "Category 2", "Category 3", "Category 4", "Category 5", "Category 6", "Category 7", "Category 8", "Category 9", "Category 10", "Eggs", "Milk", "Bread"
// ];

// const resultBox = document.getElementById(".result-box"); 
// const inputBox = document.getElementById("input-box"); 

// inputBox.onkeyup = function(){
//   let result = [];
//   let input = inputBox.value;
//   if(input.length){
//       result = availableWords.filter((keyword)=>{
//          return keyword.toLowerCase().includes(input.toLowerCase());
//       });
//       console.log(result);
//   }
//   display(result);

//   if(!result.length){
//       resultBox.innerHTML='';
//   }
// }

// function display(result){
//   const content = result.map((list)=>{
//       return "<li onclick=selectInput(this)>"+ list + "</li>";
//   });

//   resultBox.innerHTML = "<ul>"+ content.join('') + "</ul>";
// }

function toggleSearch() {
  var container = document.getElementById("searchContainer");
  container.style.display = (container.style.display === "none") ? "block" : "none";
  if (container.style.display === "block") {
      fillCategories();
  }
}

var selectedCategory = null;

function fillCategories() {
    var categories = ["Cereals and products", "Clothing", "Clothing and footwear", "Consumer Food Price Index", "Education", "Egg", "Food and beverages", "Footwear", "Fruits", "Fuel and light", "Health", "Household goods and services", "Housing", "Meat and fish", "Milk and products", "Miscellaneous", "Non-alcoholic beverages", "Oils and fats", "Pan; tobacco; and intoxicants", "Personal care and effects", "Prepared meals; snacks; sweets etc.", "Pulses and products", "Recreation and amusement", "Spices", "Sugar and confectionery", "Transport and communication", "Vegetables"];
    var categoriesList = document.getElementById("categoriesList");
    categoriesList.innerHTML = "";
  
    categories.forEach(function(category) {
        var categoryButton = document.createElement("button");
        categoryButton.textContent = category;
        categoryButton.className = "category-button"; // Add a class for styling if needed
        categoryButton.onclick = function() {
            selectedCategory = category; // Set the global variable on click
        };
        categoriesList.appendChild(categoryButton);
    });
}
  
  function sendCategoryData() {
    if (selectedCategory === null) {
        console.error('No category selected.');
        return;
    }
    var start_date = document.getElementById("start-date").value;
    var end_date = document.getElementById("end-date").value;
    
    // Use the globally selected category
    var data = {
      'category': selectedCategory,
      'start_date': start_date,
      'end_date': end_date
    };
    
    console.log(data)
    // Send the data to the Flask server
    fetch('/predictdatacategorical', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)

    })
    .then(response => {
        if (response.ok) {
            console.log('response' + response.ok)
            return response.json();
        }
        throw new Error('Network response was not ok.');
    })
    .then(data => {
        console.log('Success:', data);
        var imageSrc = 'data:image/png;base64,' + data.data.image_base64;
        console.log(imageSrc)
        var imgElement = document.createElement('img');
        imgElement.src = imageSrc;
        document.getElementById('forecastPlot').innerHTML = ''; // Clear existing content
        document.getElementById('forecastPlot').appendChild(imgElement); // Add the image element
    })    
    .catch((error) => {
        console.error('Error:', error);
    });
  }
  
  // Make sure to have your Flask server ready to handle this JSON data on '/submit_form'
  // and have 'start-date' and 'end-date' input fields on your HTML page.
  
  
function searchCategories() {
  var searchInput = document.getElementById("searchInput").value.toLowerCase(); // Convert search input to lowercase for case-insensitive matching
  var categories = ["Cereals and products", "Clothing", "Clothing and footwear", "Consumer Food Price Index", "Education", "Egg", "Food and beverages", "Footwear", "Fruits", "Fuel and light", "Health", "Household goods and services", "Housing" , "Meat and fish" , "Milk and products", "Miscellaneous", "Non-alcoholic beverages", "Oils and fats", "Pan; tobacco; and intoxicants", "Personal care and effects", "Prepared meals; snacks; sweets etc.", "Pulses and products", "Recreation and amusement", "Spices", "Sugar and confectionery", "Transport and communication", "Vegetables"];
  var suggestions = categories.filter(category => category.toLowerCase().includes(searchInput)); // Filter categories based on search input
  displaySuggestions(suggestions);
}

function displaySuggestions(suggestions) {
  var suggestionsList = document.getElementById("suggestionsList");
  suggestionsList.innerHTML = "";

  suggestions.forEach(function(suggestion) {
      var suggestionItem = document.createElement("div");
      suggestionItem.textContent = suggestion;
      suggestionsList.appendChild(suggestionItem);
  });
}

// Event listener for input in the search bar
document.getElementById("searchInput").addEventListener("input", function() {
  searchCategories();
});


// function selectInput(list){
//   inputBox.value = list.innerHTML;
//   resultBox.innerHTML='';
// }

function aboutus() {
    var mySpan = document.getElementById("mySpan");

    if (mySpan) {
        mySpan.addEventListener("click", function() {
            // Directly pass the URL rendered by Flask's url_for function
            var url = 'about';

            // Open the URL in a new tab/window
            window.open(url);
        });
    }
}

