$( document ).ready(function() {
    var edit_profile = false;
    var edit_experience = false;
    var $skillTopValSelector = '#skillTopVal';
    var $skillSecondarySelector = '#skillSecondaryVal';

    /* * * * * * * * * * * * * * *
    * click event - toggle between edit and not edit mode
    * * * * * * * * * * * * * * * */
    $(".form-group button").click(function() {
        if(edit_profile){
            // go to NO edit mode
            edit_profile = false;
            $(".edit-state").toggle(false); // hide .edit-state
            $(".no-edit-state").toggle(true); // show .no-edit-state
        }else{
            // go to edit mode
            edit_profile = true;
            $(".edit-state").toggle(true); // show .edit-state
            $(".no-edit-state").toggle(false); // hide .no-edit-state
            findAllSkillId($skillTopValSelector);
            findAllSkillId($skillSecondarySelector);
        }
    });// button click

    /* * * * * * * * * * * * * * *
    * works for the TOP skills and SECONDARY skills
    * find the id of the skills
    * this method is called after the user clicks the edit button
    * to edit the edit mode
    * * * * * * * * * * * * * * * */
    function findAllSkillId(selector){
        // selector: defines if it is about top or secondary skills
        $( selector+" .skills-owned .result-item" ).each(function( index ) {
            console.log( index + ": " + $( this ).text() );
            var query;
            var all_skills = [];

            // read the name of the skills
            $(this).find('.hidden').html("");
            query = $(this).text();

            // erase the skills owned
            $(selector+' .skills-owned').html("");

            // find the skills that the user has and handle the HTML dom
            $.get('/account/get_skills_id/', {skills_owned: query}, function(data){
                var serializedData = JSON.parse(data.skill);
                console.log(serializedData);
                $.each(serializedData, function(index, value){
                    var skill_id = value.pk;
                    var skill_name = value.fields.name;

                    if(selector===$skillTopValSelector){
                        if(!$("input[name='skill_top_val1']").val()){
                            $("input[name='skill_top_val1']").val(skill_id);
                        }else if(!$("input[name='skill_top_val2']").val()){
                            $("input[name='skill_top_val2']").val(skill_id);
                        }else if(!$("input[name='skill_top_val3']").val()){
                            $("input[name='skill_top_val3']").val(skill_id);
                        }
                    }else if(selector===$skillSecondarySelector){
                        if(!$("input[name='skill_secondary_val1']").val()){
                            $("input[name='skill_secondary_val1']").val(skill_id);
                        }else if(!$("input[name='skill_secondary_val2']").val()){
                            $("input[name='skill_secondary_val2']").val(skill_id);
                        }else if(!$("input[name='skill_secondary_val3']").val()){
                            $("input[name='skill_secondary_val3']").val(skill_id);
                        }
                    }
                    $(selector+' .skills-owned').append("<span class='result-item'>"+skill_name+
                    "<span class='hidden'>"+skill_id+"</span>"+"</span>");
                });
            }); //AJAX call
        });
    }// findAllSkillId

    /* * * * * * * * * * * * * * *
    * type event - type a skill to input
    * * * * * * * * * * * * * * * */
    $("#skillTopVal input").keyup(function(){
        var query;
        query = $(this).val();

        searchSkill(query, '#skillTopVal');
    });// skill input key up

    /* * * * * * * * * * * * * * *
    * type event - type a skill to input
    * * * * * * * * * * * * * * * */
    $("#skillSecondaryVal input").keyup(function(){
        var query;
        query = $(this).val();

        searchSkill(query, '#skillSecondaryVal');
    });// skill input key up

    /* * * * * * * * * * * * * * *
    * search for skills according to the input value
    * * * * * * * * * * * * * * * */
    function searchSkill(query, selector){
        $.get('/account/get_skill_list/', {skill_query: query}, function(data){
            var serializedData = jQuery.parseJSON(data.skills);
            $(selector+' .skills-query-result').html("");
            $.each(serializedData, function( index, value ) {
                console.log(value.pk);

                if(selector === $skillTopValSelector &&
                value.pk != $("input[name='skill_top_val1']").val() &&
                value.pk != $("input[name='skill_top_val2']").val() &&
                value.pk != $("input[name='skill_top_val3']").val()){
                    // add the skills found under the search input
                    $(selector+' .skills-query-result').append("<span class='result-item'>"+value.fields.name+
                    "<span class='hidden'>"+value.pk+"</span>"+"</span>");
                }else if(selector === $skillSecondarySelector &&
                value.pk != $("input[name='skill_secondary_val1']").val() &&
                value.pk != $("input[name='skill_secondary_val2']").val() &&
                value.pk != $("input[name='skill_secondary_val3']").val()){
                    // add the skills found under the search input
                    $(selector+' .skills-query-result').append("<span class='result-item'>"+value.fields.name+
                    "<span class='hidden'>"+value.pk+"</span>"+"</span>");
                }//if - else
            });// each
        });// AJAX call
    };// searchSkill

    /* * * * * * * * * * * * * * *
    * click event to chose to add a top skill
    * * * * * * * * * * * * * * * */
    $(document).on('click', '#skillTopVal .skills-query-result .result-item', function(){
        var value_pk = $(this).find('.hidden').text();
        console.log('value_pk='+value_pk);

        // check if all skills are filled
        if(!$("input[name='skill_top_val1']").val()){
            $("input[name='skill_top_val1']").val(value_pk);
            $(this).appendTo('#skillTopVal .skills-owned');
        }else if(!$("input[name='skill_top_val2']").val()){
            $("input[name='skill_top_val2']").val(value_pk);
            $(this).appendTo('#skillTopVal .skills-owned');
        }else if(!$("input[name='skill_top_val3']").val()){
            $("input[name='skill_top_val3']").val(value_pk);
            $(this).appendTo('#skillTopVal .skills-owned');
        }else{
            alert('all skills filled');
        }// else if
    });// on click

    /* * * * * * * * * * * * * * *
    * click event to chose to add a secondary skill
    * * * * * * * * * * * * * * * */
    $(document).on('click', '#skillSecondaryVal .skills-query-result .result-item', function(){
        var value_pk = $(this).find('.hidden').text();
        console.log('value_pk='+value_pk);

        // check if all skills are filled
        if(!$("input[name='skill_secondary_val1']").val()){
            $("input[name='skill_secondary_val1']").val(value_pk);
            $(this).appendTo('#skillSecondaryVal .skills-owned');
        }else if(!$("input[name='skill_secondary_val2']").val()){
            $("input[name='skill_secondary_val2']").val(value_pk);
            $(this).appendTo('#skillSecondaryVal .skills-owned');
        }else if(!$("input[name='skill_secondary_val3']").val()){
            $("input[name='skill_secondary_val3']").val(value_pk);
            $(this).appendTo('#skillSecondaryVal .skills-owned');
        }else{
            alert('all skills filled');
        }// else if
    });// on click

    /* * * * * * * * * * * * * * *
    * click event to remove an owned top skill
    * * * * * * * * * * * * * * * */
    $(document).on('click', '#skillTopVal .skills-owned .result-item', function(){
        if(edit_profile){
            $(this).remove();
            var query =$("#skillTopVal input").val();
            searchSkill(query, $skillTopValSelector);

            $("input[name='skill_top_val1']").removeAttr('value');
            $("input[name='skill_top_val2']").removeAttr('value');
            $("input[name='skill_top_val3']").removeAttr('value');
            findAllSkillId($skillTopValSelector);
        }
    });// on click

    /* * * * * * * * * * * * * * *
    * click event to remove an owned secondary skill
    * * * * * * * * * * * * * * * */
    $(document).on('click', '#skillSecondaryVal .skills-owned .result-item', function(){
        if(edit_profile){
            $(this).remove();
            var query =$("#skillSecondaryVal input").val();
            searchSkill(query, $skillSecondarySelector);

            $("input[name='skill_secondary_val1']").removeAttr('value');
            $("input[name='skill_secondary_val2']").removeAttr('value');
            $("input[name='skill_secondary_val3']").removeAttr('value');
            findAllSkillId($skillSecondarySelector);
        }
    });// on click

/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*   CLICK EVENTS FOR THE EXPERIENCE SECTION
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

    function cancelEditExperience(){
       edit_experience = false;
       $("#pastPositions .edit-state").hide();
       $("#pastPositions .no-edit-state").show();
       $('form.new-position').hide();
       $('#pastPositions .add-button').show();
    };// cancelEditExperience()

    // click event
    // go to edit mode of the experience
    $(document).on('click', '#pastPositions .edit-btn',function(){
        var $this = $(this);

        if(!edit_experience){
            edit_experience = true;
            var $noEditSelector = $this.closest('.no-edit-state');

            $noEditSelector.hide();
            $noEditSelector.siblings('.edit-state').show();

            $('#pastPositions .add-button').hide();
        }
    });

    // click event
    // cancel the edit mode of the experience
    $(document).on('click', '#pastPositions .cancel-btn', function(){
       cancelEditExperience();
    });

    // click event
    // add new experience
    $(document).on('click', '#pastPositions .add-button', function(){
        $(this).hide();
        $('form.new-position').show();
    }); // on click event

    $('form#editPosition').submit(function(event){
        event.preventDefault();
        $.post('/account/edit_position', $(this).serialize(), function(data){
            console.log(data);
            cancelEditExperience();
        });
    });

    $('form#deletePosition').submit(function(event){
        event.preventDefault();
        $.post('/account/delete_position', $(this).serialize(), function(data){
            var id = jQuery.parseJSON(data).id;

            if(id > 0){
                $(event.target).closest('.experience-entity').remove();
            }
        });
    });

});
