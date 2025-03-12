document.addEventListener('DOMContentLoaded', () => {
  const testimonialBox = document.querySelectorAll(".testimonial-box")
  const nextBtnTestimonial = document.querySelector(".testimonials .slide_left")
  const prevBtnTestimonial = document.querySelector(".testimonials .slide_right")

const hamburgerMenu = document.querySelector('.hamburger-menu');
const menuList = document.getElementById('menu-list');
const bar = document.querySelector('.bar')
console.log('yes')
const overlay = document.querySelector('.overlay');
const quizButton = document.querySelector('.quiz-button');
const hamburgerLink = document.querySelector('#menu-list li:nth-child(2) a');
const modal = document.querySelector('.modal-content');
document.body.appendChild(modal);

  

// Add event listeners to the quiz button and hamburger link
quizButton.addEventListener('click', () => {
  overlay.style.display = 'block';
  modal.style.display = 'block';
});

hamburgerLink.addEventListener('click', () => {
  overlay.style.display = 'block';
  modal.style.display = 'block';
});

// Add event listener to the overlay to close the modal
overlay.addEventListener('click', () => {
  overlay.style.display = 'none';
  modal.style.display = 'none';
});

// Add event listener to the submit button
document.getElementById('submit-quiz-code').addEventListener('click', (e) => {
  e.preventDefault();
  const quizCode = document.getElementById('quiz-code').value;
  // TO DO: Add logic to validate the quiz code
  if (quizCode !== '') {
    alert(quizCode)
    window.location.href = /quiz/;
  } else {
    alert('Please enter a valid quiz code');
  }
});

bar.addEventListener('click', (e) => {
  e.stopPropagation();
  menuList.classList.toggle('show-menu');
  overlay.classList.toggle('show-overlay');
  console.log('print')
});

document.addEventListener('click', function(e) {
  if (e.target !== bar && !menuList.contains(e.target)) {
    menuList.classList.remove('show-menu');
    overlay.classList.remove('show-overlay');
  }
});

  let currentTestimonialView = 0

  const updateTestimonialVisibility = () => {
    testimonialBox.forEach((testimonial, index) => {
      testimonial.style.left = `${(index - currentTestimonialView) *280}px`
    })
  }

  nextBtnTestimonial.addEventListener('click', () => {
    if (currentTestimonialView >= 1) {
      currentTestimonialView--
      updateTestimonialVisibility()
    } else {
      prevBtnTestimonial.style.color = 'grey'
    }
    
  })

  prevBtnTestimonial.addEventListener('click', () => {
    if (currentTestimonialView < testimonialBox.length - 1) {
      currentTestimonialView++
      updateTestimonialVisibility()
    } else {
      nextBtnTestimonial.style.color = 'grey'
    }
  })

  updateTestimonialVisibility() // Initialize product display

  const productBox = document.querySelectorAll(".product-box")
  const nextBtn = document.querySelector(".slide_left")
  const prevBtn = document.querySelector(".slide_right")
  let currentProductView = 0

  const updateFormVisibility = () => {
    productBox.forEach((product, index) => {
      product.style.left = `${(index - currentProductView) *250}px`
    })
  }

  nextBtn.addEventListener('click', () => {
    if (currentProductView >= 1) {
      currentProductView--
      updateFormVisibility()
    } else {
      prevBtn.style.color = 'grey'
    }
  })

  prevBtn.addEventListener('click', () => {
    
    if (currentProductView < productBox.length - 1) {
      currentProductView++
      updateFormVisibility()
    } else {
      nextBtn.style.color = 'grey'
    }
  })
  
  updateFormVisibility() // Initialize product display
})
