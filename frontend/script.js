document.addEventListener('DOMContentLoaded', async () => {
  const dropdown = document.getElementById('charityDropdown');
  const button = document.getElementById('visitButton');

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
});

