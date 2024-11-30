document.addEventListener('DOMContentLoaded', function(){
const commonDetailsTab = document.getElementById('common-details-tab');
const benefitsTab = document.getElementById('benefits-tab');
const liveReviewsTab = document.getElementById('live-reviews-tab');
const commonDetailsContent = document.getElementById('common-details-content');
const benefitsContent = document.getElementById('benefits-content');
const liveReviewsContent = document.getElementById('live-reviews-content');
const clinicalStudiesSelect = document.getElementById('clinical-studies-select');
const clinicalStudyContainer = document.getElementById('clinical-study-container');
const closeClinicalStudyBtn = document.getElementById('close-clinical-study-btn');


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
    benefitsContent.classList.add('active');
    commonDetailsContent.classList.remove('active');
    liveReviewsContent.classList.remove('active');
    benefitsTab.classList.add('active');
    commonDetailsTab.classList.remove('active');
    liveReviewsTab.classList.remove('active');
});

liveReviewsTab.addEventListener('click', () => {
    liveReviewsContent.classList.add('active');
    commonDetailsContent.classList.remove('active');
    benefitsContent.classList.remove('active');
    liveReviewsTab.classList.add('active');
    commonDetailsTab.classList.remove('active');
    benefitsTab.classList.remove('active');
});

clinicalStudiesSelect.addEventListener('change', () => {
    clinicalStudyContainer.classList.add('active');
    document.getElementById('product-detail-page').style.display = 'none';
});

closeClinicalStudyBtn.addEventListener('click', () => {
    clinicalStudyContainer.classList.remove('active');
    document.getElementById('product-detail-page').style.display = 'block';
});
})
