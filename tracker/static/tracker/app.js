document.addEventListener("DOMContentLoaded", function () {
  /*==================== SHOW NAVBAR ====================*/
  const showMenu = (headerToggle, navbarId) => {
    const toggleBtn = document.getElementById(headerToggle),
      nav = document.getElementById(navbarId);

    // Validate that variables exist
    if (headerToggle && navbarId) {
      toggleBtn.addEventListener("click", () => {
        // We add the show-menu 
        nav.classList.toggle("show-menu");
        // change icon
        toggleBtn.classList.toggle("bx-x");
      });
    }
  };
  showMenu("header-toggle", "navbar");

  /*==================== LINK ACTIVE ====================*/
  const linkColor = document.querySelectorAll(".nav__link");

  function colorLink() {
    linkColor.forEach((l) => l.classList.remove("active"));
    this.classList.add("active");
  }

  linkColor.forEach((l) => l.addEventListener("click", colorLink));

  /*==================== SLIDES ====================*/
  var swiper = new Swiper(".mySwiper", {
    spaceBetween: 5,
    cssMode: true,
    centeredSlides: true,
    loop: true,
    autoplay: {
      delay: 7500,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });


});



function search_drama() {
	let input = document.getElementById('searchbar').value
	input=input.toLowerCase();
	let x = document.getElementsByClassName('drama');
	
	for (i = 0; i < x.length; i++) {
		if (!x[i].innerHTML.toLowerCase().includes(input)) {
			x[i].style.display="none";
		}
		else {
			x[i].style.display="block";				
		}
	}
}
