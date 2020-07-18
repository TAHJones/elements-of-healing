const sm = window.matchMedia("(min-width: 576px)");
const md = window.matchMedia("(min-width: 768px)");
const backToTop = document.getElementById("backToTop");



/**
 * Function that uses matchMedia method. It toggles h2 text content if the current window width matches the CSS media query string parameter or not.
 * @param {string} pageWidth - MediaQueryList object representing the results of the specified CSS media query string.
 */
function responsiveTitle(pageWidth) {
    let title = document.getElementById("title");
    let bannerImg = document.getElementById("bannerImg");
    if(title != null) {
        if(pageWidth.matches) {
            title.textContent = "Thomas Jones BSc LCHE - Classical Homeopath";
            bannerImg.src = "/static/img/homeopathy-montage--large.png";
        } else {
            title.textContent = "Thomas Jones - Homeopath";
            bannerImg.src = "/static/img/homeopathy-montage--small.png";
        }
    } else {
        console.log("Error  element with #title id does not exist!")
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
 * function that adds or removes card content depending on whether the screen size is small <576px, medium 576-768px, or large >768px
 * function is triggered by page load or page resize and only runs if the page pathname equals "/homeopathy/"
 */
function responsiveCards() {
    if (window.location.pathname == "/homeopathy/") {
        const responsiveCards = document.getElementById("responsiveCards");
        const responsiveCardsTitle = document.getElementById("responsiveCardsTitle");
        const responsiveCardsParagraph = document.getElementById("responsiveCardsParagraph");
        if(window.innerWidth > 768) {
            responsiveCardsTitle.textContent = "Examples of the Law of Similars";
            responsiveCardsParagraph.textContent = "The examples of The Law of Similars above are highly simplistic";
            responsiveCards.innerHTML = `<div class="col-md-4 col-lg-4">
                                            <div class="card">
                                                <div class="card-body">
                                                    <img class="card-img" src="/static/img/coffee.jpg" alt="coffee beans">
                                                    <p><strong>Coffee</strong> - If you drink too much coffee it can make you feel anxious, give you a rapid heartbeat and keep you awake. A patient suffering from stress experiencing these symptoms might need <em>Coffea</em>, the homeopathic remedy made from coffee.</p>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-md-4 col-lg-4">
                                            <div class="card">
                                                <div class="card-body">
                                                    <img class="card-img" src="/static/img/onion.jpg" alt="onion">
                                                    <p><strong>Onion</strong> - <em>Allium cepa</em> is a homeopathic remedy made from onions. A person chopping onions can develop stinging watery eyes and a runny nose. This remedy is for hayfever with stinging watery eyes and a runny nose.</p>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-md-4 col-lg-4">
                                            <div class="card">
                                                <div class="card-body">
                                                    <img class="card-img" src="/static/img/bee.jpg" alt="honey bee">
                                                    <p><strong>Honey Bee</strong> - <em>Apis Mellifora</em> is the homeopathic remedy made from the honey bee. It is great for insect bites and stings where the affected area is swollen, red and hot, with burning and stinging pains. Just like a bee string!</p>
                                                </div>
                                            </div>
                                        </div>`;
        } else if(window.innerWidth < 768 && window.innerWidth >= 576) {
            responsiveCardsTitle.textContent = "Examples of the Law of Similars";
            responsiveCardsParagraph.textContent = "The examples of The Law of Similars above are highly simplistic";
            responsiveCards.innerHTML = `<div class="col-sm-5">
                                            <div class="card">
                                                <div class="card-body">
                                                    <img class="card-img" src="/static/img/coffee.jpg" alt="coffee beans">
                                                    <p><strong>Coffee</strong> - If you drink too much coffee it can make you feel anxious, give you a rapid heartbeat and keep you awake. A patient suffering from stress experiencing these symptoms might need <em>Coffea</em>, the homeopathic remedy made from coffee.</p>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-sm-5">
                                            <div class="card">
                                                <div class="card-body">
                                                    <img class="card-img" src="/static/img/onion.jpg" alt="onion">
                                                    <p><strong>Onion</strong> - <em>Allium cepa</em> is a homeopathic remedy made from onions. A person chopping onions can develop stinging watery eyes and a runny nose. This remedy is for hayfever with stinging watery eyes and a runny nose.</p>
                                                </div>
                                            </div>
                                        </div>`;
        } else if(window.innerWidth < 576 ) {
            responsiveCardsTitle.textContent = "An Example of the Law of Similars";
            responsiveCardsParagraph.textContent = "The example of The Law of Similars above is highly simplistic";
            responsiveCards.innerHTML = `<div class="col-8">
                                            <div class="card">
                                                <div class="card-body">
                                                    <img class="card-img" src="/static/img/coffee.jpg" alt="coffee beans">
                                                    <p><strong>Coffee</strong> - If you drink too much coffee it can make you feel anxious, give you a rapid heartbeat and keep you awake. A patient suffering from stress experiencing these symptoms might need <em>Coffea</em>, the homeopathic remedy made from coffee.</p>
                                                </div>
                                            </div>
                                        </div>`;        
        }
    }
}


/**
 * function for bootstrap custom form validation taken from https://www.w3schools.com/bootstrap4/bootstrap_forms.asp
 * Disable form submissions if there are invalid fields
 *  */ 
(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Get the forms we want to add validation styles to
    let forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    let validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();


// eventlisteners
sm.addListener(responsiveTitle);
sm.addListener(getCurrentYear);
window.addEventListener("scroll", scrollingButton, false);
backToTop.addEventListener("click", topFunction, false);
window.addEventListener("resize", function() {
    floatButton();
    responsiveCards();
}, false);


// function calls
document.addEventListener("DOMContentLoaded", function() {
    responsiveTitle(sm);
    floatButton();
    responsiveCards();
    getCurrentYear(sm);
}, false);
