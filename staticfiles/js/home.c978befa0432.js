document.addEventListener('DOMContentLoaded', () => {
  const testimonialBox = document.querySelectorAll(".testimonial-box")
  const nextBtnTestimonial = document.querySelector(".testimonials .slide_left")
  const prevBtnTestimonial = document.querySelector(".testimonials .slide_right")
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

