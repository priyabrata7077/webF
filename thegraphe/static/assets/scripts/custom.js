(function ($, window, Typist) {


  // Dropdown Menu Fade    
  jQuery(document).ready(function () {
    $(".dropdown").hover(
      function () {
        $('.dropdown-menu', this).fadeIn("fast");
      },
      function () {
        $('.dropdown-menu', this).fadeOut("fast");
      });
  });

  /*-------active---------*/

  $(document).ready(function () {
    $(".nav-link").click(function () {
      $(".nav-link").removeClass("active");
      $(this).addClass("active");
    });
  });

  /*--------------scroll_top----------*/

  $(document).ready(function () {
    "use strict";
    var offSetTop = 100;
    var $scrollToTopButton = $('.scrollToTop');
    //Check to see if the window is top if not then display button
    $(window).scroll(function () {
      if ($(this).scrollTop() > offSetTop) {
        $scrollToTopButton.fadeIn();
      } else {
        $scrollToTopButton.fadeOut();
      }
    });

    //Click event to scroll to top
    $scrollToTopButton.click(function () {
      $('html, body').animate({
        scrollTop: 0
      }, 800);
      return false;
    });

  });


  /*--------------header_fixed-------------------*/

  $(function () {
    var lastScrollTop = 0,
      delta = 5;
    $(window).scroll(function (event) {
      var st = $(this).scrollTop();

      if (Math.abs(lastScrollTop - st) <= delta)
        return;

      if (st > lastScrollTop) {
        // downscroll code
        $("#header").css('display', 'none').hover()
      } else {
        // upscroll code
        $("#header").css('display', 'block','backgroung','#181818');
      }
      lastScrollTop = st;
    });
  });

 
  /*---------------menu_icon_animation-------------*/

  $(document).ready(function(){
    $(".hamburger").click(function(){
      $(this).toggleClass("is-active");
    });
  });

  // /-------------Tooltip-----------------/

  $(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip();
  });

/*-----------------testimonial---------------*/

  var swiper = new Swiper(".feedback", {
    slidesPerView: 1,
    spaceBetween: 10,
    centeredSlides: false,
    loop: true,
    speed: 4000,
    autoplay: {
      delay: 2500,
      disableOnInteraction: false,
    },
    breakpoints: {
      640: {
        slidesPerView: 1,
        spaceBetween: 10,
      },
      768: {
        slidesPerView: 1,
        spaceBetween: 40,
      },
      1024: {
        slidesPerView: 1,
        spaceBetween: 10,
      },
    },
  });

  var swiper = new Swiper(".mostpopularSwiper", {
    slidesPerView: 1,
    spaceBetween: 20,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    breakpoints: {
      640: {
        slidesPerView: 1.1,
        spaceBetween: 0,
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 0,
      },
      1024: {
        slidesPerView: 3,
        spaceBetween: 0,
      },
    },
  });

/*-------------Most_popular------------*/

var swiper = new Swiper(".mostpopularSwiper", {
  slidesPerView: 1,
  spaceBetween: 20,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  breakpoints: {
    640: {
      slidesPerView: 1.5,
      spaceBetween: 0,
    },
    768: {
      slidesPerView: 2,
      spaceBetween: 0,
    },
    1024: {
      slidesPerView: 3,
      spaceBetween: 0,
    },
  },
});
  
/*-------------------youtubeSwiper-------------*/

var swiper = new Swiper(".youtubeSwiper", {
  slidesPerView: 1,
  spaceBetween: 20,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    600: {
      slidesPerView: 3,
      spaceBetween: 20
    },
    468:{
      slidesPerView: 2,
      spaceBetween: 10
    },
    1068:{
      slidesPerView: 4.5,
      spaceBetween: 50
    }
  }
});
/*-------------------instapost-------------*/

var swiper = new Swiper(".instapost", {
  slidesPerView: 2,
  spaceBetween: 10,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    600: {
      slidesPerView: 3,
      spaceBetween: 10
    },
    468:{
      slidesPerView: 2,
      spaceBetween: 10
    },
    1068:{
      slidesPerView: 5,
      spaceBetween: 10
    }
  }
});

/*-------------------instapost-------------*/

var swiper = new Swiper(".print_inv", {
  slidesPerView: 2,
  spaceBetween: 10,
  centeredSlides: true,
  paginationClickable: true,
  loop: true,
  slideToClickedSlide: true,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    600: {
      slidesPerView: 3,
      spaceBetween: 10
    },
    468:{
      slidesPerView: 2,
      spaceBetween: 10
    },
    1068:{
      slidesPerView: 3.95,
      spaceBetween: 20
    }
  }
});


/*--------mobile_stationeries_grid---------*/

var swiper = new Swiper(".staGrid", {
  slidesPerView: 2,
  spaceBetween: 15,
  centeredSlides: false,
  paginationClickable: true,
  loop: false,
  slideToClickedSlide: true,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    600: {
      slidesPerView: 3,
      spaceBetween: 15
    },
    468:{
      slidesPerView: 1,
      spaceBetween: 15
    }
  }
});
/*-------------------service_gallery-------------*/

var swiper = new Swiper(".service_gallery", {
  slidesPerView: 2,
  spaceBetween: 20,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    600: {
      slidesPerView: 3,
      spaceBetween: 30
    },
    468:{
      slidesPerView: 2,
      spaceBetween: 20
    },
    1068:{
      slidesPerView: 4.3,
      spaceBetween: 30
    }
  }
});

/*---------------gallery-thumbs-----------------*/

$(function () {
  var galleryThumbs = new Swiper(".gallery-thumbs", {
    centeredSlides: false,
    centeredSlidesBounds: true, 
    direction: "horizontal",
    spaceBetween: 30,
    slidesPerView: 2,
    loop:false,
    freeMode: false,
    watchSlidesVisibility: true,
    watchSlidesProgress: true,
    watchOverflow: true,
    breakpoints: {
      600: {
        direction: "vertical",
        slidesPerView: 2
      },
      468: {
        direction: "horizontal",
        slidesPerView: 3.2
      },
      1080: {
        slidesPerView: 2,
        direction: "vertical",
      }
    }
  });

  var galleryTop = new Swiper(".gallery-top", {
    direction: "horizontal",
    spaceBetween: 30,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev"
    },
    a11y: {
      prevSlideMessage: "Previous slide",
      nextSlideMessage: "Next slide",
    },
    keyboard: {
      enabled: true,
    },
    thumbs: {
      swiper: galleryThumbs
    }
  });
  galleryTop.on("slideChangeTransitionStart", function () {
    galleryThumbs.slideTo(galleryTop.activeIndex);
  });
  galleryThumbs.on("transitionStart", function () {
    galleryTop.slideTo(galleryThumbs.activeIndex);
  });
});


// slider-swiper
var swiper = new Swiper(".mySwiperSlide", {
  slidesPerView: 2,
  spaceBetween: 10,
  centeredSlides: false,
  loop: false,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
   navigation: {
     nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
 },
 breakpoints: {
  600: {
    slidesPerView: 3,
    spaceBetween: 20
  },
  468:{
    slidesPerView: 2,
    spaceBetween: 10
  },
  1068:{
    slidesPerView: 6,
    spaceBetween: 25
  }
}
 
});

var swiper = new Swiper(".mySwiperSlide2", {
  slidesPerView: 2,
  spaceBetween: 10,
  centeredSlides: false,
  loop: false,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
   navigation: {
     nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
 },
 breakpoints: {
  600: {
    slidesPerView: 3,
    spaceBetween: 20
  },
  468:{
    slidesPerView: 2,
    spaceBetween: 10
  },
  1068:{
    slidesPerView: 5,
    spaceBetween: 50
  }
}
 
});

/*----------------collect_detailsSlid-------------*/

var swiper = new Swiper(".collect_detailsSlid", {
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

/*----------------Lazy Loading------------------*/

(function () {
	var observer = new IntersectionObserver(onIntersect);

	document.querySelectorAll("[data-lazy]").forEach((img) => {
		observer.observe(img);
	});

	function onIntersect(entries) {
		entries.forEach((entry) => {
			if (entry.target.getAttribute("data-processed") || !entry.isIntersecting)
				return true;
			entry.target.setAttribute("src", entry.target.getAttribute("data-src"));
			entry.target.setAttribute("data-processed", true);
		});
	}
})();

/*----------------ImageZoom---------------------*/

$('.imgBox').imgZoom({
  boxWidth: 550,
  boxHeight: 550,
  marginLeft: 5,
  origin: 'data-origin',

});

/*-----------------profile_dropdown-------------------*/

$(document).ready(
  function() {
      $("#profileinfo").click(function() {
          $("#profile").fadeToggle();
      });
  });
/*-----------------Counter-------------------*/



/*--------------ASO.JS---------------*/

AOS.init();

//refresh animations

$(window).on('load', function () {
  AOS.init({
    once: true,
  });
});

/*----------------Swiper-------------------*/

// var swiper = new Swiper(".testimonial", {
//   slidesPerView: 1,
//   spaceBetween: 20,
//   slidesPerView: 'auto',
//   loop: true,
//   speed: 5000,
//   autoplay: {
//     delay: 2500,
//     disableOnInteraction: false,
//   },
// });

// var swiper = new Swiper(".provider", {
//   slidesPerView: 3,
//   spaceBetween: 30,
//   slidesPerView: 'auto',
//   loop: true,
//   speed: 5000,
//   autoplay: {
//     delay: 0,
//     disableOnInteraction: false,
//   },
//   pagination: {
//     el: ".swiper-pagination",
//     clickable: true,
//   },
//   navigation: {
//     nextEl: ".swiper-button-next",
//     prevEl: ".swiper-button-prev",
//   },
//   breakpoints: {
//     640: {
//       spaceBetween: 10,
//     },
//     768: {
//       slidesPerView: 3,
//       spaceBetween: 20,
//     },
//     1024: {
//       slidesPerView: 6,
//       spaceBetween: 30,
//     },
//   },
// });

/*------------Price_range------------*/

const rangeInput = document.querySelectorAll(".range-input input"),
priceInput = document.querySelectorAll(".price-input input"),
range = document.querySelector(".slider .progress");
let priceGap = 1000;

priceInput.forEach(input =>{
    input.addEventListener("input", e =>{
        let minPrice = parseInt(priceInput[0].value),
        maxPrice = parseInt(priceInput[1].value);
        
        if((maxPrice - minPrice >= priceGap) && maxPrice <= rangeInput[1].max){
            if(e.target.className === "input-min"){
                rangeInput[0].value = minPrice;
                range.style.left = ((minPrice / rangeInput[0].max) * 100) + "%";
            }else{
                rangeInput[1].value = maxPrice;
                range.style.right = 100 - (maxPrice / rangeInput[1].max) * 100 + "%";
            }
        }
    });
});

rangeInput.forEach(input =>{
    input.addEventListener("input", e =>{
        let minVal = parseInt(rangeInput[0].value),
        maxVal = parseInt(rangeInput[1].value);

        if((maxVal - minVal) < priceGap){
            if(e.target.className === "range-min"){
                rangeInput[0].value = maxVal - priceGap
            }else{
                rangeInput[1].value = minVal + priceGap;
            }
        }else{
            priceInput[0].value = minVal;
            priceInput[1].value = maxVal;
            range.style.left = ((minVal / rangeInput[0].max) * 100) + "%";
            range.style.right = 100 - (maxVal / rangeInput[1].max) * 100 + "%";
        }
    });
});

/*-------------filter_div---------------*/

$(function () {
    if($(window).width() < 980){ // your resolution
      $("#user").click(function()
        {
        $("#toggle-div").slideToggle(),
        $("#toggle-div a").on("click",function()
        {
          $("#toggle-div").slideToggle()
        });
      });
    }
    $("#close-sidebar").click(function(){
      $('.accordion-wrapper').hide()
    }) 
  });


  //Accordian
	$('.accordion').each(function () {
    var $accordian = $(this);
    $accordian.find('.accordion-head').on('click', function () {
          $(this).removeClass('open').addClass('close');
        $accordian.find('.accordion-body').slideUp();
        if (!$(this).next().is(':visible')) {
              $(this).removeClass('close').addClass('open');
            $(this).next().slideDown();
        }
    });
});



/*--------------change_drop_value------------*/

$(document).ready(function(){
  $("select").change(function(){
      $(this).find("option:selected").each(function(){
          var optionValue = $(this).attr("value");
          if(optionValue){
              $(".box").not("." + optionValue).hide();
              $("." + optionValue).show();
          } else{
              $(".box").hide();
          }
      });
  }).change();
});

$(document).ready(function(){
  $("select").change(function(){
      $(this).find("option:selected").each(function(){
          var optionValue = $(this).attr("value");
          if(optionValue){
              $(".box2").not("." + optionValue).hide();
              $("." + optionValue).show();
          } else{
              $(".box2").hide();
          }
      });
  }).change();
});

/*--------------------add_element--------------------------*/

$('.multi-field-wrapper').each(function() {
  var $wrapper = $('.multi-fields', this);
  $(".add-field", $(this)).click(function(e) {
      $('.multi-field:first-child', $wrapper).clone(true).appendTo($wrapper).find('input').val('').focus();
  });
  $('.multi-field .remove-field', $wrapper).click(function() {
      if ($('.multi-field', $wrapper).length > 1)
          $(this).parent('.multi-field').remove();
  });
});

/*------------quqntity-------------*/

$(document).ready(function() {
  $('.num-in span').click(function () {
      var $input = $(this).parents('.num-block').find('input.in-num');
    if($(this).hasClass('minus')) {
      var count = parseFloat($input.val()) - 1;
      count = count < 1 ? 1 : count;
      if (count < 2) {
        $(this).addClass('dis');
      }
      else {
        $(this).removeClass('dis');
      }
      $input.val(count);
    }
    else {
      var count = parseFloat($input.val()) + 1
      $input.val(count);
      if (count > 1) {
        $(this).parents('.num-block').find(('.minus')).removeClass('dis');
      }
    }
    
    $input.change();
    return false;
  });
  
});


/*--------------------responsiveTabs------------------------*/

function vertical_tabs()
	{
	if ($('.ux-vertical-tabs').length > 0)
		{
		$('.ux-vertical-tabs .tabs button').on("click", function()
			{
			var temp_tab = $(this).data('tab');
			var temp_tab_js = this.getAttribute('data-tab');
			var temp_content = $('.ux-vertical-tabs .maincontent .tabcontent[data-tab="' + temp_tab + '"]');
			var temp_content_js = document.querySelector('.ux-vertical-tabs .maincontent .tabcontent[data-tab="' + temp_tab_js + '"]');
			var temp_content_active_js = document.querySelector('.ux-vertical-tabs .maincontent .tabcontent.active');

			$('.ux-vertical-tabs .tabs button').removeClass('active');
			$('.ux-vertical-tabs .tabs button[data-tab="' + temp_tab + '"]').addClass('active');

			var animation_start = anime({ duration: 400, targets: temp_content_active_js, opacity:[1,0], translateX: [0,'100%'], easing: 'easeInOutCubic',
			complete: function()
				{
			    $('.ux-vertical-tabs .maincontent .tabcontent').removeClass('active');
				temp_content.addClass('active');
				var animation_end = anime({ duration: 400, targets: temp_content_js, opacity:[0,1], translateX: ['100%','0'], easing: 'easeInOutCubic' });
			  	}
			});
			});
		}
	}

$(function() 
  {
  vertical_tabs();
  });

  /*----------------imahe_upload-----------------*/

  jQuery(($) => {
    $('.attachment input[type="file"]')
      .on('change', (event) => {
      let el = $(event.target).closest('.attachment').find('.btn-file');
      
      el
        .find('.btn-file__actions__item')
      el
        .find('.btn-file__preview')
        .css({
          'background-image': 'url(' + window.URL.createObjectURL(event.target.files[0]) + ')'
        });
    });
  });

  /*------------------------*/

  $("#edit").click(function(event){
    event.preventDefault();
    $('.inputDisabled').removeAttr("disabled")
  });

  /*-------------shop_accordian------------------*/

  $('.toggle').click(function(e) {
  	e.preventDefault();
  
    let $this = $(this);
  
    if ($this.next().hasClass('show')) {
        $this.next().removeClass('show');
        $this.next().slideUp(350);
    } else {
        $this.parent().parent().find('li .inner').removeClass('show');
        $this.parent().parent().find('li .inner').slideUp(350);
        $this.next().toggleClass('show');
        $this.next().slideToggle(350);
    }
  });
  /*-------------------show hide dive-------------*/

$('.Logodive').hide()
jQuery('.AddButton').on('click',function(){
  jQuery('.Logodive').toggle();
})

 

//============add inputfield==================//

$(document).ready(function() {
  var buttonAdd = $("#add-button");
  var buttonRemove = $("#remove-button");
  var className = ".dynamic-field";
  var count = 0;
  var field = "";
  var maxFields =50;

  function totalFields() {
    return $(className).length;
  }

  function addNewField() {
    count = totalFields() + 1;
    field = $("#dynamic-field-1").clone();
    field.attr("id", "dynamic-field-" + count);
    field.children("label").text("Field " + count);
    field.find("input").val("");
    $(className + ":last").after($(field));
  }

  function removeLastField() {
    if (totalFields() > 1) {
      $(className + ":last").remove();
    }
  }

  function enableButtonRemove() {
    if (totalFields() === 2) {
      buttonRemove.removeAttr("disabled");
      buttonRemove.addClass("shadow-sm");
    }
  }

  function disableButtonRemove() {
    if (totalFields() === 1) {
      buttonRemove.attr("disabled", "disabled");
      buttonRemove.removeClass("shadow-sm");
    }
  }

  function disableButtonAdd() {
    if (totalFields() === maxFields) {
      buttonAdd.attr("disabled", "disabled");
      buttonAdd.removeClass("shadow-sm");
    }
  }

  function enableButtonAdd() {
    if (totalFields() === (maxFields - 1)) {
      buttonAdd.removeAttr("disabled");
      buttonAdd.addClass("shadow-sm");
    }
  }

  buttonAdd.click(function() {
    addNewField();
    enableButtonRemove();
    disableButtonAdd();
  });

  buttonRemove.click(function() {
    removeLastField();
    disableButtonRemove();
    enableButtonAdd();
  });
});

/*-----------Reatting-----------------*/

function ratingStar(star){
	star.click(function(){
		var stars = $('.ratingW').find('li')
		stars.removeClass('on');
		var thisIndex = $(this).parents('li').index();
		for(var i=0; i <= thisIndex; i++){
			stars.eq(i).addClass('on');
		}
    putScoreNow(thisIndex+1);
	});
}

function putScoreNow(i){
  $('.scoreNow').html(i);
}


$(function(){
	if($('.ratingW').length > 0){
			ratingStar($('.ratingW li a'));
	}
});

/*-------------review_dive Show------------*/

$(document).ready(function(){
  $(".show_hide").click(function(){
    $(".m_review_dive").toggle();
  });
});

/*-------------------Word Limit----------------*/

$(function(){
  $("#productform").validate(
    {
      rules: 
      {
        prodid: 
        {
          required: true,
          maxlength: 10
        },
        email: 
        {
          required: true,
          email: true,
          minlength:10
        },
        address:
        {
          required: true,
          rangelength:[10,250]
        },
        message: 
        {
          rangelength:[50,1050]
        }
      }
  });	
});

 /*------------Datepicker-------------*/
})(jQuery, window);