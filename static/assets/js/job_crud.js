
$(document).ready(function () {
console.log("loaded");
/**
 // * Create Book
 //     */
    // process the form
    $('#create_bookfrm').submit(function (e) {
         var confirmation = confirm("are you sure you want to Addd?");

       if (confirmation) {
        // console.log("Creating the book");
        e.preventDefault();
        // get the form data
        var formData = $("#create_bookfrm").serialize();
         // {
        //     'title': $('#id_title').val(),
        //     'dept': $('#id_dept').val(),
        //     'job_location': $('#id_job_location').val(),
        //     'vacancy': $('#id_vacancy').val(),
        //     'exp': $('#id_exp').val(),
        //     'skill': $('#id_skill').val(),
        //     'salary_from': $('#id_salary_from').val(),
        //     'salary_to': $('#id_salary_to').val(),
        //     'job_type': $('#id_job_type').val(),
        //     'status': $('#id_status').val(),
        //     'start_date': $('#id_start_date').val(),
        //     'end_date': $('#id_end_date').val(),
        //     'desc': $('#id_desc').val(),
        //     csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        //     contentType: 'application/x-www-form-urlencoded',
        //     encode: true,
        // };
        $.ajax({
            type: 'POST',
            url: 'create/',
            data: formData,
            dataType: 'json',
           
        }).done(function (data) {
            $(function () {
                 window.location.reload();
                /**
                 * Update book view
                //  */
                // $('#add_job').modal('toggle').slideUp(500);
                // $("#bookdata").append(
                //     '<tr id="book_row">' +
                //     '<td>' + data.data['id'] + '</td>' +
                //     '<td>' + data.data['title'] + '</td>' +
                //     '<td>' + data.data['dept'] + '</td>' +
                //     '<td>' + data.data['start_date'] + '</td>' +
                //     '<td>' + data.data['end_date'] + '</td>' +
                //     '<td>' + data.data['job_location'] + '</td>' +
                //     '<td>' + data.data['vacancy'] + '</td>' +
                //     '<td>' + data.data['exp'] + '</td>' +
                //     '<td>' + data.data['skill'] + '</td>' +
                //     '<td>' + data.data['salary_from'] + '</td>' +
                //     '<td>' + data.data['salary_to'] + '</td>' +
                //     '<td>' + data.data['job_type'] + '</td>' +
                //     '<td>' + data.data['status'] + '</td>' +
               
                //     '<td>' + data.data['desc'] + '</td>' +
                //     '<td>' + '<input type="button" class="edit-button " ' + 'id="' + data.data['id'] + '"' + 'name="edit-button' + data.data['id'] + '" value="Edit">' +
                //     '</td>' +
                //     '<td>' + '<input type="button" class="delete-button " ' + 'id="' + data.data['id'] + '"' + 'name="delete-button' + data.data['id'] + '" value="Delete">' +
                //     '</td>' +
                //     '</tr>'
                // )
            });
        });
    }});


/***Edit Viewq*/





    /**
     * Update Book
    //  */



//         $(document).on('click', '.edit-button', function (e) {
//         var confirmation = confirm("are you sure you want to remove the item?");

//        if (confirmation) {
//      // execute ajax
//         e.preventDefault();
//         row = $(this).closest('tr');
//         btn = e.target.id;      //get clicked button
//         del_id = $(this).attr(btn);
//         var formData = {
//             'id': btn,
//             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
//         };
//         $.ajax({
//             type: 'POST',       // define the type of HTTP verb we want to use (POST for our form)
//             url:"edit/" + formData.id + "/",
//             encode: true,
//             contentType: 'application/x-www-form-urlencoded',
//             crossDomain: false,
//             dataType: 'json',
//             data: formData,     // our data object
//             success: function (data) {
//                 /**
//                  * Update book view
//                  */
//                 // console.log('success', data);
//                                console.log('success', data);

//             },
//             error: function (exception) {
//                 alert('Exeption:' + exception);
//             }
//         });
//     }});
// });

   





 //    /**
 // //     * Delete Book
 //     */
    $(document).on('click', '.delete-button', function (e) {
        var confirmation = confirm("are you sure you want to remove the item?");

       if (confirmation) {
     // execute ajax
        e.preventDefault();
        row = $(this).closest('tr');
        btn = e.target.id;      //get clicked button
        del_id = $(this).attr(btn);
        var formData = {
            'id': btn,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        };
        $.ajax({
            type: 'POST',       // define the type of HTTP verb we want to use (POST for our form)
            url: "delete/" + formData.id + "/",
            encode: true,
            contentType: 'application/x-www-form-urlencoded',
            crossDomain: false,
            dataType: 'json',
            data: formData,     // our data object
            success: function (data) {
                /**
                 * Update book view
                 */
                // console.log('success', data);
                row.fadeOut(1000, function () {
                    $(this).remove();
                });
            },
            error: function (exception) {
                alert('Exeption:' + exception);
            }
        });
    }});
});



