

// delete modal the button of delete has id = confirmDeleteModal
// create function that will accept the button id when user click the delete button 
$(document).on('click', '.confirm-delete', function () {
    console.log($("#confirmDeleteModal").attr("caller-id", $(this).attr("id")));
    var caller = $("#confirmDeleteButtonModal").closest(".modal").attr("caller-id");
    // window.location = $("#".concat(caller)).attr("href");
    //$("#confirmDeleteModal").attr("caller-id", $(this).attr("id"));
});

//   $(document).on('click', '#confirmDeleteButtonModal', function () {
// var caller = $("#confirmDeleteButtonModal").closest(".modal").attr("caller-id");
// console.log( $("#confirmDeleteButtonModal").closest(".modal").attr("caller-id"));
// window.location = $("#".concat(caller)).attr("href");
//console.log(window.location);
//});

// AJAX POST
$('#confirm-delete').click(function () {
    console.log('am i called');
    var delete_id = $("#confirmDeleteModal").attr("caller-id", $(this).attr("id"));
    $.ajax({
        type: "POST",
        url: "/employee/delete/delete_id",
        //dataType: "json",
        //data: {"item": $(".todo-item").val() },
        success: function (data) {
            //  alert(data.message);
            alert("Already delete");
        }
    });

});


//Django own bypass csrf tokenizer for XHR Request
function getCookie(name) {
    var cookieValue = null;
    var i = 0;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (i; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
