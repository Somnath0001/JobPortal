// Add event listeners to collapsible buttons
const collapsibleButtons = document.querySelectorAll('.collapsible-button');

collapsibleButtons.forEach((button) => {
    button.addEventListener('click', () => {
        // Collapse other sections
        collapsibleButtons.forEach((otherButton) => {
            if (otherButton !== button) {
                const otherCollapsibleContent = otherButton.nextElementSibling;
                otherCollapsibleContent.style.display = 'none';
            }
        });

        // Toggle current section
        const collapsibleContent = button.nextElementSibling;
        collapsibleContent.style.display = collapsibleContent.style.display === 'block' ? 'none' : 'block';
    });
});
