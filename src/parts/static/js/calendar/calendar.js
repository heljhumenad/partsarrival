 $(document).ready(function() {

  $('input[name="datestart"]').daterangepicker({
    //   autoUpdateInput: false,
      singleDatePicker: true,
      locale: {
          cancelLabel: 'Clear'
      }
  });
  $('input[name="datestart"]').on('apply.daterangepicker', function(ev, picker) {
      $(this).val(picker.startDate.format('MM/DD/YYYY'));
  });

  $('input[name="dateend"]').on('cancel.daterangepicker', function(ev, picker) {
      $(this).val('');
  });

  $('input[name="dateend"]').daterangepicker({
      autoUpdateInput: false,
      singleDatePicker: true,
      locale: {
          cancelLabel: 'Clear'
      }
  });
  $('input[name="dateend"]').on('apply.daterangepicker', function(ev, picker) {
      $(this).val(picker.startDate.format('MM/DD/YYYY'));
  });

  $('input[name="dateend"]').on('cancel.daterangepicker', function(ev, picker) {
      $(this).val('');
  });





});
