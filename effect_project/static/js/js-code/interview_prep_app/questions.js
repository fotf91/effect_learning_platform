jQuery( document ).ready(function() {
    var $answerForm = '.interview-answer';
    var $TMPL_app_content = '#TMPLappContentBody';
    var $appContentBody = '.app-environment .body';

    $(document).on('submit', $answerForm, function(event){
        event.preventDefault();
        $.post('/interview/questions/pro/', $(this).serialize(), function(data){
            console.log(data);
            var serializedData = jQuery.parseJSON(data.returnedJson);

            $.each(serializedData, function(index, value){
                var templateData = {
                    progress_bar_value: value.fields.question_num*10,
                    question_num: value.fields.question_num,
                    question_text: value.fields.question_text,
                    evaluated_skills: value.fields.evaluated_skills,
                    id: value.fields.id, // the id of the current question-anwser object fetched
                    answer_advice: value.fields.answer_advice,
                    answer_pro_tip: value.fields.answer_pro_tip,
                    specialist_full_name: value.fields.specialist_full_name,
                    specialist_position: value.fields.specialist_position,
                    specialist_company: value.fields.specialist_company
                };

                var template = $($TMPL_app_content).html();

                $($appContentBody).html('');// empty the old content of the application body

                var newHtml = Mustache.to_html(template, templateData);// add the new content of the application body
                $($appContentBody).append(newHtml);
            });// each
        });// post
    });// submit form - edit position
});
