   // Pobieramy index notatki z query param
    const urlParams = new URLSearchParams(window.location.search);
    const index = urlParams.get('index');

    const notes = JSON.parse(localStorage.getItem('notes') || '[]');

    const titleEl = document.getElementById('note-title');
    const contentEl = document.getElementById('note-content');
    const editBtn = document.getElementById('edit-note-btn');
    const deleteBtn = document.getElementById('delete-note-btn');

    // Wyświetlamy notatkę
    if (index !== null && notes[index]) {
      titleEl.textContent = notes[index].title;
      contentEl.textContent = notes[index].content;
    } else {
      alert('Note not found!');
      window.location.href = 'index.html';
    }

    // Edytuj notatkę
    editBtn.addEventListener('click', () => {
      window.location.href = `html/editnote.html?index=${index}`;
    });

    // Usuń notatkę
    deleteBtn.addEventListener('click', () => {
      if (confirm('Are you sure you want to delete this note?')) {
        notes.splice(index, 1);
        localStorage.setItem('notes', JSON.stringify(notes));
        alert('Note deleted!');
        window.location.href = 'index.html';
      }
    });