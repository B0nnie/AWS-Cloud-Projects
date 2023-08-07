const counterElement = document.getElementById('counter');

fetch('https://dndyi8nh8e.execute-api.us-east-1.amazonaws.com')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log('Data successfully fetched:', data);
    // Check if the 'updated_hits' property exists in the JSON response
    if (data.hasOwnProperty('updated_hits')) {
      // Get the updated_hits value from the JSON response
      const updatedHits = data.updated_hits;

      // Update the counter element with the updated_hits value
      counterElement.textContent = updatedHits;
    } else {
      // If 'updated_hits' is not present in the JSON response, handle the error
      console.error('Invalid JSON response:', data);
      counterElement.textContent = 'Invalid response';
    }
  })
  .catch(error => {
    console.error('Error fetching data:', error);
    if (error.name === 'SyntaxError') {
      // JSON parsing error
      console.error('Error parsing JSON:', error.message);
      counterElement.textContent = 'parsing error';
    } else {
      // Network error or other general error
      console.error('Network error:', error.message);
      counterElement.textContent = 'network error';
    }
  })
  .finally(() => {
    console.log('Fetch request completed.');
  });
