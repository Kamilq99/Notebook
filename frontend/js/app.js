function renderNotes(filter = '') {
    notesContainer.innerHTML = '';
    notes.forEach((note, index) => {
        if (!filter || note.title.toLowerCase().includes(filter.toLowerCase()) || note.content.toLowerCase().includes(filter.toLowerCase())) {
            const noteDiv = document.createElement('div');
            noteDiv.className = 'bg-white p-4 rounded shadow hover:shadow-lg transition';
            noteDiv.innerHTML = `
                <div class="font-bold text-lg text-gray-800">${note.title}</div>
                <div class="text-gray-700 mt-2">${note.content}</div>
                <div class="mt-4 flex space-x-2">
                    <button onclick="editNote(${index})" class="bg-yellow-400 hover:bg-yellow-500 text-white px-3 py-1 rounded">Edit</button>
                    <button onclick="deleteNote(${index})" class="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded">Delete</button>
                </div>
            `;
            notesContainer.appendChild(noteDiv);
        }
    });
}
