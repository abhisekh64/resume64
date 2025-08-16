const sections = document.querySelectorAll('.section');

sections.forEach(section => {
    section.addEventListener('dragstart', dragStart);
    section.addEventListener('dragover', dragOver);
    section.addEventListener('drop', drop);
});

function dragStart(e) {
    e.dataTransfer.setData('text/plain', e.target.outerHTML);
    e.dataTransfer.effectAllowed = 'move';
    e.target.classList.add('dragging'); // Optional: Add a class for styling while dragging
}

function dragOver(e) {
    e.preventDefault(); // Prevent default to allow drop
    e.dataTransfer.dropEffect = 'move';
}

function drop(e) {
    e.preventDefault();
    const html = e.dataTransfer.getData('text/plain');
    const dropTarget = e.target.closest('.section');
    if (dropTarget && dropTarget !== this) {
        dropTarget.insertAdjacentHTML('beforebegin', html); // Insert the dragged section before the drop target
        this.remove(); // Remove the dragged section from the old position
    }
}
