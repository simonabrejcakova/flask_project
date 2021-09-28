
//----------------------------------------------------------------------
$('#search').bind('input', function() {
    console.log("changing");
} );

//-------------------------------------------------------
console.log("trying")
//source: https://stackoverflow.com/questions/5886858/full-text-search-in-html-ignoring-tags/5887719#5887719
function doSearch(text,color="yellow") {
    if (color!="transparent") {
      doSearch(document.getElementById('hid_search').value,"transparent"); 
      document.getElementById('hid_search').value = text; 
      }
    if (window.find && window.getSelection) {
        document.designMode = "on";
        var sel = window.getSelection();
        sel.collapse(document.body, 0);
        
        while (window.find(text)) {
            document.execCommand("HiliteColor", false, color);
            sel.collapseToEnd();
        }
        document.designMode = "off";
    } else if (document.body.createTextRange) {
        var textRange = document.body.createTextRange();
        while (textRange.findText(text)) {
            textRange.execCommand("BackColor", false, color);
            textRange.collapse(false);
        }
    }
}


//-------------------------------------------------

//https://stackoverflow.com/questions/30169906/scrolling-to-anchor-and-make-nav-fixed#
var fixmeTop = $('.anchor-links').offset().top;

$(window).scroll(function() {
    var currentScroll = $(window).scrollTop();
    if (currentScroll >= fixmeTop){
        $('.anchor-links').addClass("sticky");
    } else {
        $('.anchor-links').removeClass("sticky");
    }
});

$('.goSmoothly').click(function(event){		
    event.preventDefault();
    $(this).addClass('active');
    if( $('.anchor-links').hasClass("sticky")) {
    $('html,body').animate({
        scrollTop: $(this.hash).offset().top - 100
    }, 500);
    } else {
    $('html,body').animate({
        scrollTop: $(this.hash).offset().top - 220
    }, 500);    
    }
});