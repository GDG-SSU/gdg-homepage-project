/**
 * Created by Genus on 2016. 2. 4..
 */
/**
 * Created by Genus on 2016. 1. 2..
 */
$(document).ready(function(){

    document.getElementById('user_id').addEventListener('blur', user_duplicate_check);

});

function user_duplicate_check(){
    var script_url = '/account/check/is_user_duplicate';

    var input = document.getElementById('user_id');
    var user_id = input.value;
    console.log('b');
    $.getJSON(script_url, {
        user_id: user_id
    }, function(data) {
        if(input.nextElementSibling){
            input.nextElementSibling.remove();
            input.parentNode.parentNode.classList.remove('has-success');
            input.parentNode.parentNode.classList.remove('has-error');
        }
        if(data.result){

            var node = document.createElement('span');
            node.setAttribute('class', 'glyphicon glyphicon-remove form-control-feedback');
            node.setAttribute('aria-hidden', 'true');
            input.parentNode.appendChild(node);
            input.parentNode.parentNode.classList.add('has-error');
        }
        else{
            var node = document.createElement('span');

            node.setAttribute('class','glyphicon glyphicon-ok form-control-feedback');
            node.setAttribute('aria-hidden', 'true');
            input.parentNode.appendChild(node);
            input.parentNode.parentNode.classList.add('has-success');


        }

    });
    return false;
}

