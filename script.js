const playlistCards = document.getElementById("playlistCards");

// Ambil data playlist
fetch('data/playlist.json')
  .then(response => response.json())
  .then(playlists => {
    playlists.forEach(p => {
      // --- Card Playlist tanpa cover image ---
      const card = document.createElement('a');
      card.href = `playlist.html?name=${encodeURIComponent(p.name)}`;
      card.classList.add('card');
      card.innerHTML = `
        <h3>${p.name}</h3>
        <p>${p.description}</p>
      `;
      playlistCards.appendChild(card);
    });
  })
  .catch(err => console.error('Gagal load playlist:', err));

// Tutup overlay kalau diklik
document.getElementById('overlay').addEventListener('click', (e) => {
  if (e.target.id === 'overlay') {
    document.getElementById('overlay').style.display = 'none';
  }
});

function hideOverlay() {
  document.getElementById('overlay').style.display = 'none';
}
