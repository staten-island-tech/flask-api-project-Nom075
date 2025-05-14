
document.addEventListener('DOMContentLoaded', function () {
  // Enable Bootstrap tooltips
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.forEach(function (tooltipTriggerEl) {
    new bootstrap.Tooltip(tooltipTriggerEl);
  });

  // Enable search filter
  document.getElementById('searchBar').addEventListener('keyup', function () {
    const searchTerm = this.value.toLowerCase();
    const items = document.querySelectorAll('.item-card');

    items.forEach(item => {
      const name = item.getAttribute('data-name');
      item.style.display = name.includes(searchTerm) ? '' : 'none';
    });
  });

  // Highlight item if hash is present in URL
  function highlightFromHash() {
    const hash = window.location.hash;
    if (hash.startsWith("#item-")) {
      const targetCard = document.querySelector(hash);
      if (targetCard) {
        // Remove highlight from all items
        document.querySelectorAll('.item-card.highlighted').forEach(el => {
          el.classList.remove('highlighted');
        });

        // Add persistent highlight to the target card
        targetCard.classList.add('highlighted');
      }
    }
  }

  highlightFromHash();

  document.querySelectorAll('.grid a[href^="#item-"]').forEach(link => {
    link.addEventListener('click', function () {
      setTimeout(() => {
        highlightFromHash();
      }, 50); // Give time for hash change
    });
  });

  document.querySelectorAll('[data-bs-toggle="modal"]').forEach(trigger => {
    trigger.addEventListener('click', function () {
      const card = this.closest('.item-card');
      if (card && card.classList.contains('highlighted')) {
        card.classList.remove('highlighted');
      }
    });
  });
});

