$(document).ready(function() {
    
    $('.known').change(function() {
        if($('#new_article').attr('readonly') == false) {
            $('#new_article').attr('readonly', true);
        }
    });
    
    $('#unknown').change(function() {
        if($('#new_article').attr('readonly') == true) {
            $('#new_article').removeAttr('readonly');
        }
    });

    $('#new_article').click(function() {
        if($('#new_article').attr('readonly') == true) {
            $('#new_article').removeAttr('readonly');
            $('#unknown').attr('checked', true);
        }
    });
    
    $('.known').change(function() {
        if($('#new_link').attr('readonly') == false) {
            $('#new_link').attr('readonly', true);
        }
    });
    
    $('#unknown').change(function() {
        if($('#new_link').attr('readonly') == true) {
            $('#new_link').removeAttr('readonly');
        }
    });

    $('#new_link').click(function() {
        if($('#new_link').attr('readonly') == true) {
            $('#new_link').removeAttr('readonly');
            $('#unknown').attr('checked', true);
        }
    });
    
});