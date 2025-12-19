const form = document.getElementById('add-note-form');

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const title = document.getElementById('note-title').value.trim();
      const content = document.getElementById('note-content').value.trim();

      if (!title) {
        alert('Title cannot be empty!');
        return;
      }
      
      const notes = JSON.parse(localStorage.getItem('notes') || '[]');
      notes.push({ title, content });
      localStorage.setItem('notes', JSON.stringify(notes));

      alert('Note added successfully!');
      window.location.href = 'index.html';
    });