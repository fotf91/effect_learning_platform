jQuery( document ).ready(function() {
    var $answerForm = '.interview-answer';
    var $TMPL_app_content = '#TMPLappContentBody';
    var $appContentBody = '.app-environment .body';

    $(document).on('submit', $answerForm, function(event){
        event.preventDefault();
        $.post('/interview/questions/pro/01/', $(this).serialize(), function(data){
        });// post
    });// submit form - edit position
});
