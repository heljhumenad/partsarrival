$(document).ready(function () {
    //id = id_date_range
    //name = date_range
    $('input[name="date_hired"]').daterangepicker({
        singleDatePicker: true,
        showDropDowns: true,
    });
    $('input[name="date_hired').on('apply.daterangepicker',
        function (ev, picker) {
            $(this).val(picker.startDate.format('MM/DD/YYYY'));
        });
    $('input[name="date_hired"]').on('cancel.daterangepicker', function (ev, picker) {
        $(this).val('');
    });


    // Link two input forms to predict the value of the next input forms
    // based on the  input value of the first input forms 
    // ex two input forms if i put 1 in the first input forms the second with 
    // has pre populated data will predict the value of the first input form and 
    // give the exact value range of the first input form 

    // Input name that need to check 
    // first input
    // name = no_absences_rating 
    // id = id_no_absences_rating
    // using event handler to check the value of the form 

    // selection 
    // TODO
    // 1. Get the id of the input type
    // 2. Extract the value from input type 
    // 3. Check the value from the input type 
    //   3.1 Compare the value to the range of value in the input type (ex. first input type=4, check max and min value of selection box )
    // 4. Compare the value of first input type to the selection box
    // 4.1 trigger the set of value when hitting tab 
    // 5. Automatically Set the value of the selection box based on the value of first input type 
    // 6. Show the value of the selection box 

    // Hide message when alert success
    $(".alert").fadeTo(2000, 500).slideUp(500, function () {
        $(".alert").slideUp(500);
    });
})
