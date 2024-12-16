document.addEventListener('DOMContentLoaded', function(){
const commonDetailsTab = document.getElementById('common-details-tab');
const benefitsTab = document.getElementById('benefits-tab');
const liveReviewsTab = document.getElementById('live-reviews-tab');
const commonDetailsContent = document.getElementById('common-details-content');
const benefitsContent = document.getElementById('benefits-content');
const benefitHeaders = document.querySelectorAll('.benefit-header');
const liveReviewsContent = document.querySelector('.live-reviews');
// const clinicalStudiesSelect = document.getElementById('clinical-studies-select');
const clinicalStudiesBtns = document.querySelectorAll('.clinical-studies-btn');
const overlay = document.querySelector('.overlay');

// const clinicalStudiesContainer = document.getElementById('clinical-study-container');
const closeClinicalStudyBtn = document.getElementById('close-clinical-study-btn');


// back to gallery from product detail



// Add event listeners
commonDetailsTab.addEventListener('click', () => {
    commonDetailsContent.classList.add('active');
    benefitsContent.classList.remove('active');
    liveReviewsContent.classList.remove('active');
    commonDetailsTab.classList.add('active');
    benefitsTab.classList.remove('active');
    liveReviewsTab.classList.remove('active');
});

benefitsTab.addEventListener('click', () => {
    benefitHeaders[0].click();
    benefitsContent.classList.add('active');
    commonDetailsContent.classList.remove('active');
    liveReviewsContent.classList.remove('active');
    benefitsTab.classList.add('active');
    commonDetailsTab.classList.remove('active');
    liveReviewsTab.classList.remove('active');
});


benefitHeaders.forEach(function(header) {
    header.addEventListener('click', function() {
      const benefitContent = header.nextElementSibling;
      const clinicalStudiesContainer = benefitContent.nextElementSibling;
      // header.nextElementSibling.nextElementSibling.style.display = 'flex';

      benefitHeaders.forEach(function(otherHeader) {
        if (otherHeader !== header) {
          otherHeader.nextElementSibling.style.display = 'none';
          otherHeader.nextElementSibling.nextElementSibling.style.display = 'none'
        }
      });

      benefitContent.style.display = benefitContent.style.display === 'block' ? 'none' : 'block';
      header.nextElementSibling.nextElementSibling.style.display = header.nextElementSibling.nextElementSibling.style.display === 'flex' ? 'none' : 'flex';
    });

    clinicalStudiesBtns.forEach(function(btn) {
    btn.addEventListener('click', function() {
      const clinicalStudiesContainer = btn.nextElementSibling;
      clinicalStudiesContainer.style.display = clinicalStudiesContainer.style.display === 'block' ? 'none' : 'block';
    });
  });
})

liveReviewsTab.addEventListener('click', () => {
    liveReviewsContent.classList.add('active');
    commonDetailsContent.classList.remove('active');
    benefitsContent.classList.remove('active');
    liveReviewsTab.classList.add('active');
    commonDetailsTab.classList.remove('active');
    benefitsTab.classList.remove('active');

    document.querySelector('#audio-reviews-list').style.display = 'flex';
    document.querySelector('#audio-reviews-list').style.justifyContent = 'space-around';
    // Get all review headers
    const reviewHeaders = document.querySelectorAll('.live-reviews h2');

  // Add event listener to each review header
    reviewHeaders.forEach((header) => {
    header.addEventListener('click', () => {
      // Get the corresponding review list
      console.log(header.id)
      const reviewList = document.querySelector(`#${header.id}-list`)
      
      reviewList.classList.toggle('show');
      // Toggle the display of the review list
      if ((header.id) === 'audio-reviews' || (header.id) === 'podcast-mentions') {
        // Add touch event listeners for swiping
        // let touchStartX = 0;
        // list.addEventListener('touchstart', (e) => {
        //   touchStartX = e.touches[0].clientX;
        // });
        // list.addEventListener('touchend', (e) => {
        //   const touchEndX = e.changedTouches[0].clientX;
        //   const swipeDistance = touchEndX - touchStartX;
        //   if (swipeDistance > 50) {
        //     // Swipe right
        //     currentScroll -= itemWidth;
        //     if (currentScroll < 0) currentScroll = 0;
        //     list.scrollLeft = currentScroll;
        //   } else if (swipeDistance < -50) {
        //     // Swipe left
        //     currentScroll += itemWidth;
        //     if (currentScroll > maxScroll) currentScroll = maxScroll;
        //     list.scrollLeft = currentScroll;
        //   }
        // });
        reviewList.style.justifyContent = 'space-around';
        reviewList.style.display = reviewList.classList.contains('show') ? 'flex' : 'none';
      }
      else
        reviewList.style.display = reviewList.classList.contains('show') ? 'block' : 'none';

      // Hide other review lists
      reviewHeaders.forEach((otherHeader) => {
        if (otherHeader !== header) {
          const otherReviewList = document.querySelector(`#${otherHeader.id}-list`);
          otherReviewList.classList.remove('show');
          otherReviewList.style.display = 'none'; 
        }
      });
    });
  });
});

clinicalStudiesBtns.forEach((btn) => {
btn.addEventListener('click', () => {
const benefitContent = btn.previousElementSibling;
const benefitSelect = btn.nextElementSibling;
const fileDisplay = benefitSelect.nextElementSibling;

benefitContent.style.display = 'none';
benefitSelect.style.display = 'block';

benefitSelect.addEventListener('change', () => {
  const selectedFile = benefitSelect.value;
  fileDisplay.style.display = 'block';
  fileDisplay.querySelector('iframe').src = selectedFile;
  overlay.style.display = 'block'; // Show overlay



  // Add event listener to close button
  fileDisplay.querySelector('.close-btn').addEventListener('click', () => {
    fileDisplay.style.display = 'none';
    overlay.style.display = 'none'; // Hide overlay
  });
});

});
});
});
function goBack() {
        window.history.back();
    }