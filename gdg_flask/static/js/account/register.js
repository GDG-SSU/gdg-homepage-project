/**
 * Created by Genus on 2016. 2. 4..
 */
/**
 * Created by Genus on 2016. 1. 2..
 */
$(document).ready(function(){
    //바로 아랫것은 함수에 인자를 전달 못함
    //document.getElementById('user_id').addEventListener('blur', account_check_field);
    document.getElementById('user_id').addEventListener('blur', function(){
        account_check_field(this);
    });

});

function account_check_field(field,script_url){
    if (!script_url){
        var script_url = '/account/check/field';
    }
    else{
        var script_url = script_url;
    }


    var field_id = field.id;
    var field_value = field.value;

    $.getJSON(script_url, {
        field_id: field_id,
        field_value: field_value
    }, function(data) {
        if(field.nextElementSibling){
            field.nextElementSibling.remove();
            field.parentNode.parentNode.classList.remove('has-success');
            field.parentNode.parentNode.classList.remove('has-error');
        }
        if(data.result){
            var node = document.createElement('span');

            node.setAttribute('class','glyphicon glyphicon-ok form-control-feedback');
            node.setAttribute('aria-hidden', 'true');
            field.parentNode.appendChild(node);
            field.parentNode.parentNode.classList.add('has-success');
        }
        else{
            var node = document.createElement('span');
            node.setAttribute('class', 'glyphicon glyphicon-remove form-control-feedback');
            node.setAttribute('aria-hidden', 'true');
            field.parentNode.appendChild(node);
            field.parentNode.parentNode.classList.add('has-error');
        }

    });
    return false;
}

