// post-detail.js
document.addEventListener('DOMContentLoaded', function() {
    const commentButtons = document.querySelectorAll('.comment-btn');
    commentButtons.forEach(function(button) {
      button.addEventListener('click', function() {
        const commentForm = this.nextElementSibling;
        if (commentForm.style.display === 'none') {
          commentForm.style.display = 'block';
        } else {
          commentForm.style.display = 'none';
        }
      });
    });
  });