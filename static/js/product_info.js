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
const reviewHeaders = document.querySelectorAll('.live-reviews h2');

// const clinicalStudiesContainer = document.getElementById('clinical-study-container');
const closeClinicalStudyBtn = document.getElementById('close-clinical-study-btn');


// back to gallery from product detail



// Add event listeners
commonDetailsTab.addEventListener('click', () => {
    commonDetailsTab.classList.add('active');
    commonDetailsContent.classList.add('active');
    benefitsContent.classList.remove('active');
    liveReviewsContent.classList.remove('active');
    benefitsTab.classList.remove('active');
    liveReviewsTab.classList.remove('active');
});

benefitsTab.addEventListener('click', () => {
    benefitHeaders[0].click();
    benefitsTab.classList.add('active');
    benefitsContent.classList.add('active');
    commonDetailsContent.classList.remove('active');
    liveReviewsContent.classList.remove('active');
    commonDetailsTab.classList.remove('active');
    liveReviewsTab.classList.remove('active');
    // Close previously opened contents
    benefitHeaders.forEach((header) => {
      const benefitContent = header.nextElementSibling;
      benefitContent.style.display = 'none';
    });

    // Make the first benefit header display its content by default
    const firstBenefitHeader = benefitHeaders[0];
    const firstBenefitContent = firstBenefitHeader.nextElementSibling;
    firstBenefitContent.style.display = 'block';
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
    reviewHeaders.forEach((header) => {
      const reviewList = document.querySelector(`#${header.id}-list`);
      reviewList.style.display = 'none';
    })
    document.querySelector('#audio-reviews-list').style.display = 'flex';
    document.querySelector('#audio-reviews-list').style.justifyContent = 'space-around';
})
    
// Get all review headers
  reviewHeaders.forEach((header) => {
    header.addEventListener('click', () => {
      // Close other review lists
      reviewHeaders.forEach((otherHeader) => {
        if (otherHeader !== header) {
          const otherReviewList = document.querySelector(`#${otherHeader.id}-list`);
          otherReviewList.style.display = 'none';
        }
      });
    
    // Get the corresponding review list
    const reviewList = document.querySelector(`#${header.id}-list`);
    if ((header.id) === 'audio-reviews' || (header.id) === 'podcast-mentions') {
      reviewList.style.display = 'flex';
      reviewList.style.justifyContent = 'space-between';
    } else {
      reviewList.style.display = 'block';
    }
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