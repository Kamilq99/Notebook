    // Pobieramy index notatki z query param
    const urlParams = new URLSearchParams(window.location.search);
    const index = urlParams.get('index');

    const notes = JSON.parse(localStorage.getItem('notes') || '[]');

    const titleInput = document.getElementById('note-title');
    const contentInput = document.getElementById('note-content');
    const form = document.getElementById('edit-note-form');

    // Wypełniamy formularz istniejącą notatką
    if (index !== null && notes[index]) {
      titleInput.value = notes[index].title;
      contentInput.value = notes[index].content;
    } else {
      alert('Note not found!');
      window.location.href = 'index.html';
    }

    // Zapis zmian
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const title = titleInput.value.trim();
      const content = contentInput.value.trim();

      if (!title) {
        alert('Title cannot be empty!');
        return;
      }

      notes[index] = { title, content };
      localStorage.setItem('notes', JSON.stringify(notes));

      alert('Note updated successfully!');
      window.location.href = 'index.html';
    });