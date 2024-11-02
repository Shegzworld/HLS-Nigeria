document.addEventListener('DOMContentLoaded', function() {
    // Variable Declaration
    const benfekWrapper = document.querySelector('.benfek_wrapper')
    // Top section (top sticky bar)
    
    const topStickyBar = document.querySelector('.top_sticky_bar')
    const menuIcon = document.getElementById("menu_icon");
    const hamburger_menu = document.querySelector (".hamburger_menu")
    const menuDropdown = document.getElementById('menu_dropdown_menu');
    const closeIcon = document.getElementById('close_icon');

    const searchIcon = document.querySelector('.primary-nav .fa-search');
    const searchContainer = document.querySelector('#search_container');
    const searchForm = document.getElementById('searchForm');
    const serviceHeader = document.querySelector('.service-header');
    const services = document.querySelectorAll('.benfek-service');
    const benfekServicesContainer = document.querySelector('.benfek-services')
    const benfekServiceIconText = document.querySelectorAll('.benfek-services span')

    // Mid section(body)
    const displayBody = document.querySelector('.display_body')
    const display_contents = document.querySelectorAll('.display_content')
    

    // NT_gallery
    const NtGallery = document.querySelector('#NT-gallery')
    const menuItems = document.querySelectorAll('.menu-item');
    const Nutrient_type= document.querySelector('#Nutrient_type');
    const nutrientTypeGallery = document.querySelector('.nutrient_type_gallery');
    const nutrientGalleryContainer = document.querySelectorAll('.nutrient_gallery_container');
    const nutrient_type_glass_pack = document.querySelector('.nutrient_type_glass_pack');
    const nutrient_type_container = document.querySelector('#nutrient_type_container');
    const nutrient_gallery = document.querySelector('.nutrient_gallery');
    const nutrient_type_pack= document.querySelector('.Nutrient_type_pack');
    const NutrientTypeGlassCover = document.querySelectorAll('.Nutrient_type_glass');
    const NutrientTypeHighlightButtons = document.querySelectorAll('.label-bg');
    const selected_nutrient_screen = document.querySelector('.selected_nutrient_screen')
    const viewInfoBtns = document.querySelectorAll('.view_info_btn');
    const tooltips = document.querySelectorAll('.tooltip');
    const specifics_container = document.querySelector('#specifics_container');
    const dr_pick_container = document.querySelector('#dr_pick_container');
    
    // Nutrient Pack details
    const pic = document.querySelector(".nutrient-pack-item-pic");
    const rational = document.querySelector(".nutrient-pack-rational");
    const researchSummaryItems = document.querySelectorAll('.research_summary_intro');
    
    // Good_news section
    const Breakthroughs= document.querySelector('#Breakthroughs');
    const benfekSelectedArticles = document.querySelector('.benfek_selected_articles');
    const articleClassesContainer = document.querySelectorAll('.article_class_container');
    const articleCardsContainer = document.querySelector('#article-cards');
    const aboutYouContainer = document.querySelector('#about_you');
    
    // Podcast section
    const podcastSection = document.querySelector('.podcast-section');



    // Codes for declaring Actives and event listeners for services to display contents

    document.addEventListener('click', function(event) {
        if (menuIcon.contains(event.target)){
            menuDropdown.style.display = 'block';
        }
        
        if (!menuIcon.contains(event.target) && !menuDropdown.contains(event.target)) {
            hamburger_menu.style.display = 'none';
        }
        
        if (event.target === closeIcon) {
            hamburger_menu.style.display = hamburger_menu.style.display === 'none' ? 'block' : 'none';
        }

    });

    let isDisplayed = false
    searchIcon.addEventListener('click', ()=>{  
        if(isDisplayed)
        {
        searchContainer.style.display = 'none';
        topStickyBar.style.height = '180px';
        benfekWrapper.style.paddingTop= '180px'
        isDisplayed = false}
        else
        {   searchContainer.style.display = 'block';
            topStickyBar.style.height = '240px';
            benfekWrapper.style.paddingTop= '240px';
            isDisplayed = true}
    })
    
    NtGallery.classList.add('active')
    services.forEach(service => {
        service.addEventListener('click', () => {
            if (!service.classList.contains('active')) {
                services.forEach(service=>{
                    service.classList.remove('active')
                })
                service.classList.add('active');
            }
        });
    })

    benfekServicesContainer.addEventListener('click', function(e){
        const target = e.target;
        if (target.closest('#NT-gallery')){
            display_contents.forEach(display_content=>{
                display_content.style.display='none'
            })
            console.log('clicked')
            serviceHeader.style.display = 'block';
            topStickyBar.style.height = '250px';
            searchContainer.style.display = 'none';
            benfekServiceIconText.forEach(text=>{
            text.style.display = 'block'
            })
            let isDisplayed = false
            searchIcon.addEventListener('click', ()=>{  
                if(isDisplayed)
                {
                searchContainer.style.display = 'none';
                topStickyBar.style.height = '200px';
                benfekWrapper.style.paddingTop= '200px'
                isDisplayed = false}
                else
                {   searchContainer.style.display = 'block';
                    topStickyBar.style.height = '240px';
                    // benfekWrapper.style.paddingTop= '240px'
                    isDisplayed = true}
            })
            nutrientGalleryContainer.forEach(galleryContainer=>{
                galleryContainer.style.display='none'
            })
            menuItems.forEach(i => i.classList.remove('active'));
            this.classList.add('active');
            Nutrient_type.classList.add('active')
            nutrientTypeGallery.style.display = 'flex';
            nutrient_type_container.style.display = 'flex';
            nutrient_type_container.style.transform = 'translateX(0%)';
        }
        if (target.closest('#Its-a-News')){
            display_contents.forEach(display_content=>{
                display_content.style.display='none';
            })
            benfekSelectedArticles.style.display = 'flex';
            benfekSelectedArticles.style.transform = 'translateX(0%)';
            serviceHeader.style.display = 'none';
            searchContainer.style.display = 'none';
            let isDisplayed = false
            searchIcon.addEventListener('click', ()=>{  
                if(isDisplayed)
                {
                searchContainer.style.display = 'none';
                topStickyBar.style.height = '120px';
                benfekWrapper.style.paddingTop= '120px'
                isDisplayed = false}
                else
                {   searchContainer.style.display = 'block';
                    topStickyBar.style.height = '180px';
                    benfekWrapper.style.paddingTop= '180px';
                    isDisplayed = true}
            })
            benfekServiceIconText.forEach(text=>{
            text.style.display = 'none'
            })
            menuItems.forEach(i => i.classList.remove('active'));
            Breakthroughs.classList.add('active');
            topStickyBar.style.height = '120px';
            articleClassesContainer.forEach(articleContainer=>{
                articleContainer.style.display='none'
            })
            articleCardsContainer.style.display = 'flex';
        }
        if (target.closest('#Podcast')){
            display_contents.forEach(display_content=>{
                display_content.style.display='none'
            })
            podcastSection.style.display = 'flex';
            podcastSection.style.transform = 'translateX(0%)';
            serviceHeader.style.display = 'none';
            searchContainer.style.display = 'none';
            

            let isDisplayed = false
            searchIcon.addEventListener('click', ()=>{  
                if(isDisplayed)
                {
                searchContainer.style.display = 'none';
                topStickyBar.style.height = '146.4px';
                benfekWrapper.style.paddingTop= '146.4px';
                isDisplayed = false}
                else
                {   
                searchContainer.style.display = 'block';
                topStickyBar.style.height = '200px';
                benfekWrapper.style.paddingTop= '200px';
                isDisplayed = true}
            })
            benfekServiceIconText.forEach(text=>{
            text.style.display = 'none'
            })
            topStickyBar.style.height = '120px';
        }
        // if (target.closest('#Doctors-Note')){
        // serviceHeader.style.display = 'none';
        // searchContainer.style.display = 'none';
        // benfekServiceIconText.forEach(text=>{
        //     text.style.display = 'none'
        //     })
        // topStickyBar.style.height = 'auto'
        // benfekWrapper.style.paddingTop = '95px'
        // }
    })

    menuItems.forEach(item => {
        item.addEventListener('click', function () {
            menuItems.forEach(i => i.classList.remove('active'));
            this.classList.add('active');
            nutrientGalleryContainer.forEach(galleryContainer=>{
                    galleryContainer.style.transform = 'translateX(0%)';
                    galleryContainer.style.transform = 'translateX(100%)';
                nutrientTypeGallery.style.position = 'relative';
                })

            articleClassesContainer.forEach(articleContainer=>{
                    articleContainer.style.display='none';
                })
                
            if(item.id===('Nutrient_type'))
            {
                nutrient_type_container.style.display = 'flex';
                nutrient_type_container.style.transform = 'translateX(0%)';
                nutrient_type_container.style.transition= 'transform 0.3s';
                specifics_container.style.transition= 'transform 0.1s';
                dr_pick_container.style.transition= 'transform 0.1s';
            }
            if(item.id===('specifics')){
                specifics_container.style.display = 'flex';
                specifics_container.style.transform = 'translateX(0%)';
                specifics_container.style.transition= 'transform 0.3s';
                nutrient_type_container.style.transition= 'transform 0.1s';
                dr_pick_container.style.transition= 'transform 0.1s';
            }
            if(item.id===('doctors_pick')){
                dr_pick_container.style.display = 'flex';
                dr_pick_container.style.transform = 'translateX(0%)';
                dr_pick_container.style.transition= 'transform 0.3s';
                nutrient_type_container.style.transition= 'transform 0.1s';
                specifics_container.style.transition= 'transform 0.1s';
            }
            if(item.id===('Breakthroughs')){
                articleCardsContainer.style.display = 'flex';
            }
            if(item.id===('About_you')){
                aboutYouContainer.style.display = 'flex';
                aboutYouContainer.style.transform = 'translateX(0%)'
            }
        });
    });

    const my_nutrient_picture = document.querySelectorAll(".my_nutrient_picture")
    const nextBtnNutrient_type = document.querySelector(".Nutrient_type_pack .slide_left")
    const prevBtnNutrient_type = document.querySelector(".Nutrient_type_pack .slide_right")
    let currentNutrientPictureView = 0

    const updateNutrient_typeVisibility = () => {
        my_nutrient_picture.forEach((nutrientPic, index) => {
        nutrientPic.style.left = `${(index - currentNutrientPictureView) *180}px`
        })
    }
    nextBtnNutrient_type.addEventListener('click', () => {
        if (currentNutrientPictureView >= 1) {
        currentNutrientPictureView--
        updateNutrient_typeVisibility()
        } else {
        nextBtnNutrient_type.style.color = 'grey'
        }
    })
    prevBtnNutrient_type.addEventListener('click', () => {
        if (currentNutrientPictureView < my_nutrient_picture.length - 1) {
        currentNutrientPictureView++
        updateNutrient_typeVisibility()
        } else {
        prevBtnNutrient_type.style.color = 'grey'
        }
    })
  
    NutrientTypeGlassCover.forEach(glassCover=>{
        const revealButton = glassCover.querySelector('button');
        const glassCoverText = glassCover.querySelector('p');
        const packRating = glassCover.querySelector('.nutrient_pack_rating');
        console.log('clicked')
        supplementInfoButton = glassCover.parentElement.querySelectorAll('.view_info_btn')
            supplementInfoButton.forEach(infoButton=>{
                infoButton.style.display = 'none'
            })
            const labelBg = glassCover.previousElementSibling;
            revealButton.addEventListener('click', ()=>
            {
            packRating.style.display = 'none';
            prevBtnNutrient_type.style.display = 'block'
            nextBtnNutrient_type.style.display = 'block'
            updateNutrient_typeVisibility()
            glassCover.style.height = '0%';
            glassCover.style.border = '0px';
            glassCoverText.style.opacity = '0';
            revealButton.style.opacity = '0';
            labelBg.style.opacity = '1';
        })
    })

    NutrientTypeHighlightButtons.forEach(NutrientTypeHighlightButton => {
        NutrientTypeHighlightButton.addEventListener('click', () =>{
            topStickyBar.style.display = 'none'
            nutrientTypeGallery.style.display = 'none';
            selected_nutrient_screen.style.display = 'block'
            selected_nutrient_screen.style.transition = 'transform 1s';
            selected_nutrient_screen.style.transform = 'translateX(0%)';
            
        backToNutrientPack = selected_nutrient_screen.querySelector('.fa-arrow-left');
        backToNutrientPack.addEventListener('click', ()=>{
            selected_nutrient_screen.style.transform = 'translateX(100%)';
            selected_nutrient_screen.style.display = 'none'
            topStickyBar.style.display = 'flex'
            topStickyBar.style.transform = 'translateX(0%)';
            nutrientTypeGallery.style.transform = 'translateX(0%)';
            nutrientTypeGallery.style.display = 'flex'
            nutrientTypeGallery.style.transition = 'transform 0.3s';
            topStickyBar.style.transition = 'transform 0.3s';
            benfekWrapper.style.paddingBottom= '60px';
            })
        })
    })

    rational.addEventListener('click', () => {
    pic.style.animation = 'shuffle_up 0.5s forwards';
    rational.style.animation = 'shuffledown 0.5s forwards';
    });

    researchSummaryItems.forEach(researchSummaryItem => {
        researchSummaryItem.addEventListener('click', () => {
        const extraContent = researchSummaryItem.nextElementSibling;
        const icon = researchSummaryItem.querySelector('.toggle-text i');
        const isExpanded = extraContent.style.height !== '0px' && extraContent.style.height !== '';

        if (isExpanded) {
            // Collapse content
            extraContent.style.height = '0px';
            extraContent.style.overflow = 'hidden';
            
            icon.classList.remove('fa-minus');
            icon.classList.add('fa-plus');
        } else {
            // Expand content
            extraContent.style.height = `${extraContent.scrollHeight}px`;
            extraContent.style.borderBottom = 'solid rgba(100, 98, 98, 0.587) 0.01px';
            researchSummaryItem.style.borderBottom = 'none'
            icon.classList.remove('fa-plus');
            icon.classList.add('fa-minus');
        }
        });
    });


    // const flashers = document.querySelectorAll('.readmore_flasher');
    //     // const items=container.children;

    //     flashers.forEach(flasher =>{
    //         console.log('flash')
    //         flasher.addEventListener('click', ()=> {
    //                 flasher.previousElementSibling.classList.toggle('active');
    //                 console.log('flash')
    //             });
    //          })
        
    viewInfoBtns.forEach(btn => {
    btn.addEventListener('mouseenter', () => {
        const parentNutrientPicture = btn.closest('.my_nutrient_picture');
        const overlay = parentNutrientPicture.querySelector('.overlay');
        const shoppingCart = parentNutrientPicture.querySelector('.fa-shopping-cart')
        overlay.style.display = 'block';
         shoppingCart.style.display = 'block';
         shoppingCart.style.color = '#e8cfa2';
    });
    btn.addEventListener('mouseleave', () => {
        const parentNutrientPicture = btn.closest('.my_nutrient_picture');
        const shoppingCart = parentNutrientPicture.querySelector('.fa-shopping-cart')
        const overlay = parentNutrientPicture.querySelector('.overlay');
        shoppingCart.style.display = 'none';
        overlay.style.display = 'none';
    });
    });

    tooltips.forEach(tooltip => {
    tooltip.addEventListener('mouseenter', () => {
        const parentNutrientPicture = tooltip.closest('.my_nutrient_picture');
        const overlay = parentNutrientPicture.querySelector('.overlay');
        overlay.style.display = 'block';
    });
    tooltip.addEventListener('mouseleave', () => {
        const parentNutrientPicture = tooltip.closest('.my_nutrient_picture');
        const overlay = parentNutrientPicture.querySelector('.overlay');
        overlay.style.display = 'none';
    });
    });

    const podcastCards = document.querySelectorAll('.podcast-card');
    let currentlyPlayingAudio = null;

    podcastCards.forEach((card) => {
    const playButton = card.querySelector('.podcast-action-call span');
    const audioElement = card.querySelector('.podcast-action-call audio');
    
    playButton.audioElement = audioElement;
    
    playButton.addEventListener('click', function() {
        if (this.audioElement.paused) {
        if (currentlyPlayingAudio) {
            currentlyPlayingAudio.pause();
        }
        this.audioElement.play();
        currentlyPlayingAudio = this.audioElement;
        this.innerHTML = '<i class="fas fa-pause"></i> Pause';
        } else {
        this.audioElement.pause();
        currentlyPlayingAudio = null;
        this.innerHTML = '<i class="fas fa-play"></i> Play Now';
        }
  });
});
});






