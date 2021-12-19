const searchQueryURL = 'https://api.github.com/repos/merlin';

window.addEventListener('DOMContentLoaded', function(e) {
  return fetch(searchQueryURL)
  .then(result => result.json())
  .then(response => console.log(response))
  .catch(err => console.log(err))
})


