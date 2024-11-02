document.addEventListener('DOMContentLoaded', () => {
    const quizClassDropdowns = document.querySelectorAll('.quizClass_dropdown');

    quizClassDropdowns.forEach(quizClassDropdown => {
        const quizClass = quizClassDropdown.querySelector('.quizClass');
        const dropdown = quizClassDropdown.querySelector('.dropdown');
        
        // Opening and closing dropdowns
        quizClass.addEventListener('click', () => {
            const isOpen = dropdown.style.height !== '0px' && dropdown.style.height !== '';
            
            // Close all dropdowns
            document.querySelectorAll('.dropdown').forEach(dd => {
                dd.style.height = '0';
                dd.style.padding = '0';
            });
            
            // open specific dropdowns
            if (!isOpen) {
                dropdown.style.height = dropdown.scrollHeight + 120 +'px';
                dropdown.style.minheight = dropdown.scrollHeight + 80 +'px';
                dropdown.style.borderTopLeftRadius = '0';
                dropdown.style.borderTopRightRadius = '0';
                dropdown.previousElementSibling.style.borderBottomLeftRadius = '0';
                dropdown.previousElementSibling.style.borderBottomRightRadius = '0';
                console.log(dropdown.scrollHeight)
                console.log(dropdown.style.height)
                dropdown.style.paddingBottom = '0px';
            } else {
                dropdown.style.height = '0';
                dropdown.style.padding = '0';
                dropdown.previousElementSibling.style.borderRadius= '5px';
            }
        });
    });

    // script for basic data quiz
    const takeQuizBasics = document.querySelectorAll('.dropdown button');
    const quizHeader = document.querySelector('.quiz_header');
    
    const nextButtons = document.querySelectorAll('.next');
    const backButtons = document.querySelectorAll('.back');
    const mainQuizContainer = document.querySelector('.container')

    const quizDisplayScreen = document.querySelector('.quiz_display_screen');
    const displayScreens = document.querySelectorAll('.display_screen');
    const basicsDisplayScreen = document.querySelector('#basics_display_screen');
    const lifestyleDisplayScreen = document.querySelector('#lifestyle_display_screen');
    const healthConditionDisplayScreen = document.querySelector('#health_condition_display_screen');
    const preferenceDisplayScreen = document.querySelector('#preference_display_screen');
    
    
    takeQuizBasics.forEach(takeQuizButton =>{
        displayScreens.forEach(displayScreen =>{
            displayScreen.style.display = 'none';
        })
        
        takeQuizButton.addEventListener('click', ()=>{
            quizDisplayScreen.style.display = 'flex';
            mainQuizContainer.style.transform = 'translateX(-100%)';
            if (takeQuizButton.id === "basic_btn"){
                    basicsDisplayScreen.style.display = 'flex';
                    const formareas = basicsDisplayScreen.querySelectorAll('.formarea')
                    let currentForm = 0;
                    const updateFormVisibility = () => {
                    formareas.forEach((formarea, index) => {
                    formarea.style.transform = `translateX(${(index - currentForm) * 100}%)`;
                    });
                    };
                    nextButtons.forEach((button, index) => {
                    button.addEventListener('click', () => {
                        if (currentForm < formareas.length - 1) {
                            currentForm++;
                            updateFormVisibility();
                        } else {
                            const formCompleteBasic = document.querySelector('.basic_data_complete');
                            formCompleteBasic.style.transform = 'translateX(0%)';
                            quizHeader.style.display = 'none';
                        }
                    });
                    });
                    backButtons.forEach((button) => {
                        button.addEventListener('click', () => {
                            if (currentForm > 0) {
                                currentForm--;
                                updateFormVisibility();
                            }
                        });
                    });
                    updateFormVisibility();
                }
            
            if (takeQuizButton.id === "lifestyle_btn"){
                lifestyleDisplayScreen.style.display = 'flex';
                const formareas = lifestyleDisplayScreen.querySelectorAll('.formarea')
                let currentForm = 0;
                const updateFormVisibility = () => {
                formareas.forEach((formarea, index) => {
                formarea.style.transform = `translateX(${(index - currentForm) * 100}%)`;
                });
                };
                nextButtons.forEach((button, index) => {
                button.addEventListener('click', (e) => {
                    e.preventDefault()
                    if (currentForm < formareas.length - 1) {
                        currentForm++;
                        updateFormVisibility();
                    } else {
                        const formCompleteBasic = document.querySelector('.lifestyle_data_complete');
                        formCompleteBasic.style.transform = 'translateX(0%)';
                        quizHeader.style.display = 'none';
                    }
                });
                });
                backButtons.forEach((button) => {
                    button.addEventListener('click', () => {
                        if (currentForm > 0) {
                            currentForm--;
                            updateFormVisibility();
                        }
                    });
                });
                updateFormVisibility();
            }

            if (takeQuizButton.id === "health_condition_btn"){
                healthConditionDisplayScreen.style.display = 'flex';
                const formareas = healthConditionDisplayScreen.querySelectorAll('.formarea')
                let currentForm = 0;
                const updateFormVisibility = () => {
                formareas.forEach((formarea, index) => {
                formarea.style.transform = `translateX(${(index - currentForm) * 100}%)`;
                });
                };
                nextButtons.forEach((button, index) => {
                button.addEventListener('click', (e) => {
                    e.preventDefault()
                    if (currentForm < formareas.length - 1) {
                        currentForm++;
                        updateFormVisibility();
                    } else {
                        const formCompleteBasic = document.querySelector('.health_condition_data_complete');
                        formCompleteBasic.style.transform = 'translateX(0%)';
                        quizHeader.style.display = 'none';
                    }
                });
                });
                backButtons.forEach((button) => {
                    button.addEventListener('click', () => {
                        if (currentForm > 0) {
                            currentForm--;
                            updateFormVisibility();
                        }
                    });
                });
                updateFormVisibility();
            }

            if (takeQuizButton.id === "preference_btn"){
                preferenceDisplayScreen.style.display = 'flex';
                const formareas = preferenceDisplayScreen.querySelectorAll('.formarea')
                let currentForm = 0;
                const updateFormVisibility = () => {
                formareas.forEach((formarea, index) => {
                formarea.style.transform = `translateX(${(index - currentForm) * 100}%)`;
                });
                };
                nextButtons.forEach((button, index) => {
                button.addEventListener('click', (e) => {
                    e.preventDefault()
                    if (currentForm < formareas.length - 1) {
                        currentForm++;
                        updateFormVisibility();
                    } else {
                        const formCompleteBasic = document.querySelector('.preference_data_complete');
                        formCompleteBasic.style.transform = 'translateX(0%)';
                        quizHeader.style.display = 'none';
                    }
                });
                });
                backButtons.forEach((button) => {
                    button.addEventListener('click', () => {
                        if (currentForm > 0) {
                            currentForm--;
                            updateFormVisibility();
                        }
                    });
                });
                updateFormVisibility();
            }
        
        })
    })
})

