(function ($, window, Typist) {

//*====================Left_menu====================*//

document.addEventListener("DOMContentLoaded", function(event) {

    const showNavbar = (toggleId, navId, bodyId, headerId) =>{
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId),
    bodypd = document.getElementById(bodyId),
    headerpd = document.getElementById(headerId)
    
    // Validate that all variables exist
    if(toggle && nav && bodypd && headerpd){
    toggle.addEventListener('click', ()=>{
    // show navbar
    nav.classList.toggle('show')
    // change icon
    toggle.classList.toggle('bx-x')
    // add padding to body
    bodypd.classList.toggle('body-pd')
    // add padding to header
    headerpd.classList.toggle('body-pd')
    })
    }
    }
    
    showNavbar('header-toggle','nav-bar','body-pd','header')
    
    /*===== LINK ACTIVE =====*/
    const linkColor = document.querySelectorAll('.nav_link')
    
    function colorLink(){
    if(linkColor){
    linkColor.forEach(l=> l.classList.remove('active'))
    this.classList.add('active')
    }
    }
    linkColor.forEach(l=> l.addEventListener('click', colorLink))
    
    // Your code to run since DOM is loaded and ready
    });

    function myFunction() {
        var x = document.getElementById("demo");
        if (x.style.display === "none") {
        x.style.display = "block";
        } else {
        x.style.display = "none";
        }            
    }


  // ---------------invoice-download---------------------

 
// add element invoice
$('.extra-fields-customer').click(function() {
  $('.customer_records').clone().appendTo('.customer_records_dynamic');
  $('.customer_records_dynamic .customer_records').addClass('single remove');
  $('.single .extra-fields-customer').remove();
  $('.single').append('<a href="#" class="remove-field btn-remove-customer">Remove Fields</a>');
  $('.customer_records_dynamic > .single').attr("class", "remove");

  $('.customer_records_dynamic input').each(function() {
    var count = 0;
    var fieldname = $(this).attr("name");
    $(this).attr('name', fieldname + count);
    count++;
  });

});

$(document).on('click', '.remove-field', function(e) {
  $(this).parent('.remove').remove();
  e.preventDefault();
});
/*-----------edit_divshow-------------*/

$(document).ready(function () {
  $("#btn").click(function () {
      $("#Create").toggle();
  });
});


// allocate dropdown image
$(function() {
  // Set
  var main = $('div.mm-dropdown .textfirst')
  var li = $('div.mm-dropdown > ul > li.input-option')
  var inputoption = $("div.mm-dropdown .option")
  var default_text = 'Select<img src="https://cdn4.iconfinder.com/data/icons/ionicons/512/icon-arrow-down-b-128.png" width="10" height="10" class="down" />';

  // Animation
  main.click(function() {
    main.html(default_text);
    li.toggle('fast');
  });

  // Insert Data
  li.click(function() {
    // hide
    li.toggle('fast');
    var livalue = $(this).data('value');
    var lihtml = $(this).html();
    main.html(lihtml);
    inputoption.val(livalue);
  });
});


// select_option
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



//*============Select_dropdown==================*//

$(".custom-select").each(function() {
    var classes = $(this).attr("class"),
        id      = $(this).attr("id"),
        name    = $(this).attr("name");
    var template =  '<div class="' + classes + '">';
        template += '<span class="custom-select-trigger">' + $(this).attr("placeholder") + '</span>';
        template += '<div class="custom-options">';
        $(this).find("option").each(function() {
          template += '<span class="custom-option ' + $(this).attr("class") + '" data-value="' + $(this).attr("value") + '">' + $(this).html() + '</span>';
        });
    template += '</div></div>';
    
    $(this).wrap('<div class="custom-select-wrapper"></div>');
    $(this).hide();
    $(this).after(template);
  });
  $(".custom-option:first-of-type").hover(function() {
    $(this).parents(".custom-options").addClass("option-hover");
  }, function() {
    $(this).parents(".custom-options").removeClass("option-hover");
  });
  $(".custom-select-trigger").on("click", function() {
    $('html').one('click',function() {
      $(".custom-select").removeClass("opened");
    });
    $(this).parents(".custom-select").toggleClass("opened");
    event.stopPropagation();
  });
  $(".custom-option").on("click", function() {
    $(this).parents(".custom-select-wrapper").find("select").val($(this).data("value"));
    $(this).parents(".custom-options").find(".custom-option").removeClass("selection");
    $(this).addClass("selection");
    $(this).parents(".custom-select").removeClass("opened");
    $(this).parents(".custom-select").find(".custom-select-trigger").text($(this).text());
});

})(jQuery, window);


// description
var ghostEditor = {
  bindEvents: function() {
    this.bindDesignModeToggle();
    this.bindToolbarButtons();
  },

  bindDesignModeToggle: function() {
    $('#page-content').on('click', function(e) {
      document.designMode = 'on';
    });

    $('#page-content').on('click', function(e) {
      var $target = $(e.target);

      if ($target.is('#page-content')) {
        document.designMode = 'off';
      }
    });
  },

  bindToolbarButtons: function() {
    $('#toolbar').on('mousedown', '.icon', function(e) {
      e.preventDefault();
      var btnId = $(e.target).attr('id');
      this.editStyle(btnId);
    }.bind(this));
  },

  editStyle: function(btnId) {
    var value = null;

    if (btnId === 'createLink') {
      if (this.isSelection()) value = prompt('Enter a link:');
    }

    document.execCommand(btnId, true, value);
  },

  isSelection: function() {
    var selection = window.getSelection();
    return selection.anchorOffset !== selection.focusOffset
  },

  init: function() {
    this.bindEvents();
  },
}

ghostEditor.init();

function getContent() {
	var content = document.getElementById('page').innerHTML;
	alert(content);
}

/*---------------Tooltip----------------*/

$(function () {
  $('[data-toggle="tooltip"]').tooltip({
    placement: 'top'
  });
});





// -------------feedback-comment------------------
// $(document).ready(function(){
//   $(".cmt-show").click(function(){
//     $(".more_cmt").toggle();
//   });
// });




$(document).ready(function() {
  $(".set > a").on("click", function() {
    if ($(this).hasClass("active")) {
      $(this).removeClass("active");
      $(this)
        .siblings(".content")
        .slideUp(200);
      $(".set > a i")
        .removeClass("fa-minus")
        .addClass("fa-plus");
    } else {
      $(".set > a i")
        .removeClass("fa-minus")
        .addClass("fa-plus");
      $(this)
        .find("i")
        .removeClass("fa-plus")
        .addClass("fa-minus");
      $(".set > a").removeClass("active");
      $(this).addClass("active");
      $(".content").slideUp(200);
      $(this)
        .siblings(".content")
        .slideDown(200);
    }
  });
});





// -------------rating------------------
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


$(document).ready(function() {
    
  //alert('here');

$('.tabs a').click(function(){

   $('.panel').hide();
   $('.tabs a.active').removeClass('active');
   $(this).addClass('active');
   
   var panel = $(this).attr('href');
   $(panel).fadeIn(1000);
   
   return false;  // prevents link action
  
});  // end click 

   $('.tabs li:first a').click();
   
}); // end ready



/*-------------data_table---------------*/

$(document).ready(function() {
  $('#example').DataTable();
} );

// input_readonly
// $("#edit").click(function(event){
//   event.preventDefault();
//   $('.inputDisabled').removeAttr("disabled")
// });

// --------------------add_element--------------------------

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

// image_upload

function img_pathUrl(input){
  $('#img_url')[0].src = (window.URL ? URL : webkitURL).createObjectURL(input.files[0]);
}

function img_pathUrl1(input){
  $('#img_url1')[0].src = (window.URL ? URL : webkitURL).createObjectURL(input.files[0]);
}

// --------------approved_toggle----------------
$(document).ready(function(){
  $(".approved").click(function(){
    $("#approved_show").toggle();
  });
  $(".reject").click(function(){
    $("#reject_show").toggle();// --------------reject_toggle----------------
  });
  $("#approve_hide").click(function(){
    $("#approved_show").hide();
  });
  $("#reject_hide").click(function(){
    $("#reject_show").hide();
  });
  $("#addPayment").click(function(){
    $("#addPaymentShow").toggle(); // -------------add payment------------------
  });
 

});


// date_time
$(".date1").flatpickr({
  minDate: "2020-01",
  dateFormat: "d-m-y",
});

$(".time").flatpickr({
enableTime: true,
noCalendar: true,
dateFormat: "H:i",
});


// ------------multiselection options-----------------

jQuery('#photoSelect').multiselect({
  columns: 1,
  placeholder: 'Select Photo',
  search: true
});
jQuery('#colorSelect').multiselect({
  columns: 1,
  placeholder: 'Select Color',
  search: true
});
jQuery('#shapeSelect').multiselect({
  columns: 1,
  placeholder: 'Select Shape',
  search: true
});
jQuery('#styleSelect').multiselect({
  columns: 1,
  placeholder: 'Select Style',
  search: true
});
jQuery('#sizeSelect').multiselect({
  columns: 1,
  placeholder: 'Select Size',
  search: true
});
jQuery('#themeSelect').multiselect({
  columns: 1,
  placeholder: 'Select Theme',
  search: true
});
jQuery('#formatSelect').multiselect({
  columns: 1,
  placeholder: 'Select Format',
  search: true
});


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


//============swiper-slide==================//
var swiper = new Swiper(".collection-tab-swiper", {
  slidesPerView: 1.65,
  spaceBetween: 10,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    640: {
      slidesPerView: 2.5,
      spaceBetween: 0,
    },
    768: {
      slidesPerView: 3.5,
      spaceBetween: 0,
    },
    1024: {
      slidesPerView: 6.5,
      spaceBetween: 0,
    },
    1460: {
      slidesPerView: 8,
      spaceBetween: 0,
    },
  },
});

//============swiper-slide==================//



// currentdate
let cdate = document.getElementById('cdate')
let cweek = document.getElementById('cweek')

let d = new Date().toLocaleString('en-us',{month:'short', year:'numeric',day: 'numeric'})

const weekday = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"];

const w = new Date();
let day = weekday[w.getDay()];

cdate.innerHTML = d
cweek.innerHTML = day

console.log(day)
// ----------------------





// ----------------------










