const sm = window.matchMedia("(min-width: 576px)");
const md = window.matchMedia("(min-width: 768px)");
const backToTop = document.getElementById("backToTop");
const searchFormButton = document.getElementById("searchFormButton");
const closeToastBg = document.querySelector(".close");


/**
 * Function that uses matchMedia method. It toggles h2 text content if the current window width matches the CSS media query string parameter or not.
 * @param {string} pageWidth - MediaQueryList object representing the results of the specified CSS media query string.
 */
function responsiveTitle(pageWidth) {
    let title = document.getElementById("title");
    if(title != null) {
        if(pageWidth.matches) {
            title.textContent = "Thomas Jones BSc LCHE - Classical Homeopath";
        } else {
            title.textContent = "Thomas Jones - Homeopath";
        }
    }
}


/**
 * Function that uses js date method to get current year and adds it to copyright statement then inserts them into page footer. Uses matchMedia query as parameter to make copyright statement responsve
* @param {string} pageWidth - - MediaQueryList object representing the results of the specified CSS media query string.
*/
function getCurrentYear(pageWidth) {
    const copyRight = document.getElementById("copyRight");
    let copyRightText;
    let currentTime = new Date();
    let year = currentTime.getFullYear();
    if(pageWidth.matches) {
        copyRightText = "2011 - " + year + " © Thomas Jones - All Rights Reserved";
    } else {
        copyRightText = "2011 - " + year + " © Thomas Jones";
    }
    copyRight.innerHTML = copyRightText;
}


/**
 *  CREDIT: code for scrolling button taken from
 *  https://www.w3schools.com/howto/howto_js_scroll_to_top.asp 
 * makes floating button visible once user starts scrolling.
 */
function scrollingButton() {
    if(document.body.scrollTop > 40 || document.documentElement.scrollTop > 40) {
        backToTop.classList.add("active");
    } else {
        backToTop.classList.remove("active");
    }
}


/**
 * topFunction function scrolls back to the top of the page
 */
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}


/**
 * floatButton function fixes floating button in place on screens larger than 1200px
 * It also unfixes floating button on screens smaller than 1200px
 */
function floatButton() {
    if(window.innerWidth < 576) {
        backToTop.classList.replace("btn-float", "btn-fixed");
        backToTop.classList.add("active");
    } else {
        backToTop.classList.replace("btn-fixed", "btn-float");
    }
}


/**
 * function toggles search form by adding/removing show-search-form class on screens larger than 576px
 * function is triggered when  searchFormButton is clicked
 */
function toggleSearchForm() {
    if(window.innerWidth >= 576) {
        let searchForm = document.getElementById("searchForm");
        searchForm.classList.toggle("show-search-form");
    }
}


/**
 * function reveals search form by removing hide-search-form on screens smaller than 576px
 * function hides search form by adding hide-search-form on screens larger than 576px
 * function is triggered by window resize event
 */
function showSearchForm() {
    let searchForm = document.getElementById("searchForm");
    if(window.innerWidth < 576) {
        searchForm.classList.remove("hide-search-form");
        searchForm.classList.remove("show-search-form");
    } else {
        searchForm.classList.add("hide-search-form");
    }
}


// jquery scripts for basket & product_detail pages
$(document).ready(function(){
    /**
     *  Disable plus/minus quantity buttons outside 1-99 range
     */
    function handleEnableDisable(itemId) {
        var currentValue = parseInt($(`#id_qty_${itemId}`).val());
        var minusDisabled = currentValue < 2;
        var plusDisabled = currentValue > 98;
        $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
    }


    /**
     * Ensure proper enabling/disabling of all inputs on page load
     */
    var allQtyInputs = $('.qty_input');
    for(var i = 0; i < allQtyInputs.length; i++){
        var itemId = $(allQtyInputs[i]).data('item_id');
        handleEnableDisable(itemId);
    }


    /**
     * Check enable/disable every time the input is changed
     */
    $('.qty_input').change(function() {
        var itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });


    /**
    * Function that increments form input value when quantity plus button is clicked.
    */
    $('.increment-qty').click(function(e) {
       e.preventDefault();
       var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
       var currentValue = parseInt($(closestInput).val());
       $(closestInput).val(currentValue + 1);
       var itemId = $(this).data('item_id');
       handleEnableDisable(itemId);
    });


    /**
    * Function that decrements form input value when quantity minus button is clicked.
    */
    $('.decrement-qty').click(function(e) {
       e.preventDefault();
       var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
       var currentValue = parseInt($(closestInput).val());
       $(closestInput).val(currentValue - 1);
       var itemId = $(this).data('item_id');
       handleEnableDisable(itemId);
    });


    /**
     * jquery to intialise bootstrap toasts
     */
    $('.toast').toast('show');


    /**
     * Function hides custom toast background when toast close button is clicked
     */
    closeToastBg.addEventListener("click", function(){
        const toastContainerBg = document.querySelector(".toast-container-bg");
        toastContainerBg.style.display = "none";
    }, false);
});


// eventlisteners
sm.addListener(responsiveTitle);
sm.addListener(getCurrentYear);
window.addEventListener("scroll", scrollingButton, false);
backToTop.addEventListener("click", topFunction, false);
searchFormButton.addEventListener("click", toggleSearchForm, false);
window.addEventListener("resize", function() {
    responsiveTitle(sm);
    floatButton();
    responsiveCards();
    showSearchForm();
}, false);


// function calls
document.addEventListener("DOMContentLoaded", function() {
    responsiveTitle(sm);
    floatButton();
    responsiveCards();
    showSearchForm();
    getCurrentYear(sm);
}, false);
