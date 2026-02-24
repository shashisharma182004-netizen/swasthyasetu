// app.js

// Function to search for diseases based on user input
async function searchDiseases(query) {
    const response = await fetch(`https://api.example.com/diseases?search=${query}`);
    const data = await response.json();
    return data;
}

// Function to handle the search form submission
function handleSearch(e) {
    e.preventDefault();
    const query = document.getElementById('search-input').value;
    searchDiseases(query).then(data => {
        console.log(data);
        // Update the UI with the search results
    }).catch(error => {
        console.error('Error:', error);
    });
}

// Event listener for the search form
document.getElementById('search-form').addEventListener('submit', handleSearch);