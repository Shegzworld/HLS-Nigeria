document.addEventListener('DOMContentLoaded', function(){
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabPanes = document.querySelectorAll('.tab-pane');
    const likeButton = document.querySelector('.like-button');
    const commentButton = document.querySelector('.comment-button');
    const shareButton = document.querySelector('.share-button');

    // likeButton.addEventListener('click', () => {
    //   // Add like functionality here
    //   console.log('Like button clicked!');
    // });

    // commentButton.addEventListener('click', () => {
    //   // Add comment functionality here
    //   console.log('Comment button clicked!');
    // });

    // shareButton.addEventListener('click', () => {
    //   // Add share functionality here
    //   console.log('Share button clicked!');
    // });

    tabButtons.forEach((button) => {
      button.addEventListener('click', () => {
        const tabId = button.getAttribute('data-tab');
        const tabPane = document.querySelector(`.${tabId}`);
        console.log('clicked')

        tabButtons.forEach((btn) => btn.classList.remove('active'));
        button.classList.add('active');

        tabPanes.forEach((pane) => pane.classList.remove('active'));
        tabPane.classList.add('active');
      });
    });

    const productSlider = document.querySelector('.product-slider');
    const productCards = document.querySelectorAll('.product-card');

    let currentSlide = 0;

    function showSlide(slideIndex) {
      productCards.forEach((card, index) => {
        card.style.transform = `translateX(${(index - slideIndex) * 100}%)`;
      });
    }

    function nextSlide() {
      currentSlide = (currentSlide + 1) % productCards.length;
      showSlide(currentSlide);
    }

    function prevSlide() {
      currentSlide = (currentSlide - 1 + productCards.length) % productCards.length;
      showSlide(currentSlide);
    }


    showSlide(currentSlide);

    productSlider.addEventListener('swipeleft', nextSlide);
    productSlider.addEventListener('swiperight', prevSlide);

    // Add navigation buttons
    const navButtons = document.createElement('div');
    navButtons.innerHTML = `
      <button class="prev-button">&lt;</button>
      <button class="next-button">&gt;</button>
    `;

  productSlider.appendChild(navButtons);
})