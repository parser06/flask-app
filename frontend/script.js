document.addEventListener('DOMContentLoaded', async () => {
  const dropdown = document.getElementById('charityDropdown');
  const button = document.getElementById('visitButton');
  const donateButton = document.getElementById('donateButton');

  try {
    const response = await fetch('https://flask-app-rien.onrender.com//api/charities');
    const charities = await response.json();

    charities.forEach(charity => {
      const option = document.createElement('option');
      option.value = charity.url;
      option.textContent = charity.name;
      dropdown.appendChild(option);
    });
  } catch (err) {
    console.error('Failed to load charities:', err);
  }

  dropdown.addEventListener('change', () => {
    button.disabled = dropdown.value === "";
  });

  button.addEventListener('click', () => {
    const selectedURL = dropdown.value;
    if (selectedURL) {
      window.open(selectedURL, '_blank');
    }
  });

  donateButton.addEventListener('click', () => {
    const selectedCharity = dropdown.options[dropdown.selectedIndex].text;
    const selectedURL = dropdown.value;
  
    // Pass selected charity info via query params
    const params = new URLSearchParams({
      name: selectedCharity,
      url: selectedURL
    });
  
    window.location.href = `donate.html?${params.toString()}`;
  });


});

